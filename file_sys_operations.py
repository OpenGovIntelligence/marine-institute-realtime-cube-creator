from mLogger import Logee
import json

import csv
import urllib2

class File_sys:

    # constructor
    def __init__(self):
        # initiate logger object
        global logee
        logee = Logee("pulishing_pipeline.log", "pulishing_pipeline:file_sys")




    def store_json_data_to_file_system(self, sender, json_data):

        logee.info('storing to file system.')
        path = "MI_ds1_data/"
        file_name = self.creating_file_name(sender)
        import os
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except OSError as exception:
                logee.error(exception)
        with open(path + file_name, 'w+') as outfile:
            json.dump(json_data, outfile)

    def store_csv_data_to_file_system(self, sender, csv_data):

        logee.logger.info('storing to file system.')
        path = "MI_ds1_data/"
        file_name = self.creating_file_name(sender)
        import os
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except OSError as exception:
                logee.logger.error(exception)
        #csvReader = csv.reader(csv_data)
        csvWriter = csv.writer(open(path + file_name, 'w+'), delimiter=',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        #csv_data.next()  # skip header line
        #csv_data.next()  # skip header line
        for line in csv_data:
            csvWriter.writerow(line)

    """search_output_dir_for_previous_responses function used in quality and lof service to chick previous file system cached responses"""
    def search_output_dir_for_previous_responses(file_name, path):
        import os

        for root, dirs, files in os.walk(path):
            if file_name in files:
                return str(os.path.join(root, file_name))

    """creating_file_name function used in quality and lof service to create name of the file caching the responses"""
    def creating_file_name(self,sender):
        # storing responses to file system for faster response time
        #setting default variables values
        features_names = ""
        json_response = "error.json"
        # try catch statemnt for error handling
        try:

            file_name = sender+".csv"

        # incase compiler catched an error
        except Exception, e:
            # logging error
            logee.logger.error(e)


        return file_name
