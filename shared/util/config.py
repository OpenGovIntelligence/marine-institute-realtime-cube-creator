
import os

#logging

log_dir = os.path.abspath( os.path.join(os.path.dirname(__file__),os.pardir,'logs'))
log_file=log_dir+"/service.log"
log_name="ogi-realtime-service"


#cube builder API
cubeBuilderAPI = "********:4567/cubeBuilderAPI/cubeBuilderArgs?"


druidServer = 'vmogi01.deri.ie:8090/druid/indexer/v1/task'

#dataSets/inputsSchemas names turtle-stored
ds_names = {}
ds_names['IWBNetwork'] = "IWBNetwork"
ds_names['IrishNationalTideGaugeNetwork'] = "IrishNationalTideGaugeNetwork"
ds_names['IWaveBNetwork_spectral'] = "IWaveBNetwork_spectral"
ds_names['IWaveBNetwork_zerocrossing'] = "IWaveBNetwork_zerocrossing"

#assets for table2qb
# /home/mohade/workspace/marine-institute-realtime-cube-creator/pipeline_components/b_table2qbAPI
assets = {}
assets['IWBNetwork'] = '/home/mohade/workspace/marine-institute-realtime-cube-creator/pipeline_components/b_table2qbAPI/Marine_Institute_table2qbwrapper_data/IWBNetwork'
assets['IrishNationalTideGaugeNetwork'] = '/home/mohade/workspace/marine-institute-realtime-cube-creator/pipeline_components/b_table2qbAPI/Marine_Institute_table2qbwrapper_data/IrishNationalTideGaugeNetwork'
assets['IWaveBNetwork_spectral'] = '/home/mohade/workspace/marine-institute-realtime-cube-creator/pipeline_components/b_table2qbAPI/Marine_Institute_table2qbwrapper_data/IWaveBNetwork_spectral'
assets['IWaveBNetwork_zerocrossing'] = '/home/mohade/workspace/marine-institute-realtime-cube-creator/pipeline_components/b_table2qbAPI/Marine_Institute_table2qbwrapper_data/IWaveBNetwork_zerocrossing'


outputsCSV_dir =os.path.abspath( os.path.join(os.path.dirname(__file__),os.pardir,'MI_polrtal_downloaded_CSVs'))
outputsCSV_dir_for_builder = "/ogi-publishing-pipeline-realtime/outputsCSV"
inputsSchemas_dir = "/ogi-publishing-pipeline-realtime/inputsSchemas"
    #os.path.abspath( os.path.join(os.path.dirname(__file__),os.pardir,'inputsSchemas'))
outputsCubes_dir = "/ogi-publishing-pipeline-realtime/outputsCubes"
    #os.path.abspath( os.path.join(os.path.dirname(__file__),os.pardir,'outputsCubes'))

skip_units_row = True

endpoint_rdf_store_url = "http://vmogi01.deri.ie:8000/sparql"
endpoint_rdf_store_url_crud = "http://vmogi01.deri.ie:8000/sparql-graph-crud-auth"
endpoint_user_name = "dba"
endpoint_password = "deriegovvirtuoso"
testing_graph_name = "graph=http://localhost:8890/DAV"

prefixes = """
PREFIX dccs:  <http://data.gmdsp.org.uk/data/example/stats/dccs/>  \n
PREFIX owl:  <http://www.w3.org/2002/07/owl#>  \n
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#> \n
PREFIX skos:  <http://www.w3.org/2004/02/skos/core#>  \n
PREFIX rdfs:  <http://www.w3.org/2000/01/rdf-schema#>  \n
PREFIX ds:  <http://data.gmdsp.org.uk/data/example/stats/dataset/>  \n
PREFIX ogi:  <http://www.opengovintelligence.eu/pilots#>  \n
PREFIX qb:  <http://purl.org/linked-data/cube#>  \n
PREFIX dct:  <http://purl.org/dc/terms/>  \n
PREFIX prop:  <http://data.gmdsp.org.uk/data/example/stats/prop/>  \n
PREFIX sdmx-concept:  <http://purl.org/linked-data/sdmx/2009/concept#>  \n
PREFIX scovo:  <http://purl.org/NET/scovo#>  \n
PREFIX sdmx-attribute:  <http://purl.org/linked-data/sdmx/2009/attribute#>  \n
PREFIX prov:  <http://www.w3.org/ns/prov#>  \n
PREFIX admingeo:  <http://data.ordnancesurvey.co.uk/ontology/admingeo/> \n
PREFIX sdmx-dimension:  <http://purl.org/linked-data/sdmx/2009/dimension#>  \n
PREFIX sdmx-subject:  <http://purl.org/linked-data/sdmx/2009/subject#>  \n
PREFIX sdmx-metadata:  <http://purl.org/linked-data/sdmx/2009/metadata#>  \n
PREFIX void:  <http://rdfs.org/ns/void#>  \n
PREFIX dbpedia-owl:  <http://dbpedia.org/ontology/>  \n
PREFIX org:  <http://www.w3.org/ns/org#>  \n
PREFIX sdmx-measure:  <http://purl.org/linked-data/sdmx/2009/measure#>  \n
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  \n
PREFIX sdmx-code:  <http://purl.org/linked-data/sdmx/2009/code#>  \n
PREFIX interval:  <http://reference.data.gov.uk/def/intervals/>  \n
"""