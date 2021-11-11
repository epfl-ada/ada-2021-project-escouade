import requests


def get_person_info(name):
    params = dict (
        action='wbsearchentities',
        format='json',
        language='en',
        uselang='en',
        type='article',
        search='country'
        )
    response = requests.get('https://www.wikidata.org/w/api.php?', params).json()
    print(response.get('search')[0]['id'])
    
    
if __name__ == '__main__':
    get_person_info("Elon Musk")
    
    
    
    # Human = Q5
    # Instace of = P31
    # ?item wdt:P31 wd:Q5 --> select human
    # native name = P1559
    # Family name = P734
    # given name = P735
    # IMDb ID = P345
    # wdt:P7 "value1"
    
    
    """
    SELECT ?item ?name ?nameLabel ?genderLabel ?placeofbirth ?nationality (year(?birthdate) as ?birthyear) (year(?deathdate) as ?deathyear)
WHERE
{
  ?item wdt:P31 {IMDb_id}
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
}
}"""