# ADA 2021
### Folder containing Code and Notebooks used to complete the project

1. Finir nos bases de données IMDb et Quotebank 
    
    Quotebank : 
      - rajouter les données de Wikidata (sexe pour chaque speeker)
      - filtrer par rapport aux mots-clés (en choississant une méthode pour le choix des mots-clé)
      - valeur 'None' pour speaker : on les supprime ?
      - si sexe ni homme ni femme : remplacer par 'other'
      - colonne pour dire de quel film ça parle


  IMDb : 
    - rajouter le sexe pour toutes les personnes (male/female/other)
    - checker si bien supprimé directeurs des acteurs
    - colonne date de sortie des films (API wikidata)
    - création de deux listes (peut-être après tuple) (sauvegardé en pickle) où figurent tous les noms de films et une autre liste pour le nom des crew/acteurs,      sauvegardé dans generated
    - rajouter une colonne par film 'gender_all' : pourcentage de femmes (0 : male, 1 : female) (comme un LR, et on s'affranchit des others)
    
    Wikidata : 
      - mettre 'other' dans sexe
      
2. Question 1

  Entrée : df1 qui contient 'quote', 'sexe', 'age'
  - describe, distribution, etc
  
3. Question 2

  - commet on définit la mémorabilité ? 
  - entrée : Quotebank avec 'date_citation', 'name_film', 'id_film'
  - supprimer les quote qui ne parle pas d'un film spécifique
  - entrée 2 : IMDb, 'gender_all', 'gender_director' (0 : male, 1 : female, on prend pas les other) (pourcentage de femmes), 'film_name', 'film_id', 'genre_film', 'ratings'
  - task : add column = 'memorability'
  - task : filtrer dans quotebank celles qui ne parle pas de film (NaN)
  - task : left merge quotebank et IMDb. Si mémorabilité dépend que de quotebank pas besoin de merger les deux.
  - sort by film_id : itere row (on peut alors faire des actions ligne par ligne sur des lignes qui parlent du même film) : appliquer la mémorabilité (selon méthode choisie). Stocker le résultat dans un nouvelle df: 'film_id', 'memorability'. Merge avec IMDb qu'on avait en entrée.
  - visualisation

4. Question 3

- entrée : Quotebank 'date_citation', 'citation', 'name_film', 'speaker', 'sexe_speaker', 'age', 'memorability' 
- task : filtrer quote qui ne parle pas de film
- task : ajouter column = 'score_positivity'
- split le model en train/test
 
