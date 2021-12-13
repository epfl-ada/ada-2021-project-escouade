from datetime import datetime
from json import JSONDecodeError
from time import sleep
from numpy import random
from qwikidata.sparql import return_sparql_query_results

sleeptime = random.uniform(1,10)

def get_person_info(IMDb_ID):
    query_string = """
SELECT
  ?item ?itemLabel
  ?value
  ?genderLabel
  ?birthdate ?deathdate
WHERE
{
  VALUES ?value {"%s"}
  ?item wdt:P345 ?value .
  ?item wdt:P31 wd:Q5 ;
  wdt:P21 ?gender;
  wdt:P569 ?birthdate;
  OPTIONAL {?item wdt:P570 ?deathdate}
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
LIMIT 10
""" % IMDb_ID
    results = return_sparql_query_results(query_string)
    return results['results']['bindings']


#@cache
def get_person_gender(IMDb_ID):
    sleep(sleeptime)
    result = get_person_info(IMDb_ID)[0]
    gender = result['genderLabel']['value']
    return gender


def get_film_info(IMDb_ID):
    query_string = """
SELECT DISTINCT ?film ?date ?placeLabel ?filmLabel WHERE {
  VALUES ?value {"%s"}
  ?film wdt:P345 ?value.
  ?film p:P577 ?release_statement.
  ?release_statement (psv:P577/wikibase:timePrecision) 11 ;
    ps:P577 ?date.
    ?release_statement pq:P291 ?place.
  ?release_statement pq:P291 wd:Q30.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
} ORDER BY ASC (?date) LIMIT 1
""" % IMDb_ID
    results = return_sparql_query_results(query_string)
    if results :
        return results['results']['bindings']
    else:
        print("Warning")

def get_film_release_date(IMDb_ID):
    #sleep(sleeptime)
    try:
        result = get_film_info(IMDb_ID)
    except JSONDecodeError:
        result = None

    if result:
        date = result[0]['date']['value']
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
        date = datetime.strftime(date, '%d.%m.%Y')
        return date

if __name__ == '__main__':
    #get_person_gender("nm0000901")
    print(get_film_release_date("tt0816692"))


