from SPARQLWrapper import SPARQLWrapper, JSON
import queries


def get_query_results():
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)

    query = queries.getCountries

    sparql.setQuery(query)  # the previous query as a literal string

    return sparql.query().convert()


if __name__ == '__main__':
    result = get_query_results()
    for m in result:
        print(m.film_title)
