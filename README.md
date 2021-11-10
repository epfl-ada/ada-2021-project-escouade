# How big is the impact of public opinion on the film industry?
## Milestone 2



### Abstract 

For feminist film studies, some of the most recent ground-breaking work has been on recovering women’s film history. Another study released in 2018 about women on-screen shows that female speaking characters in the top 100 movies accounted for just 31.8 percent of all roles. We wonder why the representation of women has not changed (or a little) for the 10 past years, and if it is due to the opinion people have on this representation. The aim of the project is to understand how public opinion impacts the film industry, by automatically analyzing quotations about movies in social and traditional media. The first part of the project deals with the analysis of the relation between public opinion and the general reception a film receives, focusing on gender issues. In the second part, public opinion will be used to predict the different characteristics of a film.


### Research Questions
1. How does the memorability of a movie evolve regarding his characteristics (gender of producer, gender of actors, genre of movies, ratings, etc.) ? 

2. Who are the people talking about cinema, regarding gender and age ?

3. Using Quotebank to define how much about a movie is told (even without seeing it)
    - predict genre
    - predict ratings/reception

### Proposed additional datasets (if any)
List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.

In addition to Quotebank, which allows the automatic analysis of content in social and traditional media, two other databases will be used for this project :

- Wikidata 

A database that provides additional attributes about people of interest. In order to answer our research questions, we need to extract the gender of different protagonists (speakers, producers, actors), as such as the speaker's professional environment and their age. Additional metadata about speakers in the Quotebank dataset are already provided in a file named speaker_attributes.parquet. This file will be enriched with attributes of other protagonists, that will be extract wih a python3 code.

- IMDb 

IMDb is a free database that provides a lot of information about movies. This database is available online. Ratings and genre of movies are needed for the project. 


### Methods
Before response to these questions we need to select relevant elements for each dataset. For Quotebank dataset, we decide to use the keyword "movies" and "cinema" to extract quotes of interest. Moreover, we also use the category "movies" on the URLs. For Wikidata, we need to extract characteristics of quote's author and movie's actor and producer. The variables of interest are gender, age and professional field. Finally, for IMDB dataset, we need movie's ratings, movie's actor and producer.
In order to response to this question some tools need to be use.

First, for question one, we need to find movies of interest in quotbank. To do that, movie’s name in IMDb can serve as a keyword to extract quote related to movie. Then, thanks to IMDb and wikidata, we can add, for each movie selected, speaker’s, actor’s and producer’s gender and movie’s rating. Finally, in order to see the evolution of the movie’s memorability, a timeline of the quotes can be done. An analysis of memorability considering the features can now be done using statistic test between variables. 

For the second question, about who taking about cinema, we need to attribute gender and age to the speaker. This information can be reach by research quote’s speaker’s gender and age in wikidata.  Then, an analysis of these variable can be realized using statistic test, distribution, and regression. 

And finally, we wonder if it’s possible to predict movie’s genre and ratings regarding the memorability. To do so, a logistic or linear regression can be used to determine if genre and rating are predictor or not. 


### Proposed timeline and Organization within the team

Milestone 3 is due to 17 December and homework 2 is due to 26 November. So, we have 3 weeks for finishing M3. For M3 we need to execute the project proposed in M2 and communicate our result with data story.  
•	26 November until 3 December the question 1 and 2 should be done
    - Benoit: extract quote related to movie
    - Céline: add gender of person of interest in the dataset (wikidata and IMDB)
    - Maud and Inès: do the analyzes to answer the question 1 and 2 

•	3 December until 10 December the question 3 should be done and start to learn how Jekyll works.
    - Groups working together to response question 3 
    - One of the team will focus on Jeckyll

•	10 December until 17 December we will create the web site with our data story and complete README with members contributions and URL of the data story. 
    - Benoit create data story for question 1
    - Céline create data story for question 2
    - Inès create data story for question 3
    - Maud finishes the README
    


### Questions for TAs (optional)
Add here any questions you have for us related to the proposed project.
