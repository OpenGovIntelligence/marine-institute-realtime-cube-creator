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
from d_cubiQLAPI.cubiqlAPI import cubiqlAPI
from e_DRUIDStoreAPI.DRUIDStore import DRUID

# pipeline_components/b_table2qbAPI/table2qb_wrapper/table2qb_preprocessor

from util.config import assets, ds_names, druidServer

global marineapi
marineapi = MarineDataPortalApi()

global t2qbapi
t2qbapi = table2qbWrapper()

global rdfstoreapi
rdfstoreapi = RDFStoreAPI()

global cubiqlapi
cubiqlapi = cubiqlAPI()

global druid
druid = DRUID()



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

    # D - get created cubes in json with structure ready for pushing to DRUID
    retrieved_json_cubes_path_info = {}

    for ds in ds_names:
        """ use cubiql api fucntion to retrieve and store json cubes """
        retrieved_json_cubes_path_info[ds] = ''
    # E - push retrieved json cubes to DRUID server

    for ds in ds_names:

        ### using pycurl
        druid.push_observations_to_druid_BATCH(druidServer=druidServer,
                                               schemaFile='druid_schemas/schema_'+ds+'.json',
                                               #observations_file_path='/home/mohade/ogitesting/druid/druid-0.10.1/datasets/ogi-sample-datasets/for_druid/marine/IWBNetwork/IWBNetwork.json',
                                               observations_file_path=retrieved_json_cubes_path_info[ds],
                                               method='pycurl')


job("is started")

"""scheduling
schedule.every().day.at("01:00").do(job,'It is 01:00 time to start harvesting MI data!')

while True:
    schedule.run_pending()
    time.sleep(01) # wait one minute
    print datetime.datetime.now().isoformat()
"""
