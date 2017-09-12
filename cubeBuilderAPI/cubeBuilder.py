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

        """
        "> http://localhost:4567/cubeBuilderAPI/cubeBuilderArgs?" \
        "csv=/ogi-CubeSchema-creator/example_1/IWaveBNetwork_spectral.csv" \
        "&schema=/ogi-cubebuilder/src/main/resources/IWaveBNetowrk_spectral_output.ttl" \
        "&serializationIn=TURTLE" \
        "&serializationOut=TURTLE" \
        "&qbPath=/ogi-cubebuilder/test_output/" \
        "&qbName=webtest.ttl"
        """

    def transformToRDFcube_GET(self, cubebuilderapi, csv_file_path, csv_file_name, schema_path, schema_name, serialization_in,
                           serialization_out, qbpath, qbname):

        response = ""
        try:

            csv = encode_decode.encode(csv_file_path +"/"+ csv_file_name)  # inputFileNameAndLocation
            schema = encode_decode.encode(schema_path + "/" + schema_name + "_output.ttl")  # marineInstituteDatasetId
            serializationIn = "TURTLE"  # serlization" #
            serializationOut = "TURTLE"
            qbPath = encode_decode.encode(qbpath + "/")  # outputFileLocation
            qbName = encode_decode.encode(qbname + ".ttl")  # outputFileName

            APIurl = cubebuilderapi + "csv=" + csv + "&" + "schema=" + schema + "&" + "serializationIn=" + serializationIn + \
                     "&"+"serializationOut=" +serializationOut+ "&" + "qbPath=" + qbPath + "&" + "qbName=" + qbName

            print APIurl
            #response = requests.get(url).content
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


        """
        >>> r = requests.post("http://bugs.python.org", data={'number': 12524, 'type': 'issue', 'action': 'show'})
        >>> print(r.status_code, r.reason)
        """
        response = ""
        argumnets = {}
        try:
            argumnets['csv'] = csv_file_path +"/"+ csv_file_name  # inputFileNameAndLocation
            argumnets['schema']  = schema_path + "/" + schema_name + "_output.ttl"  # marineInstituteDatasetId
            argumnets['serializationIn']  = "TURTLE"  # serlization" #
            argumnets['serializationOut']  = "TURTLE"
            argumnets['qbPath']  = qbpath + "/"  # outputFileLocation
            argumnets['qbName']  = qbname + ".ttl"  # outputFileName


            #APIurl = cubebuilderapi + "csv=" + csv + "&" + "schema=" + schema + "&" + "serializationIn=" + serializationIn + \
             #        "&"+"serializationOut=" +serializationOut+ "&" + "qbPath=" + qbPath + "&" + "qbName=" + qbName
            #print APIurl

            response = requests.post(cubebuilderapi, argumnets)
            print response.status_code

        except Exception as e:
            logee.logger.error(e)

        return response

""" java service for the builder

        //get 
        get("cubeBuilderAPI/cubeBuilderArgs", "application/json", (request,
                response) -> {
            response.header("Access-Control-Allow-Origin", "*");
            response.header("Content-Type", "application/json");
            if (request.queryParams("csv")
                    != null && request.queryParams("schema") != null && request.queryParams("serializationIn") != null && request.queryParams("serializationOut") != null && request.queryParams("qbPath") != null && request.queryParams("qbName") != null) {
                String path = new File("").getAbsolutePath().substring(0, new File("").getAbsolutePath().length() - 16);
                csvFilePath_in = path + request.queryParams("csv");
                qbSchmeaPath_in = path + request.queryParams("schema");
                serialization_in = request.queryParams("serializationIn");
                serialization_out = request.queryParams("serializationOut");
                qbFilePath_out = path + request.queryParams("qbPath");
                qbFileName_out = request.queryParams("qbName");

                System.out.println(csvFilePath_in + "\n" + qbSchmeaPath_in + "\n" + serialization_in + "\n" + serialization_out + "\n" + qbFilePath_out + "\n" + qbFileName_out);
                return run();
            } else {
//                return "";
                JsonResponse = new JSONObject();
                JsonResponse.put("success", false);
                JsonResponse.put("error message", "Please check missing or incorrect arguments!");
                return JsonResponse.toString();
            }

        });

        //post if a post request is used to call 
        post("cubeBuilderAPI/cubeBuilderArgs", "application/json", (request,
                response) -> {
            response.header("Access-Control-Allow-Origin", "*");
            response.header("Content-Type", "application/json");
            if (request.queryParams("csv")
                    != null && request.queryParams("schema") != null && request.queryParams("serializationIn") != null && request.queryParams("serializationOut") != null && request.queryParams("qbPath") != null && request.queryParams("qbName") != null) {
                String path = new File("").getAbsolutePath().substring(0, new File("").getAbsolutePath().length() - 16);
                csvFilePath_in = path + request.queryParams("csv");
                qbSchmeaPath_in = path + request.queryParams("schema");
                serialization_in = request.queryParams("serializationIn");
                serialization_out = request.queryParams("serializationOut");
                qbFilePath_out = path + request.queryParams("qbPath");
                qbFileName_out = request.queryParams("qbName");

                System.out.println(csvFilePath_in + "\n" + qbSchmeaPath_in + "\n" + serialization_in + "\n" + serialization_out + "\n" + qbFilePath_out + "\n" + qbFileName_out);
                return run();
            } else {
//                return "Please check missing or incorrect arguments!";
                JsonResponse = new JSONObject();
                JsonResponse.put("success", false);
                JsonResponse.put("error_message", "Please check missing or incorrect arguments!");
                return JsonResponse.toString();
            }
        });


"""