# Cinema : is there a gender gap ?


### Abstract

Today, gender parity is a hot topic that raise number of debates and reforms. The cinema industry is not "Women films don't sell, they tell you" [Mery Streep].


Women have always been present in the cinema, but in what proportion? Every year, institutions publish reports whose aim is to show the evolution of the place of women in cinema and point out the inequalities that still exist.

The goal of this project is to have a better view of the place of women in the cinema industry. To answer this question we will rely mainly on Quotebank, which is a database containing quotes attributed to individuals, which are extracted from newspapers between 2008 and 2020. This project will focus on quotes from 2018 and will pave the way for future studies on other years.

### Research Questions

1. Who, in terms of gender, is talking about movies in the newspapers?

2. What are the characteristics of movies that impact their memorability over time? Does the gender have an influence on a movie's memorability ?

3. Is it possible to predict the genre and rating of a film by using Quotebank ?


### Proposed additional datasets

In addition to Quotebank, two other databases will be used for this project :

- Wikidata

A database that contains information about people (DOB, gender, etc.), movies (release date, crew, etc), and much more. In order to answer our research questions, we need to extract the gender and age of Quotebank's speakers and IMDb's people (crew and actors/actresses). We also need to extract movies release date. Data about Quotebank's speakers are already provided in the file speaker_attributes.parquet. The rest will be retrieved via the Wikidata API (i.e gender of actors/actresses).

source : https://www.wikidata.org/

- IMDb

The Internet Movie Database (IMDb) is an open source database that provides information related to movies, series, etc. This database is available online, separated in six datasets. These datasets are merged and treated in one single and personalized dataset. Columns were filtrated regarding of the needs of the research. Elements of interest that were kept are : movie title, released year, movie genres, crew (producer, cinematographer, writer), actors/actresses and ratings.  

source : https://www.imdb.com/interfaces/


### Method

À refaire

Four notebooks were created : one for pre-processing the datasets and one to answer each question. This allows us to better distribute the work within the team and reduce risks of conflict

#### Notebook_0: Preprocessing
In order to assess our questions, we need to select the relevant elements in each dataset to reduce their size and therefore the tasks computing time.
- For Quotebank : we decide to keep only the quotes presenting the keywords "movie", "cinema" and “film” in either the quote itself or the url of the articles.
- For Wikidata : for all the information about the Quotebank speakers, we used the provided structured data (parquet files) to extract speaker's gender and age. For the release date, actors and crew members of the films, we made a python script based on Wikidata API to collect those informations. We did so because in our opinion it was better than downloading and parsing the 100GB json dump.
- For IMDb : we filter out the types in order to keep only the movies' record (i.e filter out the 'series'). The dataset is then reduced to movies released in the year of 2018. The dataset is completed with the release date, the gender of the actors and crew members by using the Wikidata API.

#### Notebook_1: Question 1
For this question, we need to retrieve the gender of speakers. This is done with the wikidata parquets. Then, an analysis can be realized using aggregation, and then statistic tes and/or distribution.

#### Notebook_2: Question 2
For the second question, we need to find movies of interest in Quotebank. To do that, movie’s name in IMDb can serve as a keyword to extract quote related to movies in quotebank. Then, thanks to IMDb and Wikidata, we can add to those quotes the speaker’s, actor’s and producer’s gender, movie’s rating and release date of the movies. To reduce the gender to only one variable, we decides to attribute a score to each movie, and the score is simply the percentage of women involved. Finally, in order to investigate the movie’s memorability, we can aggregate quotes by film and look at the distribution of the quotes' date arround the release date. An analysis of memorability considering the features can now be done using statistic test between variables.

#### Notebook_3: Question 3
Finally, we wonder if it’s possible to predict movie’s genre and ratings regarding several features. We want to test if the memorability of a movie and the gender of actors, directors, producers and writers are predictive of the genre and the rating of a movie. To do so, we will train a model under a supervised learning method, using a logistic or linear regression.


### Proposed timeline and Organization within the team

Milestone 3 is due on 17 December and homework 2 is due on 26 November. For M3 we need to complete the project proposed in M2 and communicate our results with data story.

•	Until 26 November the data should be enriched and ready to analyse

- Benoit & Inès: cleaning QUOTEBANK plus adding gender and age
- Céline & Maud: cleaning IMDb plus adding gender and release date

•	26 November until 3 December the question 1 and 2 should be done

- Benoit: process data for question 1
- Céline: process data for question 2
- Maud and Inès: visualize data and create story for questions 1 and 2
- All team: start processing data for question 3

•	3 December until 10 December the question 3 should be done

- Group working together to response question 3
- One of the team member will focus on Jeckyll

	10 December until 17 December we will create the web site with our data story and complete README with members contributions and URL of the data story.

- Group create data story for question 3
- Maud finishes the README


### Questions for TAs

Crossing databases is going to pose a data size problem. We are thinking about reducing the data of interest to one or two particular years (e.g. 2018-2019 to be recent without taking into account Covid-related variables).

### Data story 
https://igag9.github.io/Site_web_ada/

