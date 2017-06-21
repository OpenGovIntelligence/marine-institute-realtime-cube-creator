import requests
import urllib3
import json
from mLogger import Logee

from file_sys_operations import File_sys

import csv
import urllib2

class Ds_API:



    # constructor
    def __init__(self):

        # initiate logger object
        global logee
        logee = Logee("pulishing_pipeline.log", "pulishing_pipeline:file_sys")

        global cube_builder_API
        cube_builder_API = "http://localhost:4567/cubeBuilderAPI/cubeBuilderArgs?"

        global file_sys
        file_sys = File_sys()

        global url_json_IMI_EATL_WAVE
        url_json_IMI_EATL_WAVE = "https://erddap.marine.ie/erddap/griddap/IMI_EATL_WAVE.json?significant_wave_height[(2017-06-12T21:00:00Z):1:(2017-06-19T21:00:00Z)][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)],swell_wave_height[(2017-06-12T21:00:00Z):1:(2017-06-19T21:00:00Z)][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)],mean_wave_direction[(2017-06-12T21:00:00Z):1:(2017-06-19T21:00:00Z)][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)],mean_wave_period[(2017-06-12T21:00:00Z):1:(2017-06-19T21:00:00Z)][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)]"

        global url_csv_IMI_EATL_WAVE
        url_csv_IMI_EATL_WAVE = "https://erddap.marine.ie/erddap/griddap/IMI_EATL_WAVE.csv?significant_wave_height[(2017-06-12T21:00:00Z):1:(2017-06-19T21:00:00Z)][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)],swell_wave_height[(2017-06-12T21:00:00Z):1:(2017-06-19T21:00:00Z)][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)],mean_wave_direction[(2017-06-12T21:00:00Z):1:(2017-06-19T21:00:00Z)][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)],mean_wave_period[(2017-06-12T21:00:00Z):1:(2017-06-19T21:00:00Z)][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)]"

        global url_json_IWaveBNetwork30Min
        url_json_IWaveBNetwork30Min = "https://erddap.marine.ie/erddap/tabledap/IWaveBNetwork30Min.json?longitude%2Clatitude%2Ctime%2Cstation_id%2CPeakPeriod%2CPeakDirection%2CUpcrossPeriod%2CSignificantWaveHeight%2CSeaTemperature%2CHmax%2CTHmax%2CMeanCurDirTo%2CMeanCurSpeed%2CSignificantWaveHeight_qc%2CPeakPeriod_qc%2CPeakDirection_qc%2CUpcrossPeriod_qc%2CSeaTemperature_qc%2CHmax_qc%2CTHmax_qc%2CMeanCurDirTo_qc%2CMeanCurSpeed_qc&time%3E="#2017-06-07T00%3A00%3A00Z"

        global url_csv_IWaveBNetwork30Min
        url_csv_IWaveBNetwork30Min = "https://erddap.marine.ie/erddap/tabledap/IWaveBNetwork30Min.csv?longitude%2Clatitude%2Ctime%2Cstation_id%2CPeakPeriod%2CPeakDirection%2CUpcrossPeriod%2CSignificantWaveHeight%2CSeaTemperature%2CHmax%2CTHmax%2CMeanCurDirTo%2CMeanCurSpeed%2CSignificantWaveHeight_qc%2CPeakPeriod_qc%2CPeakDirection_qc%2CUpcrossPeriod_qc%2CSeaTemperature_qc%2CHmax_qc%2CTHmax_qc%2CMeanCurDirTo_qc%2CMeanCurSpeed_qc&time%3E="#2017-06-07T00%3A00%3A00Z"

        global time_from
        time_from =  "time%3E=2017-06-07T00%3A00%3A00Z"

    def encode (self,URl):
        URl_encoded = urllib3.quote_plus(URl)
        #   print URI_encoded
        return URl_encoded

    def get_json(self,api):
        if api == "IWaveBNetwork30Min":
            url = url_json_IWaveBNetwork30Min
            r = requests.get(url).json()


        #print r.headers
        #data_dim_json = response_dim_json.json()
        return r

    def get_csv (self,api, time_from, time_to):

        if api == "IWaveBNetwork30Min":
            url = url_csv_IWaveBNetwork30Min + time_from
            #r = requests.get(url).content
            response = urllib2.urlopen(url)
            csvReader = csv.reader(response)



        if api == "IMI_EATL_WAVE":
            """Restructure url format"""
            url = url_csv_IMI_EATL_WAVE + time_from + time_to
            response = urllib2.urlopen(url)
            csvReader = csv.reader(response)

        #print r.headers
        #data_dim_json = response_dim_json.json()
        return csvReader

    def put_csv_to_file(self, csv_data, file_name):
        #print "waiting logic"
        file_sys.store_csv_data_to_file_system(file_name, csv_data)

    def transform_to_rdfcube(self, api, csv_file_path, csv_file_name, qbpath, qbname):
        if api == "IWaveBNetwork30Min":
            csv = csv_file_path + csv_file_name #inputFileNameAndLocation
            schema = api #marineInstituteDatasetId
            serialization = "turtle"#serlization" #
            qbPath = qbpath #outputFileLocation
            qbName = qbname #outputFileName
            url = cube_builder_API +"csv="+csv+"&"+"schema="+schema+"&"+"serialization="+serialization+"&"+"qbPath="+qbPath+"&"+"qbName="+qbName
            print url
            print requests.get(url).content



    def push_to_rdf_datastore(self, rdf_file_path):
        print "waiting logic"



