from SPARQLWrapper import SPARQLWrapper, JSON
import queries


def get_query_results(queryname):
    sparql = SPARQLWrapper(
        "https://semantic.localtunnel.me/SemanticProject/sparql")
    sparql.setReturnFormat(JSON)

    query = getattr(queries, queryname)

    sparql.setQuery(query)

    return sparql.query().convert()


if __name__ == '__main__':
    result = get_query_results()
    for m in result:
        print(m.film_title)
