getCountries = "PREFIX dbpedia-ont-PP: <http://dbpedia.org/ontology/PopulatedPlace/>"\
"PREFIX  dbpedia-owl:  <http://dbpedia.org/ontology/>"\
"SELECT DISTINCT ?country ?populationDensity"\
"WHERE {"\
    "?country a dbpedia-owl:Country ."\
    "?country dbpedia-ont-PP:populationDensity ?populationDensity . "\
"}"\
"LIMIT 5"