# add outer modules
import sys

# sys.path.insert(0, '/home/mohade/workspace/marine-institute-realtime-cube-creator/shared')
sys.path.append(
    '/home/mohade/workspace/marine-institute-realtime-cube-creator/pipeline_components/b_table2qbAPI/table2qb_wrapper/table2qb-preprocessor')

from table2qb_preprocessor.table2qb_Wrapper import Table2qbAPI

class Table2qbAPI(object):

    def __init__(self):
        self.table2qb = Table2qbAPI()

        self.pipeline = ''
        self.slug = ''
        self.datasetname = ''
        self.baseURI = ''

        self._input_components = ''
        self._input_observations = ''
        self._input_columns = ''

    def start_conversion(self, obs_file_path):
        print 'starting rdf cube building!'

        # get csv observation files

        # get componnets csv files

        #get columns csv files


