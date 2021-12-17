# "Cinema : is there a gender gap ?"


## Abstract


"She's learning where she fits on the food chain, and I'm not sure you want her to figure that out" [Owen Grady, Jurassic World]

In today's world, gender inequality is a phenomenon that is largely present and the cinema industry makes no exception to the rule. As inequalities have been largely highlighted by debates or studies during those previous years, a remaining question can be : what is the place of women in the cinema industry, as seen from the point of view of speakers in newspapers ?

The goal of this project is to answer this question. For that, it will rely mainly on Quotebank, a database containing quotes attributed to individuals, which are extracted from newspapers between 2008 and 2020.  This project will focus on quotes from 2018 and will pave the way for future studies on other years.


## Research Questions

1. What is the gender distribution of people talking about cinema in the newspapers?

2. Does the gender have an influence on a movie's memorability?

3. Is it possible to predict the rating of a movie by using Quotebank?


## Additional datasets
“Mommy’s Very Angry.” ['Ian Malcolm, Jurassic Park]

In addition to Quotebank, two other databases will be used for this project :

- Wikidata

A database that contains information about people (DOB, gender, etc.), movies (release date, crew, etc), and much more. In order to answer our research questions, we need to extract the gender and age of Quotebank's speakers and IMDb's people (crew and actors/actresses). We also need to extract movies release date. Data about Quotebank's speakers are already provided in the file speaker_attributes.parquet. The rest will be retrieved via the Wikidata.

source : https://www.wikidata.org/

- IMDb

The Internet Movie Database (IMDb) is an open source database that provides information related to movies, series, etc. This database is available online, separated in six datasets. These datasets are merged and treated in one single and personalized dataset. Columns were filtrated regarding of the needs of the research. Elements of interest that were kept are : movie title, released year, movie genres, crew (producer, cinematographer, writer), actors/actresses and ratings.  

source : https://www.imdb.com/interfaces/


## Method
“When You Gotta Go, You Gotta Go.” [Ian Malcolm, Jurassic Park]

Six notebooks were created : three for the pre-processing of each dataset and three to answer to each question. This allows us to better distribute the work within the team and reduce risks of conflict

#### Notebook_1: prepro_QUOTEBANK
We decide to keep only the quotes presenting the keywords "movie", "cinema" and “film” in either the quote itself or the url of the articles.
#### Notebook_1: prepro_WIKIDATA
For all the information about the Quotebank speakers, we used the provided structured data (parquet files) to extract speaker's gender and age. For the release date, actors and crew members of the films, we made a python script based on Wikidata API to collect those informations. We did so because in our opinion it was better than downloading and parsing the 100GB json dump.
#### Notebook_1: prepro_IMDb
We filter out the types in order to keep only the movies' record (i.e filter out the 'series'). The dataset is enriched with the gender of the actors and crew members by using the Wikipedia dataset.

#### Notebook_4: Question 1
For this question, we need to retrieve the gender of speakers. This is done with the wikidata parquets. Then, an analysis can be realized using aggregation, and then statistic tes and/or distribution.

#### Notebook_5: Question 2
For the second question, we need to find movies of interest in Quotebank. To do that, movie’s name in IMDb can serve as a keyword to extract quote related to movies in quotebank. Then, thanks to IMDb and Wikidata, we can add to those quotes the speaker’s, actor’s and producer’s gender, movie’s rating and release date of the movies. To reduce the gender to only one variable, we decides to attribute a score to each movie, and the score is simply the percentage of women involved. Finally, in order to investigate the movie’s memorability, we can aggregate quotes by film and look at the distribution of the quotes' date arround the release date. An analysis of memorability considering the features can now be done using statistic test between variables.

#### Notebook_6: Question 3
Finally, we wonder if it’s possible to predict movie’s ratings regarding several features. We want to test if the memorability of a movie and the gender of actors, directors, producers and writers are predictive of the genre and the rating of a movie. To do so, we will train a model under a supervised learning method, using a logistic or linear regression.


### Contribution of team members
Céline: IMDb expert
Inès: Wonderfull website designer
Maud: Astonishing vizualisation maker
Benoît: Wikidata parser and head debugger



"Garbage in, gargabe out" [Robert West]
