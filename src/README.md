# ADA 2021
### Folder containing Code and Notebooks used to complete the project

1. Finir nos bases de données IMDb et Quotebank 

    Wikidata : (les fichiers fournis par les assistants)
      - mettre 'other' dans sexe. On avait déjà mis male female mais il faut mettre other pour le reste
    
    Quotebank : 
      - rajouter les données de Wikidata depuis le fichier wikidata : sexe pour chaque speeker
      - filtrer par rapport aux mots-clés (en choississant une méthode pour le choix des mots-clé) --> enelver tout ceux qui parlent pas de notre thème. On peut ajouter une colonne 'relevant' avec 0 pour faux et 1 pour True et après on filtre pour enregistrer dans un nouveau fichier
      - valeur 'None' pour speaker : on les supprime ?
      - si sexe ni homme ni femme : remplacer par 'other' --> normalement ça sera déjà le cas dans le fichier Wikidata, mais juste faire un values_count() pour vérifier
      - colonne pour dire de quel film ça parle --> recherche par mots-clés (comme vu en cours / lab) et on met dans une colonne de quel film ça parle (le nom du film)


    IMDb : 
    - rajouter le sexe pour toutes les personnes (male/female/other) --> time.sleep pour pas DDOS, avec l'API Wikidata, mais si ça marche pas on peut faire avec le fichier de 100 Go
    - checker si bien supprimé directeurs des acteurs --> Céline sait de quoi ça parle
    - colonne date de sortie des films (API wikidata) --> time.sleep pour pas DDOS
    - création de deux listes (peut-être après tuple) (sauvegardé en pickle) ~~où figurent tous les noms de films~~ et une autre liste pour le nom des crew/acteurs,      sauvegardé dans generated --> ça sera utile pour après, genre recherche par mots clés
    - rajouter une colonne par film 'gender_all' : pourcentage de femmes (0 : male, 1 : female) (comme un LR, et on s'affranchit des others)
    - rajouter une colonne gender_director avec % de femme dans director
    - rajouter une colonne gender_crew avec % de femme dans crew
    - rajouter une colonne gender_actor avec % de femmes dans actors --> si possible une seule cellule qui fait les 4 ci-dessus pour pas itérer 'x dessus
    
      
2. Question 1

      - Entrée : df1 qui contient 'quote', 'sexe', 'age', déjà filtré avec les quotes relevant
      - Sanitariser : les virgules posent probleme pour lexicon
      - Explo des données
      - Visualisation, distribution, etc --> production de résultats et interprétation / data story
  
3. Question 2

      - commet on définit la mémorabilité ? --> très important de bien le définir
      - entrée : Quotebank avec 'date_citation', 'name_film', 'id_film'
      - supprimer les quote qui ne parle pas d'un film spécifique --> donc celles qui parlent de cinéma mais pas d'un film spécifique


      - entrée 2 : IMDb, 'gender_all', 'gender_directors' (0 : male, 1 : female, on prend pas les other) (pourcentage de femmes), 'film_name', 'film_id', 'genre_film', 'ratings' et potentiellement d'autres colonnes de pourcentage de genre
      - task : left merge quotebank et IMDb. Si mémorabilité dépend que de quotebank pas besoin de merger les deux.
      - sort by film_id : itere row (on peut alors faire des actions ligne par ligne sur des lignes qui parlent du même film) : appliquer la mémorabilité (selon méthode choisie). Stocker le résultat dans un nouvelle df: 'film_id', 'memorability'. Merge avec IMDb qu'on avait en entrée.
      - task (la mê) : add column sur le df = 'memorability' --> iterrow (ou autre si on arrive pas à charger le df en mémoire) et on applique le calcul de memorability pour chaque ligne
      - taskme mais expliqué différemment : add column sur le df = 'memorability' --> iterrow (ou autre si on arrive pas à charger le df en mémoire) et on applique le calcul de memorability pour chaque ligne
      - visualisation et data story

4. Question 3

    - entrée : Quotebank 'date_citation', 'citation', 'name_film', 'speaker', 'sexe_speaker', 'age', 'memorability' et autre features si on a besoin
    - task : filtrer quote qui ne parle pas de film
    - task : ajouter column = 'score_positivity'
    - groupy film
    - ajouter le ratings du film
    - split le model en train/test
    - train un model pour prédire le rating, plusieurs fois, avec plusieurs façon de groupby, plusieurs features, et prendre le meilleur
    - visu et data story
 
