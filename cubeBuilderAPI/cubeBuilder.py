#libraries
import requests

#objects
from util.mLogger import logee
from util.urlEncode import EncodeDecode

#vars
from util.config import log_dir, log_name, log_file


class CubeBuilder:




    def __init__(self):

        # initiate logger object
        global log
        log = logee(log_dir, log_file, log_name)

        global encode_decode
        encode_decode = EncodeDecode()



    def transformToRDFcube_GET(self, cubebuilderapi, csv_file_path, csv_file_name, schema_path, schema_name, serialization_in,
                           serialization_out, qbpath, qbname):

        response = ""
        try:
            #preparing and encoding webserive arguments
            csv = encode_decode.encode(csv_file_path +"/"+ csv_file_name)  # inputFileNameAndLocation
            schema = encode_decode.encode(schema_path + "/" + schema_name + "_output.ttl")  # marineInstituteDatasetId
            serializationIn = "TURTLE"  # serlization" #
            serializationOut = "TURTLE"
            qbPath = encode_decode.encode(qbpath + "/")  # outputFileLocation
            qbName = encode_decode.encode(qbname + ".ttl")  # outputFileName

            APIurl = cubebuilderapi + "csv=" + csv + "&" + "schema=" + schema + "&" + "serializationIn=" + serializationIn + \
                     "&"+"serializationOut=" +serializationOut+ "&" + "qbPath=" + qbPath + "&" + "qbName=" + qbName

            print APIurl
            #response = requests.get(url).content #not used

        except Exception as e:
            log.logger.error(e)

        return response


    def transformToRDFcube_POST(self, cubebuilderapi, csv_file_path, csv_file_name, schema_path, schema_name, serialization_in,
                           serialization_out, qbpath, qbname):

        """


        :param cubebuilderapi:
        :param csv_file_path:
        :param csv_file_name:
        :param schema_path:
        :param schema_name:
        :param serialization_in:
        :param serialization_out:
        :param qbpath:
        :param qbname:
        :return:
        """


        response = ""
        argumnets = {}
        try:
            # preparing and encoding webserive arguments [no http encoding needed in POST request ]

            argumnets['csv'] = csv_file_path +"/"+ csv_file_name  # inputFileNameAndLocation
            argumnets['schema']  = schema_path + "/" + schema_name + "_output.ttl"  # marineInstituteDatasetId
            argumnets['serializationIn']  = "TURTLE"  # serlization" #
            argumnets['serializationOut']  = "TURTLE"
            argumnets['qbPath']  = qbpath + "/"  # outputFileLocation
            argumnets['qbName']  = qbname + ".ttl"  # outputFileName




            response = requests.post(cubebuilderapi, argumnets)
            print response.status_code

        except Exception as e:
            logee.logger.error(e)

        return response
