
#objects
from util.urlEncode import Encode
from marineDataAPI.marineAPI import MarineAPI
from util.time import TimeOperations

#vars
from util.config import ds_IrishNationalTideGaugeNetwork, ds_IWaveBNetwork_spectral, ds_IWaveBNetwork_zerocrossing, ds_IWBNetwork


global marineAPI
marineAPI = MarineAPI()

global encode
encode = Encode()

global time
time=TimeOperations()


#prepare list for loop

datasets_list = []

datasets_list.append(ds_IrishNationalTideGaugeNetwork)
datasets_list.append(ds_IWaveBNetwork_spectral)
datasets_list.append(ds_IWaveBNetwork_zerocrossing)
datasets_list.append(ds_IWBNetwork)


#prepare time
timeStartFrom_encoded=time.getTimeFrom()
timeEndAt_encoded=time.getTimeTo()

timeStartFrom=time.getTimeFromEncoded()
timeEndAt=time.getTimeToEncoded()


#harvet data
for ds in datasets_list:
    apiURL = marineAPI.getAPIurl(ds, timeStartFrom_encoded, timeEndAt_encoded)
    print ("API URL arguments :", apiURL)
    csvData = marineAPI.getCSV(apiURL)

    # for row in csvData:
    #    print row

    csvfileName = ds +"__SRARTED__"+timeStartFrom+"__TO__"+timeEndAt
    message = marineAPI.putCSVToFile(csvData, csvfileName)

    if message:
        print message


