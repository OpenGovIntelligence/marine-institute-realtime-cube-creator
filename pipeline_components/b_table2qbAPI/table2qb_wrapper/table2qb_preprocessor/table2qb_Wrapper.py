from __future__ import division  # a/b is float division
import subprocess
import pandas as pd
import datetime
import os
import sys
import copy
import csv
from math import ceil
import math


class table2qbWrapper(object):

    def __init__(self):
        self._executable = "table2qb.jar"
        self.pipelineName = 'components-pipeline'
        self._input_components = "components.csv"
        self._input_observations = "observations.csv"
        self._input_columns = 'columns.csv'
        self._output_files_list = []
        self.codeListHeaders = ['Label', 'Notation', 'Parent Notation']
        self.observationFileHeaders = ['Measure Type', 'value']

        self.unique_folder_for_each_run = 'data/'
        self.dimensions_list = []
        self.measures_list = []
        self.slugized_list = []
        self.datasetname = 'myDs'
        self.baseURI = 'http://example.com/dataset/'
        self.slug = 'test'
        self.files_count = 1

        # mesaage for holding created folders paths
        self.created_triples_path_info = {}

    # used here as module not as cmd tool
    def run_full_table2qb_pipes(self, pipelineName, datasetname, baseURI, slug, input_components, input_observations,
                                input_columns):

        # self.pipelineName = sys.argv[1]
        # self.datasetname = sys.argv[2]
        # self.baseURI = sys.argv[3]
        # self.slug = sys.argv[4]
        # self._input_components = sys.argv[5]
        # self._input_observations = sys.argv[6]
        # self._input_columns = sys.argv[7]
        # used here as module not as cmd tool
        self.pipelineName = pipelineName
        self.datasetname = datasetname
        self.baseURI = baseURI
        self.slug = slug
        self._input_components = input_components
        self._input_observations = input_observations
        self._input_columns = input_columns
        # create unique folder to hold outputs
        self.unique_folder_for_each_run = self.generate_folder_name()

        #mesaage for holding created folders paths
        # self.created_triples_path_info = {}

        # execute cube creation pipeline
        subprocess.call(["java", "-jar", self._executable, 'list'])

        if self.pipelineName == 'components-pipeline':
            # components pipeline
            subprocess.call(["java", "-jar", self._executable, 'describe', 'components-pipeline'])
            components_outputfile = self.unique_folder_for_each_run + 'components__' + self.datasetname + '.ttl'
            # print  self._input_components
            subprocess.call(
                ["java", "-jar", self._executable, 'exec', 'components-pipeline', '--input-csv', self._input_components,
                 '--base-uri', self.baseURI,
                 '--output-file', components_outputfile])

            # self.created_triples_path_info['components_path'] = components_ouptfile
            # return self.created_triples_path_info
            return components_outputfile

        if self.pipelineName == 'cube-pipeline':

            # generate single measure per row observation file
            ready_input_file = self.generate_single_row_observations()

            # cube pipeline
            subprocess.call(["java", "-jar", self._executable, 'describe', 'cube-pipeline'])
            cube_ouptfile = self.unique_folder_for_each_run + 'cube_' + self.datasetname
            cube_ouptfiles = []
            for i in range(0, self.files_count):
                subprocess.call(
                    ["java", "-jar", self._executable, 'exec', 'cube-pipeline', '--input-csv',
                     ready_input_file + '_p' + str(i),
                     '--dataset-name', self.datasetname, '--dataset-slug', self.slug, '--column-config',
                     self._input_columns,
                     '--base-uri', self.baseURI, '--output-file', cube_ouptfile + '_p' + str(i) + '.ttl'])
                cube_ouptfiles.append(cube_ouptfile+ '_p' + str(i) + '.ttl')

            #self.created_triples_path_info['cube_path'] = cube_ouptfile
            #return self.created_triples_path_info
            return cube_ouptfiles

        if self.pipelineName == 'codelist-pipeline':

            # generate code lists
            self.generate_code_lists()

            # code list pipeline
            subprocess.call(["java", "-jar", self._executable, 'describe', 'codelist-pipeline'])
            for dim in self.dimensions_list:
                code_list_input = self.unique_folder_for_each_run + dim + '.csv'
                code_list_ouptfile = self.unique_folder_for_each_run + dim + '__codeList__' + self.datasetname + '.ttl'
                subprocess.call(
                    ["java", "-jar", self._executable, 'exec', 'codelist-pipeline', '--codelist-csv', code_list_input
                        , '--codelist-name', dim, '--codelist-slug', dim,
                     '--base-uri',
                     self.baseURI,
                     '--output-file', code_list_ouptfile])

            # self.created_triples_path_info['codelist_path'] = code_list_ouptfile
            # return self.created_triples_path_info
            return code_list_ouptfile


    #renaming fuction and keeping old name as well
    run_table2qb_pipes = run_full_table2qb_pipes

    def generate_code_lists(self):

        # get dimesions names list
        components_df = pd.read_csv(self._input_components)
        dimensions_df = components_df[(components_df['Component Type'] == 'Dimension')]
        self.dimensions_list = dimensions_df['Label'].tolist()

        # get slugized values
        columns_df = pd.read_csv(self._input_columns)
        slugized_df = columns_df[(columns_df['value_transformation'] == 'slugize')]
        self.slugized_list = slugized_df['title'].tolist()

        # get observation/dimensions values
        observations_df = pd.read_csv(self._input_observations)

        # do the generation thingy
        for dimension in self.dimensions_list:
            # create final code list data frame
            dimCodeList_df = pd.DataFrame(columns=self.codeListHeaders)
            # get dim values
            dim_values_list = observations_df[dimension].tolist()
            # get unique values of dim
            unique_dime_vals_list = list(set(dim_values_list))
            # If dimension values are slugized, notation values are also slugized in codelist.
            notation_values_list = []
            if (dimension in self.slugized_list):
                # slugify the values
                slugized_unique_dime_vals_list = []
                for value in unique_dime_vals_list:
                    slugized_unique_dime_vals_list.append(str(value).lower().replace(" ", "-"))
                notation_values_list = slugized_unique_dime_vals_list
            # Otherwise, the values are copied exactly.
            else:
                notation_values_list = unique_dime_vals_list

            dimCodeList_df['Label'] = unique_dime_vals_list
            dimCodeList_df['Notation'] = notation_values_list
            # dataframe to csv
            CodeListcsvFileName = self.unique_folder_for_each_run + dimension + '.csv'
            dimCodeList_df.to_csv(CodeListcsvFileName, sep=',', encoding='utf-8', index=False)

    def generate_single_row_observations(self):

        # get measures/dimesnions names list
        components_df = pd.read_csv(self._input_components)
        measures_df = components_df[(components_df['Component Type'] == 'Measure')]
        self.measures_list = measures_df['Label'].tolist()
        dimensions_df = components_df[(components_df['Component Type'] == 'Dimension')]
        self.dimensions_list = dimensions_df['Label'].tolist()

        # get observation/measures values
        observations_df = pd.read_csv(self._input_observations)

        # create new observation data frame to hold new data format
        new_observations_header = []
        new_observations_row = []
        new_observations_list = []

        # prepare header
        for dim in self.dimensions_list:
            new_observations_header.append(dim)
        for new_head in self.observationFileHeaders:
            new_observations_header.append(new_head)
        # append to final list
        # new_observations_list.append(copy.deepcopy(new_observations_header))

        # extract measures values
        for index, row in observations_df.iterrows():
            for measure in self.measures_list:
                if (not math.isnan(row[measure])):
                    # dim values
                    for dim in self.dimensions_list:
                        new_observations_row.append(copy.deepcopy(row[dim]))
                    # mesure type
                    new_observations_row.append(measure)
                    # unit
                    # new_observations_row.append('')
                    # value
                    new_observations_row.append(copy.deepcopy(row[measure]))

                    # append to final list
                    new_observations_list.append(copy.deepcopy(new_observations_row))
                    # clean
                    del new_observations_row[:]

        # save observations to csv [using pandas]
        # readyObs_df = pd.DataFrame(new_observations_list, columns=new_observations_header)
        readyObsFileName = self.unique_folder_for_each_run + 'input' + '.csv'
        # readyObs_df.to_csv(readyObsFileName, sep=',', chunksize=5000, encoding='utf-8', index=False)

        # save observations to csv [using csv writer]
        total_size = len(new_observations_list)  # observations_df.size
        chucnkSize = 50000
        self.files_count = int(ceil(total_size / chucnkSize))

        counter = 0
        for i in range(0, len(new_observations_list), chucnkSize):
            chucnkList = new_observations_list[i:i + chucnkSize]
            with open(readyObsFileName + '_p' + str(counter), 'wb') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                # add header
                wr.writerow(new_observations_header)
                for row in chucnkList:
                    wr.writerow(row)
                counter += 1
            # clear memory
            del chucnkList[:]

        return readyObsFileName

    def decode_output(self):
        pass

    def generate_folder_name(self):
        basename = "data/table2qb_generated_files/"
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        folder_name = "_".join([basename, suffix])

        if not os.path.exists(folder_name + '/'):
            os.makedirs(folder_name + '/')
        return folder_name + '/'

    def chunks(self, inputList=[], numberOfChuncks=1):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(inputList), numberOfChuncks):
            yield inputList[i:i + numberOfChuncks]


if __name__ == "__main__":
    table2qb = table2qbWrapper()
    # table2qb.generate_code_lists()
    # print table2qb.generate_folder_name()
    # print table2qb.generate_single_row_observations()
    table2qb.run_full_table2qb_pipes()
