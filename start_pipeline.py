# add outer modules
import sys

# sys.path.insert(0, '/home/mohade/workspace/marine-institute-realtime-cube-creator/shared')
sys.path.append('/home/mohade/workspace/marine-institute-realtime-cube-creator/shared')
sys.path.append('/home/mohade/workspace/marine-institute-realtime-cube-creator/pipeline_components')

# lib
import copy
import datetime
import urllib
from datetime import timedelta

# my classes
from a_marineDataAPI.marineAPI import MarineDataPortalApi
from b_table2qbAPI.table2qb_wrapper.table2qb_preprocessor.table2qb_Wrapper import table2qbWrapper
from c_rdfDataStoreAPI.RDFStore import RDFStoreAPI

# pipeline_components/b_table2qbAPI/table2qb_wrapper/table2qb_preprocessor

from util.config import assets, ds_names

global marineapi
marineapi = MarineDataPortalApi()

global t2qbapi
t2qbapi = table2qbWrapper()

global rdfstoreapi
rdfstoreapi = RDFStoreAPI()

global baseuri
baseuri = 'http://www.opengovintelligence.eu/statistics/marine-institute/'


def job(t):

    #@TODO 0 - check last run time [saved in json from marine api download part] and see if we should run again or not

    print "MARINE NEAR REAL TIME RDFDATACUBE BUIDLING AND PUBLISHING PIPE ...", t

    # a - harvest csv row data
    observations_files_locations_list = marineapi.start_harvesting()
    print observations_files_locations_list

    # b - build cubes of harvested data
    created_triples_path_info = {}
    temp_obj = {}
    created_triples_path_info_by_ds = []
    created_triples_path_info_no_ds = []

    for obs_csv in observations_files_locations_list:
        print obs_csv
        # 1 - create code lists
        """it needs headers of csv ####"""
        print 'CODELIST PIPELINE --------------------OF -   ---' + str(obs_csv)
        created_triples_path_info['codelists_path'] = t2qbapi.run_table2qb_pipes(pipelineName='codelist-pipeline',
                                                                                 datasetname=obs_csv['ds'],
                                                                                 baseURI=baseuri,
                                                                                 slug=str(obs_csv['ds']).lower(),
                                                                                 input_components=str(assets[obs_csv[
                                                                                     'ds']]) + '/components.csv',
                                                                                 input_observations=str(
                                                                                     obs_csv['folderName']) + str(
                                                                                     obs_csv['fileName']),
                                                                                 input_columns=str(assets[obs_csv[
                                                                                     'ds']]) + '/columns.csv')
        # 2 - cube schema or comonents
        print 'COMPONENTS PIPELINE ---------------------OF -   ---' + str(obs_csv)
        created_triples_path_info['components_path'] = t2qbapi.run_table2qb_pipes(pipelineName='components-pipeline',
                                                                                  datasetname=obs_csv['ds'],
                                                                                  baseURI=baseuri,
                                                                                  slug=str(obs_csv['ds']).lower(),
                                                                                  input_components=str(assets[obs_csv[
                                                                                      'ds']]) + '/components.csv',
                                                                                  input_observations=str(
                                                                                      obs_csv['folderName']) + str(
                                                                                      obs_csv['fileName']),
                                                                                  input_columns=str(assets[obs_csv[
                                                                                      'ds']]) + '/columns.csv')
        # 3-4- create cubes [with single row measues inside]
        print 'CUBE PIPELINE ----------------------OF -   --- ' + str(obs_csv)
        created_triples_path_info['cube_path'] = t2qbapi.run_table2qb_pipes(pipelineName='cube-pipeline',
                                                                            datasetname=obs_csv['ds'], baseURI=baseuri,
                                                                            slug=str(obs_csv['ds']).lower(),
                                                                            input_components=str(assets[obs_csv[
                                                                                'ds']]) + '/components.csv',
                                                                            input_observations=str(
                                                                                obs_csv['folderName']) + str(
                                                                                obs_csv['fileName']),
                                                                            input_columns=str(
                                                                                assets[obs_csv['ds']]) + '/columns.csv')

        temp_obj[str(obs_csv['ds'])] = created_triples_path_info
        created_triples_path_info_no_ds.append(copy.deepcopy(created_triples_path_info))
        created_triples_path_info_by_ds.append(copy.deepcopy(temp_obj))

        created_triples_path_info.clear()
        temp_obj.clear()

    print created_triples_path_info_by_ds


    # C - push cubes- components - codelists to rdf store
    for ds in created_triples_path_info_no_ds:
        # print ds[0]
        #1 - push components
        rdfstoreapi.push_curl(ds['components_path'])
        #2 - push codelist
        rdfstoreapi.push_curl(ds['codelists_path'])
        #3 - push cubes - loop on partitions
        for part in ds['cube_path']:
            rdfstoreapi.push_curl(part)

    # D - push cubes- components - codelists to rdf store




#
# """screen scheduled_tasks.py"""
# def ds_tasks(api, time_from):
#
#     temp_csv_data =  ds_api.get_csv(api, time_from, "jjj")
#     print temp_csv_data
#
#
#
#     ds_api.put_csv_to_file(temp_csv_data, file_name=api+"_"+decode(time_from).replace(" ","_"))
#     ds_api.transform_to_rdfcube(api, csv_file_path="/ogi-publishing-pipeline-realtime/MI_ds1_data/", csv_file_name=api+"_"+decode(time_from).replace(" ","_")+".csv", qbpath="/ogi-publishing-pipeline-realtime/MI_ds1_data/", qbname=api+"_"+decode(time_from).replace(" ","_")+".ttl")
#     #ds_api.push_to_rdf_datastore()
#     print "done "+ api + "! file:"+ api+"_"+decode(time_from)
#     return
#
# def prepare_time_from():
#
#     time_from = "time%3E=2017-06-07T00%3A00%3A00Z"
#
#     # print encode(time_from)
#
#     # print decode(time_from)
#
#     print time_from
#     print datetime.datetime.now().replace(microsecond=0).isoformat()
#     print encode(datetime.datetime.now().replace(microsecond=0).isoformat())
#
#     yesterday = datetime.datetime.now() - timedelta(days=1)
#     yesterday.strftime('%m%d%y')
#
#     print yesterday
#
#     print encode(yesterday.replace(microsecond=0).isoformat())
#
#     time_from = encode(yesterday.replace(microsecond=0).isoformat())
#
#     return time_from
#
# def encode(URL):
#     URI_encoded = urllib.quote_plus(URL)
#     #   print URI_encoded
#     return URI_encoded
#
#
# def decode(URL):
#     URI_decoded = urllib.unquote(URL)
#     #   print URI_encoded
#     return URI_decoded
#

job("is started")

"""scheduling
schedule.every().day.at("01:00").do(job,'It is 01:00 time to start harvesting MI data!')

while True:
    schedule.run_pending()
    time.sleep(01) # wait one minute
    print datetime.datetime.now().isoformat()
"""
