# Cinema: is there a gender gap?
## Milestone 2


### Abstract

The goal of the project is to understand how public opinion about the movies can impact the film industry. For this, we are using Quotebank, a dataset of speaker-attributed quotations that were extracted from news articles and web domains between 2008 and 2020. By automatically analyzing quotations about movies in the media, this project aims to respond the following question : *What can people sayings say about the film industry, and how gender affects it ?* The first part of the project deals with the analysis of the relation between quotations and the general reception a film receives, focusing on gender issues. In a second part, quotations will be used to predict the different characteristics of a film.


### Research Questions

1. Who are the people talking about cinema, regarding gender and age ?

2. How does the memorability of a movie evolve regarding his characteristics (gender of producer/actors, genre of movies, ratings, etc.) ?

3. Could Quotebank's data predict the genre and/or the ratings of a movie ?


### Proposed additional datasets

In addition to Quotebank, two other databases will be used for this project :

- Wikidata

A database that provides additional attributes about people of interest. In order to answer our research questions, we need to extract the gender, the age of different protagonists (speakers, producers, actors), and release date of the movies. Additional metadata about speakers in the Quotebank dataset are already provided in a file named speaker_attributes.parquet. This file will be enriched with attributes of other protagonists, that will be extract wih a python3 code. API's will be used for this.
source : https://www.wikidata.org/

- IMDb

Internet Movie Database (IMDb) is an open source database that provides a lot of information about movies. This database is available online, separated in six datasets. This datasets were concatenated and treated in one single dataset. Columns were filtrated regarding of the needs of the research. Columns of interest are the following : title, year, genres, crew (producer, cinematographer, writer), actors, ratings.  
source : https://www.imdb.com/interfaces/


### Method

We created four notebooks, one for pre-processing and one for each question. This allows us to better distribute the work within the team and reduce the risk of conflict

#### Notebook_0: Preprocessing
To answer our questions, we need to select relevant elements for each dataset in order to reduce their size and therefore the following tasks' computing time.
- For Quotebank dataset, we decide to keep only the quotes presenting the keywords "movie", "cinema" and “film” in either the quote itself or the url of the articles.
- For Wikidata, for all the informations about the Quotebank speakers, we used the provided structured data (parquet files) to extract the gender, the age of the speaker and the release date of movies. For the actors and crew members from the films, we made a python script based on Wikidata API to collect info based on IMDb ID. We did so because in our opinion it was better to do so than to download and parse the json dump of 100GB.
- For IMDb dataset, we filtered out all series & co to keep only the informations about movies. Then we need to enrich the dataset with the gender of the actors and crew members via the Wikidata API.

#### Notebook_1: Question 1
First, for question one, about who taking about cinema, we need to attribute gender and age to speakers. This information can be reach by research quote’s speaker’s gender and age in wikidata.  Then, an analysis of these variable can be realized using statistic test, distribution, and regression.

#### Notebook_2: Question 2
For the second question, we need to find movies of interest in quotebank. To do that, movie’s name in IMDb can serve as a keyword to extract quote related to movie in quotebank. Then, thanks to IMDb and Wikidata, we can add, for each movie selected, speaker’s, actor’s and producer’s gender, movie’s rating and release date of the movies. To assign the gender, we decides that if more than 50% of actors are female, in concequence global gender is female. Finally, in order to see the evolution of the movie’s memorability, a timeline of the quotes can be done. An analysis of memorability considering the features can now be done using statistic test between variables.

#### Notebook_3: Question 3
Finally, we wonder if it’s possible to predict movie’s genre and ratings regarding several features. We want to test if the memorability of a movie and the gender of actors, directors, producers and writers are predictive of the genre and the rating of a movie. To do so, we will train a model under a supervised learning method, using a logistic or linear regression.


### Proposed timeline and Organization within the team

Milestone 3 is due on 17 December and homework 2 is due on 26 November. For M3 we need to complete the project proposed in M2 and communicate our result with data story.

•	Until 26 November the data should be enriched and ready to analyse

- Benoit & Inès: cleaning QUOTEBANK plus adding gender and age
- Céline & Maud: cleaning IMDb plus adding gender and age for people of interest with Wikidata API

•	26 November until 3 December the question 1 and 2 should be done

- Benoit: process the data to answer question 1
- Céline: process the data to answer question 2
- Maud and Inès: visualize data and create story to questions 1 and 2
- All team: start processing data for question 3

•	3 December until 10 December the question 3 should be done and start to learn how Jekyll works.

- Group working together to response question 3
- One of the team member will focus on Jeckyll

•	10 December until 17 December we will create the web site with our data story and complete README with members contributions and URL of the data story.

- Group create data story for question 3
- Maud finishes the README


### Questions for TAs

Crossing databases is going to pose a data size problem. We are thinking about reducing the data of interest to one or two particular years (e.g. 2018-2019 to be recent without taking into account Covid-related variables).
