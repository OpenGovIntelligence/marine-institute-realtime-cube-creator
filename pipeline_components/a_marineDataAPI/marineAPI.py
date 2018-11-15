# add outer modules
import sys

# sys.path.insert(0, '/home/mohade/workspace/marine-institute-realtime-cube-creator/shared')
sys.path.append('/home/mohade/workspace/marine-institute-realtime-cube-creator/shared')

import csv
import json
# import requests
import urllib2

# objects
from util.file_sys_operations import FileOperations
from util.mLogger import logee

# vars
from util.config import log_dir, log_name, log_file

# objects
from util.urlEncode import EncodeDecode
# from marineDataAPI.marineAPI import MarineAPI
from util.time import TimeOperations
# vars
from util.config import ds_names


class MarineDataPortalApi(object):

    def __init__(self):

        self.encode = EncodeDecode()
        self.time = TimeOperations()
        # initiate logger object
        self.log = logee(log_dir, log_file, log_name)
        self.file_sys = FileOperations()
        # times place holders
        self.time_from = ""
        self.time_to = ""

        # datasets APIs/URLs
        self.url_csv_IWBNetwork = "https://erddap.marine.ie/erddap/tabledap/IWBNetwork.csv0?station_id%2Clongitude%2Clatitude%2Ctime%2CAtmosphericPressure%2CWindDirection%2CWindSpeed%2CGust%2CWaveHeight%2CWavePeriod%2CMeanWaveDirection%2CHmax%2CAirTemperature%2CDewPoint%2CSeaTemperature%2Csalinity%2CRelativeHumidity%2CQC_Flag&time%3E="
        self.url_csv_IWaveBNetwork_spectral = "https://erddap.marine.ie/erddap/tabledap/IWaveBNetwork_spectral.csv0?buoy_id%2Ctime%2Clatitude%2Clongitude%2Cstation_id%2CPeakDirection%2CPeakSpread%2CSignificantWaveHeight%2CEnergyPeriod%2CMeanWavePeriod_Tm01%2CMeanWavePeriod_Tm02%2CPeakPeriod%2Cqcflag&time%3E="
        self.url_csv_IWaveBNetwork_zerocrossing = "https://erddap.marine.ie/erddap/tabledap/IWaveBNetwork_zerocrossing.csv0?buoy_id%2Ctime%2Clatitude%2Clongitude%2Cstation_id%2CHmax%2CHmaxPeriod%2CHavg%2CTavg%2Cqcflag&time%3E="
        self.url_csv_IrishNationalTideGaugeNetwork = "https://erddap.marine.ie/erddap/tabledap/IrishNationalTideGaugeNetwork.csv0?longitude%2Clatitude%2Caltitude%2Ctime%2Cstation_id%2CWater_Level%2CWater_Level_LAT%2CWater_Level_OD_Malin%2CQC_Flag&time%3E="
        # deprecated dataset
        # self.url_json_IWaveBNetwork30Min = "https://erddap.marine.ie/erddap/tabledap/IWaveBNetwork30Min.json?longitude%2Clatitude%2Ctime%2Cstation_id%2CPeakPeriod%2CPeakDirection%2CUpcrossPeriod%2CSignificantWaveHeight%2CSeaTemperature%2CHmax%2CTHmax%2CMeanCurDirTo%2CMeanCurSpeed%2CSignificantWaveHeight_qc%2CPeakPeriod_qc%2CPeakDirection_qc%2CUpcrossPeriod_qc%2CSeaTemperature_qc%2CHmax_qc%2CTHmax_qc%2CMeanCurDirTo_qc%2CMeanCurSpeed_qc&time%3E="  # 2017-06-07T00%3A00%3A00Z"
        # self.url_csv_IWaveBNetwork30Min = "https://erddap.marine.ie/erddap/tabledap/IWaveBNetwork30Min.csv?longitude%2Clatitude%2Ctime%2Cstation_id%2CPeakPeriod%2CPeakDirection%2CUpcrossPeriod%2CSignificantWaveHeight%2CSeaTemperature%2CHmax%2CTHmax%2CMeanCurDirTo%2CMeanCurSpeed%2CSignificantWaveHeight_qc%2CPeakPeriod_qc%2CPeakDirection_qc%2CUpcrossPeriod_qc%2CSeaTemperature_qc%2CHmax_qc%2CTHmax_qc%2CMeanCurDirTo_qc%2CMeanCurSpeed_qc&time%3E="  # 2017-06-07T00%3A00%3A00Z"

    def start_harvesting(self):

        # prepare time
        timeStartFrom_encoded = self.time.getTimeFromEncoded()
        timeEndAt_encoded = self.time.getTimeToEncoded()

        timeStartFrom = self.time.getTimeFrom()
        timeEndAt = self.time.getTimeTo()

        # prepare datasets names
        ds_names_list = ds_names.values()

        # In Python 3
        # list(d.values())

        # harvet data
        for ds in ds_names_list:
            apiURL = self.getAPIurl(ds, timeStartFrom_encoded, timeEndAt_encoded)
            print("API URL arguments :", apiURL)
            csvData = self.getCSV(apiURL)

            # for row in csvData:
            #    print row

            csvfileName ="__SRARTED__" + timeStartFrom + "__TO__" + timeEndAt +"__ds__" + ds
            message = self.putCSVToFile(csvData, csvfileName)

            if message:
                print  message

    # not finished yet as not in scope OF ogi project
    def getJSON(self, api):
        r = ""
        # if api == "IWaveBNetwork30Min":
        # url = url_json_IWaveBNetwork30Min
        # r = requests.get(url).json()

        # print r.headers
        # data_dim_json = response_dim_json.json()
        return r

    def getCSV(self, MIapi):

        response = urllib2.urlopen(MIapi)
        csvReader = csv.reader(response)

        # print r.headers
        # data_dim_json = response_dim_json.json()

        # if MIapi == "IWaveBNetwork30Min":
        # url = url_csv_IWaveBNetwork30Min + time_from
        # r = requests.get(url).content
        ##response = urllib2.urlopen(url)
        # csvReader = csv.reader(response)

        # if MIapi == "IMI_EATL_WAVE":

        # url = url_csv_IMI_EATL_WAVE + time_from + time_to
        # response = urllib2.urlopen(url)
        # csvReader = csv.reader(response)

        # else:

        return csvReader

    def putCSVToFile(self, csv_data, file_name):
        # print "waiting logic"
        self.file_sys.store_csv_data_to_file_system(csv_data, file_name)

        return "success"

    def getAPIurl(self, api, timeFrom, timeTo):

        time_from = timeFrom
        time_to = timeTo

        if api == "IrishNationalTideGaugeNetwork":
            print self.url_csv_IrishNationalTideGaugeNetwork + time_from
            return self.url_csv_IrishNationalTideGaugeNetwork + time_from

        if api == "IWaveBNetwork_spectral":
            print self.url_csv_IWaveBNetwork_spectral + time_from
            return self.url_csv_IWaveBNetwork_spectral + time_from

        if api == "IWaveBNetwork_zerocrossing":
            print self.url_csv_IWaveBNetwork_zerocrossing + time_from
            return self.url_csv_IWaveBNetwork_zerocrossing + time_from

        if api == "IWBNetwork":
            print self.url_csv_IWBNetwork + time_from
            return self.url_csv_IWBNetwork + time_from


if __name__ == "__main__":
    marineAPI = MarineDataPortalApi()
    marineAPI.start_harvesting()
