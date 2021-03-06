from utils import run_bigquery, strings_list

FROM = '2018-12-01'
TO = '2018-12-02'

persons = run_bigquery(name='persons', sql=f"""
SELECT
  COUNT(*) AS mentions_count,
  person
FROM (
  SELECT
    DocumentIdentifier,
    REGEXP_REPLACE(personOffset, r',.*', '') AS person
  FROM
    `gdelt-bq.gdeltv2.gkg_partitioned` gkg,
    UNNEST(SPLIT(V2Persons ,';')) AS personOffset
  WHERE
    _PARTITIONTIME >= TIMESTAMP('{FROM}')
    AND _PARTITIONTIME < TIMESTAMP('{TO}'))
GROUP BY
  person
ORDER BY
  mentions_count DESC
LIMIT 20
""")

sources = run_bigquery(name='sources', sql=f"""
SELECT
  MentionSourceName as source_name,
  COUNT(*) mentions_count
FROM
  `gdelt-bq.gdeltv2.eventmentions_partitioned`
WHERE
  _PARTITIONTIME >= TIMESTAMP('{FROM}')
  AND _PARTITIONTIME < TIMESTAMP('{TO}')
GROUP BY
  source_name
ORDER BY
  mentions_count DESC
LIMIT 20
""")

mentions = run_bigquery(name='mentions', sql=f"""
SELECT
  COUNT(*) mentions_count,
  source_name,
  person,
  AVG(tone) AS tone_avg,
  STDDEV(tone) AS tone_std
FROM (
  SELECT
    DocumentIdentifier,
    SourceCommonName AS source_name,
    CAST((SPLIT(V2Tone)[OFFSET(0)]) AS FLOAT64) AS tone,
    REGEXP_REPLACE(personOffset, r',.*', '') AS person
  FROM
    `gdelt-bq.gdeltv2.gkg_partitioned` gkg,
    UNNEST(SPLIT(V2Persons,';')) AS personOffset
  WHERE
    _PARTITIONTIME >= TIMESTAMP('{FROM}')
    AND _PARTITIONTIME < TIMESTAMP('{TO}'))
WHERE
  person IN ({strings_list(persons.person.values.tolist())})
  AND source_name IN ({strings_list(sources.source_name.values.tolist())})
GROUP BY
  person,
  source_name
ORDER BY
  mentions_count DESC,
  person,
  source_name
LIMIT
  5000
""")

mentions.to_csv('mentions.csv', index=False)
