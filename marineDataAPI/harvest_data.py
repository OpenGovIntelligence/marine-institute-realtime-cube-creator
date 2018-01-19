
#objects
from util.urlEncode import EncodeDecode
from marineDataAPI.marineAPI import MarineAPI
from util.time import TimeOperations

#vars
from util.config import ds_names

global marineAPI
marineAPI = MarineAPI()

global encode
encode = EncodeDecode()

global time
time=TimeOperations()



#prepare time
timeStartFrom_encoded=time.getTimeFromEncoded()
timeEndAt_encoded=time.getTimeToEncoded()

timeStartFrom=time.getTimeFrom()
timeEndAt=time.getTimeTo()

#prepare datasets names

ds_names_list = ds_names.values()

#In Python 3
#list(d.values())


#harvet data
for ds in ds_names_list:
    apiURL = marineAPI.getAPIurl(ds, timeStartFrom_encoded, timeEndAt_encoded)
    print ("API URL arguments :", apiURL)
    csvData = marineAPI.getCSV(apiURL)

    # for row in csvData:
    #    print row

    csvfileName = ds +"__SRARTED__"+timeStartFrom+"__TO__"+timeEndAt
    message = marineAPI.putCSVToFile(csvData, csvfileName)

    if message:
        print message


