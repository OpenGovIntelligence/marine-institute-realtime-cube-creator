
#libraries
import csv
import json
import os

#objects
from util.mLogger import logee

#vars
from util.config import log_file, log_name, log_dir, outputsCSV_dir, skip_units_row

class FileOperations:

    # constructor
    def __init__(self):
        # initiate logger object
        global log
        log = logee(log_dir, log_file, log_name)

    def store_json_data_to_file_system(self, sender, json_data):

        log.info('storing to file system.')
        path = "outpts/"
        file_name = self.creating_file_name(sender)

        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except OSError as exception:
                log.error(exception)
        with open(path + file_name, 'w+') as outfile:
            json.dump(json_data, outfile)


    #the one in use
    def store_csv_data_to_file_system(self, csv_data, sender):

        log.logger.info('storing to file system.')
        #outputs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'outputsCSV'))
        #path = "outputsCSV/"
        file_name = self.creating_file_name(sender)

        if not os.path.exists(outputsCSV_dir):
            try:
                os.makedirs(outputsCSV_dir)
            except OSError as exception:
                log.logger.error(exception)
        #csvReader = csv.reader(csv_data)
        csvWriter = csv.writer(open(outputsCSV_dir +"/"+ file_name, 'w+'), delimiter=',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        #csv_data.next()  # skip header line
        #csv_data.next()  # skip header line
        row = 0 # to ignore unites row
        for line in csv_data:
            if skip_units_row:
                if row != 1:
                    print line
                    csvWriter.writerow(line)
                row += 1
            else:
                print line
                csvWriter.writerow(line)
    """search_output_dir_for_previous_responses function used in quality and lof service to chick previous file system cached responses"""
    def search_output_dir_for_previous_responses(file_name, path):


        for root, dirs, files in os.walk(path):
            if file_name in files:
                return str(os.path.join(root, file_name))

    """creating_file_name function used in quality and lof service to create name of the file caching the responses"""
    def creating_file_name(self,sender):
        # storing responses to file system for faster response time
        #setting default variables values
        features_names = ""
        file_name = "error_Nameing.csv"
        # try catch statemnt for error handling
        try:

            file_name = sender+".csv"

        # incase compiler catched an error
        except Exception, e:
            # logging error
            log.logger.error(e)


        return file_name
