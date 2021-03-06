# Proposal

## Project name
A network of news sites

## Objective (min 300 words)
The Gdelt project provide several datasets related to the news and the news coverage. One of
them relates news events to a unique ID and reports any publication about this event in the online news. A
network of news sites can be made to get a better picture of how much they share the same information. News
that report the same events would be linked in the network. The connection weights would increase as the
number of shared news increases. Can we make some interesting and clean visualizations of the news sites
landscape? Can we categorize them? Are there news sites that are more central? Do we get different networks if
we take into account news related to particular topics? Can we combine additional info present in the data with
the graph to get additional insights?

The final design of the website will likely change before submission, but at present we intend for the central feature of our website design to be a single window with an interactive graph visualization. The visualization will have multiple views (perhaps 3-4) that the user can toggle based on which information they are interested in. In the visualizations, nodes will represent news sources, and edge weights will vary based on which parameters we find interesting after exploring the dataset. Weights would likely be related to the number of stories two news outlets shared out of a set of news outlets. Variables in different views include the geographic location of events, the organizations (nation states, political factions, non-governmental organizations, inter-governmental organizations, etc.) involved, the impact of the event as noted in the database, the time of event, the length of the articles (short summaries vs in-depth investigations), and sentiment analysis (e.g., a certain weight color for strong sentiment correlation and a different weight color for conflicting sentiment correlation). In the case of time analysis a slider could show a variation in the graph visualization at different points in time. 

In the event that time proves to be a particularly interesting variable to investigate, instead of having multiple graph views, we could have one graph view with another line graph window that shows the change in connection weights of two news sources over time (sources which the user would select from the graph.)

Varying the location (clustering) of the nodes in the visualization and the color of the nodes/edges may also be explored.

(Word count: ~140 from the lab's proposa; ~260 added)

## Target audience
Our visualization will be interested in anyone interested in learning about media bias. While the primary audience will likely be consumers that are interested in evaluating the credibility of the news they view, our visualization may also be useful for those studying media bias at the level of academia or public policy.

## Project tags
\#Media, \#MediaBias, \#News, \#GraphVisualizations, \#GDELT

## Dataset description
The GDELT Project monitors the world's broadcast, print, and web news from nearly every corner of every country in over 100 languages and identifies the people, locations, organizations, themes, sources, emotions, counts, quotes, images and events driving our global society every second of every day, creating a free open platform for computing on the entire world (From the GDELT website).

Our dataset will be a subset of this data, filtered using the Google BigQuery search tool offered for free by the GDELT organization based on the features discussed in the "Objective" section. 

## Dataset URL
https://www.gdeltproject.org/#downloading

## Other

## SCIPERs
250300 - Matthieu Bovel
237913 - Ruslan Aydarkhanov 
295269 - Daniel Smarda
