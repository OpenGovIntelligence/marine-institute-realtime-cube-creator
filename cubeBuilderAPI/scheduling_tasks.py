import datetime
import datetime
import schedule
import time
import urllib
from datetime import timedelta

from marineDataAPI.marineAPI import Ds_API

#todo : logging

global ds_api
ds_api = Ds_API()


def job(t):
    print "I'm working...", t
    ds_tasks("IWaveBNetwork30Min", time_from=prepare_time_from())
    #ds_tasks("IMI_EATL_WAVE",  time_from=prepare_time_from())
    #ds_tasks("IWBNetwork",  time_from=prepare_time_from())
    #ds_tasks("IrishNationalTideGaugeNetwork",  time_from=prepare_time_from())

    return



"""screen scheduled_tasks.py"""

def ds_tasks(api, time_from):

    temp_csv_data =  ds_api.get_csv(api, time_from, "jjj")
    print temp_csv_data



    ds_api.put_csv_to_file(temp_csv_data, file_name=api+"_"+decode(time_from).replace(" ","_"))
    ds_api.transform_to_rdfcube(api, csv_file_path="/ogi-publishing-pipeline-realtime/MI_ds1_data/", csv_file_name=api+"_"+decode(time_from).replace(" ","_")+".csv", qbpath="/ogi-publishing-pipeline-realtime/MI_ds1_data/", qbname=api+"_"+decode(time_from).replace(" ","_")+".ttl")
    #ds_api.push_to_rdf_datastore()
    print "done "+ api + "! file:"+ api+"_"+decode(time_from)
    return

def prepare_time_from():


    time_from = "time%3E=2017-06-07T00%3A00%3A00Z"

    # print encode(time_from)

    # print decode(time_from)

    print time_from
    print datetime.datetime.now().replace(microsecond=0).isoformat()
    print encode(datetime.datetime.now().replace(microsecond=0).isoformat())

    yesterday = datetime.datetime.now() - timedelta(days=1)
    yesterday.strftime('%m%d%y')

    print yesterday

    print encode(yesterday.replace(microsecond=0).isoformat())

    time_from = encode(yesterday.replace(microsecond=0).isoformat())

    return time_from

def encode(URL):
    URI_encoded = urllib.quote_plus(URL)
    #   print URI_encoded
    return URI_encoded


def decode(URL):
    URI_decoded = urllib.unquote(URL)
    #   print URI_encoded
    return URI_decoded


job("start")


"""scheduling
schedule.every().day.at("01:00").do(job,'It is 01:00 time to start harvesting MI data!')

while True:
    schedule.run_pending()
    time.sleep(01) # wait one minute
    print datetime.datetime.now().isoformat()
"""