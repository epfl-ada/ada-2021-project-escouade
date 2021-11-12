from functool import lru_cache
from qwikidata.sparql import return_sparql_query_results


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


@lru_cache(maxsize=10000)
def get_person_gender(IMDb_ID):
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
} ORDER BY ASC (?date)
""" % IMDb_ID
    results = return_sparql_query_results(query_string)
    return results['results']['bindings']


def get_film_release_date(IMDb_ID):
    result = get_film_info(IMDb_ID)[0]
    date = result['date']['value']
    return date


if __name__ == '__main__':
    get_person_info("nm0000901")
    get_person_gender("nm0000901")
