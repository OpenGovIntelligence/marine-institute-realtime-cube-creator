import csv
import json
#import requests
import urllib2

#objects
from util.file_sys_operations import FileOperations
from util.mLogger import logee

#vars
from util.config import log_dir, log_name, log_file


class MarineAPI:



    # constructor
    def __init__(self):

        # initiate logger object
        global log
        log = logee(log_dir, log_file, log_name)

        global file_sys
        file_sys = FileOperations()

        # times place holders
        global time_from
        time_from = ""
        global time_to
        time_to = ""

        # datasets APIs
        """
        global url_csv_IMIEATLWAVE
        url_csv_IMIEATLWAVE = "https://erddap.marine.ie/erddap/griddap/IMI_EATL_WAVE.csv?significant_wave_height[(" + time_from + "):1:(" + time_to + ")][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)],swell_wave_height[(" + time_from + "):1:(" + time_to + ")][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)],mean_wave_direction[(" + time_from + "):1:(" + time_to + ")][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)],mean_wave_period[(" + time_from + "):1:(" + time_to + ")][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)]"

        global url_json_IMIEATLWAVE
        url_json_IMIEATLWAVE = "https://erddap.marine.ie/erddap/griddap/IMI_EATL_WAVE.json?significant_wave_height[(2017-06-12T21:00:00Z):1:(2017-06-19T21:00:00Z)][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)],swell_wave_height[(2017-06-12T21:00:00Z):1:(2017-06-19T21:00:00Z)][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)],mean_wave_direction[(2017-06-12T21:00:00Z):1:(2017-06-19T21:00:00Z)][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)],mean_wave_period[(2017-06-12T21:00:00Z):1:(2017-06-19T21:00:00Z)][(36.5125):1:(59.987500000000004)][(-19.9875):1:(-0.01249999999999929)]"
        """
        global url_csv_IWBNetwork
        url_csv_IWBNetwork = "https://erddap.marine.ie/erddap/tabledap/IWBNetwork.csv?station_id%2Clongitude%2Clatitude%2Ctime%2CAtmosphericPressure%2CWindDirection%2CWindSpeed%2CGust%2CWaveHeight%2CWavePeriod%2CMeanWaveDirection%2CHmax%2CAirTemperature%2CDewPoint%2CSeaTemperature%2Csalinity%2CRelativeHumidity%2CQC_Flag&time%3E=" + time_from

        global url_csv_IWaveBNetwork_spectral
        url_csv_IWaveBNetwork_spectral = "https://erddap.marine.ie/erddap/tabledap/IWaveBNetwork_spectral.csv?buoy_id%2Ctime%2Clatitude%2Clongitude%2Cstation_id%2CPeakDirection%2CPeakSpread%2CSignificantWaveHeight%2CEnergyPeriod%2CMeanWavePeriod_Tm01%2CMeanWavePeriod_Tm02%2CPeakPeriod%2Cqcflag&time%3E=" + time_from

        global url_csv_IWaveBNetwork_zerocrossing
        url_csv_IWaveBNetwork_zerocrossing = "https://erddap.marine.ie/erddap/tabledap/IWaveBNetwork_zerocrossing.csv?buoy_id%2Ctime%2Clatitude%2Clongitude%2Cstation_id%2CHmax%2CHmaxPeriod%2CHavg%2CTavg%2Cqcflag&time%3E=" + time_from

        global url_csv_IrishNationalTideGaugeNetwork
        url_csv_IrishNationalTideGaugeNetwork = "https://erddap.marine.ie/erddap/tabledap/IrishNationalTideGaugeNetwork.csv?longitude%2Clatitude%2Caltitude%2Ctime%2Cstation_id%2CWater_Level%2CWater_Level_LAT%2CWater_Level_OD_Malin%2CQC_Flag&time%3E=" + time_from

        # deprecated dataset
        url_json_IWaveBNetwork30Min = "https://erddap.marine.ie/erddap/tabledap/IWaveBNetwork30Min.json?longitude%2Clatitude%2Ctime%2Cstation_id%2CPeakPeriod%2CPeakDirection%2CUpcrossPeriod%2CSignificantWaveHeight%2CSeaTemperature%2CHmax%2CTHmax%2CMeanCurDirTo%2CMeanCurSpeed%2CSignificantWaveHeight_qc%2CPeakPeriod_qc%2CPeakDirection_qc%2CUpcrossPeriod_qc%2CSeaTemperature_qc%2CHmax_qc%2CTHmax_qc%2CMeanCurDirTo_qc%2CMeanCurSpeed_qc&time%3E="  # 2017-06-07T00%3A00%3A00Z"

        url_csv_IWaveBNetwork30Min = "https://erddap.marine.ie/erddap/tabledap/IWaveBNetwork30Min.csv?longitude%2Clatitude%2Ctime%2Cstation_id%2CPeakPeriod%2CPeakDirection%2CUpcrossPeriod%2CSignificantWaveHeight%2CSeaTemperature%2CHmax%2CTHmax%2CMeanCurDirTo%2CMeanCurSpeed%2CSignificantWaveHeight_qc%2CPeakPeriod_qc%2CPeakDirection_qc%2CUpcrossPeriod_qc%2CSeaTemperature_qc%2CHmax_qc%2CTHmax_qc%2CMeanCurDirTo_qc%2CMeanCurSpeed_qc&time%3E="  # 2017-06-07T00%3A00%3A00Z"

    #not finished yet as not in scope
    def getJSON(self,api):
        r= ""
        #if api == "IWaveBNetwork30Min":
            #url = url_json_IWaveBNetwork30Min
            #r = requests.get(url).json()


        #print r.headers
        #data_dim_json = response_dim_json.json()
        return r

    def getCSV (self, MIapi):



        response = urllib2.urlopen(MIapi)
        csvReader = csv.reader(response)

        #print r.headers
        #data_dim_json = response_dim_json.json()



        #if MIapi == "IWaveBNetwork30Min":
            #url = url_csv_IWaveBNetwork30Min + time_from
            #r = requests.get(url).content
            ##response = urllib2.urlopen(url)
            #csvReader = csv.reader(response)



        #if MIapi == "IMI_EATL_WAVE":

            #url = url_csv_IMI_EATL_WAVE + time_from + time_to
            #response = urllib2.urlopen(url)
            #csvReader = csv.reader(response)

        #else:

        return csvReader

    def putCSVToFile(self, csv_data, file_name):
        #print "waiting logic"
        file_sys.store_csv_data_to_file_system(csv_data, file_name)

        return "success"

    def getAPIurl(self, api, timeFrom, timeTo):

        time_from = timeFrom
        time_to = timeTo

        if api == "IrishNationalTideGaugeNetwork":

            print url_csv_IrishNationalTideGaugeNetwork+time_from
            return url_csv_IrishNationalTideGaugeNetwork+time_from

        if api == "IWaveBNetwork_spectral":

            print url_csv_IWaveBNetwork_spectral+time_from
            return url_csv_IWaveBNetwork_spectral+time_from

        if api == "IWaveBNetwork_zerocrossing":

            print url_csv_IWaveBNetwork_zerocrossing +time_from
            return url_csv_IWaveBNetwork_zerocrossing +time_from

        if api == "IWBNetwork":

            print url_csv_IWBNetwork+time_from
            return url_csv_IWBNetwork+time_from
