query1 = "select (count(?l) as ?data_count) ?state_name "\
"FROM NAMED <http://localhost:3030/SemanticProject/data/food>"\
"WHERE "\
"{"\
"    GRAPH <http://localhost:3030/SemanticProject/data/food>"\
    "{"\
    "?l <https://github.com/timrdf/csv2rdf4lod-automation/wiki/CSV2RDF4LOD_BASE_URI#/source/Users/dataset/AshishMAC/vocab/enhancement/1/state> ?state_name."\
    "}"\
"} group by (?state_name)"


query2= "select (count(?f) as ?data_count) ?state_name "\
"FROM NAMED <http://localhost:3030/SemanticProject/data/health>"\
"WHERE"\
"{"\
    "GRAPH <http://localhost:3030/SemanticProject/data/health>"\
    "{ "\
    "?f <https://chronicdata.cdc.gov/resource/_4ny5-qn3w/locationdesc> ?state_name"\
". "\
    "}"\
"} group by (?state_name)"


query3 = "select (count(?k) as ?data_count) ?state_name "\
"FROM NAMED <http://localhost:3030/SemanticProject/data/claims>"\
"WHERE"\
"{"\
    "GRAPH <http://localhost:3030/SemanticProject/data/claims>"\
    "{"\
" ?k <https://chronicdata.cdc.gov/resource/iw6q-r3ja/locationdesc> ?state_name."\
"}"\
"} group by (?state_name)"

query4 = "select ?data_count ?state_name "\
"FROM NAMED <http://localhost:3030/SemanticProject/data/population>"\
"WHERE "\
"{"\
    "GRAPH <http://localhost:3030/SemanticProject/data/population>"\
 "{"\
    '?s <https://github.com/timrdf/csv2rdf4lod-automation/wiki/CSV2RDF4LOD_BASE_URI#/source/Users/dataset/AshishMAC/vocab/raw/state_code> ?state_name FILTER(?state_name != "USA").'\
    "?s <https://github.com/timrdf/csv2rdf4lod-automation/wiki/CSV2RDF4LOD_BASE_URI#/source/Users/dataset/AshishMAC/vocab/raw/population_est18plus2016> ?data_count "\
"}"\
"}"


query5 = "select (count(?l) as ?restaurent_count) (sample(?18plus_pop) as ?18_plus_pop) ?state "\
"FROM NAMED <http://localhost:3030/SemanticProject/data/food>"\
"FROM NAMED <http://localhost:3030/SemanticProject/data/population>"\
"WHERE  "\
"{"\
    "GRAPH <http://localhost:3030/SemanticProject/data/food> "\
   " {"\
     "   ?l <https://github.com/timrdf/csv2rdf4lod-automation/wiki/CSV2RDF4LOD_BASE_URI#/source/Users/dataset/AshishMAC/vocab/enhancement/1/state> ?state."\
    "}"\
    "GRAPH <http://localhost:3030/SemanticProject/data/population> "\
    "{"\
   '     ?s <https://github.com/timrdf/csv2rdf4lod-automation/wiki/CSV2RDF4LOD_BASE_URI#/source/Users/dataset/AshishMAC/vocab/raw/state_code> ?state FILTER(?state != "USA").'\
  "      ?s <https://github.com/timrdf/csv2rdf4lod-automation/wiki/CSV2RDF4LOD_BASE_URI#/source/Users/dataset/AshishMAC/vocab/raw/population_est18plus2016> ?18plus_pop. "\
 "   }"\
"} group by (?state) "