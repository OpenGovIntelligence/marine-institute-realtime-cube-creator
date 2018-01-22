
#objects
from cubeBuilderAPI.cubeBuilder import CubeBuilder
from util_bk.urlEncode import EncodeDecode

#vars
from util_bk.config import cubeBuilderAPI, outputsCSV_dir_for_builder, inputsSchemas_dir, outputsCubes_dir




global cubebuilder
cubebuilder = CubeBuilder()



#sending post request to the cube builderr service
cubebuilder.transformToRDFcube_POST(

    cubeBuilderAPI,
    outputsCSV_dir_for_builder,
    "IrishNationalTideGaugeNetwork__SRARTED__2017-09-11T16:42:57__TO__2017-09-12T16:42:57.csv",
    inputsSchemas_dir,
    "IrishNationalTideGaugeNetwork",
    "TURTLE",
    "TURTLE",
    outputsCubes_dir,
    "IrishNationalTideGaugeNetwork__SRARTED__2017-09-11T16:42:57__TO__2017-09-12T16:42:5"#without .csv

)


#transformToRDFcube(self, cubebuilderapi, csv_file_path, csv_file_name, schema_path,schema_name, serialization_in,
                           #serialization_out, qbpath, qbname):

cubebuilder.transformToRDFcube_GET(

    cubeBuilderAPI,
    outputsCSV_dir_for_builder,
    "IrishNationalTideGaugeNetwork__SRARTED__2017-09-11T16:42:57__TO__2017-09-12T16:42:57.csv",
    inputsSchemas_dir,
    "IrishNationalTideGaugeNetwork",
    "TURTLE",
    "TURTLE",
    outputsCubes_dir,
    "IrishNationalTideGaugeNetwork__SRARTED__2017-09-11T16:42:57__TO__2017-09-12T16:42:5"#without .csv

)

"http://localhost:4567/cubeBuilderAPI/cubeBuilderArgs?csv=/Users/mohade/GoogleDrive/__MYPERSONALBACKUP/TEMP-WAITING-ORGANIZATION/3-workspace/ogi-publishing-pipeline-realtime/outputsCSV/IrishNationalTideGaugeNetwork__SRARTED__2017-09-10T18%3A27%3A46__TO__2017-09-11T18%3A27%3A46.csv&schema=/Users/mohade/GoogleDrive/__MYPERSONALBACKUP/TEMP-WAITING-ORGANIZATION/3-workspace/ogi-publishing-pipeline-realtime/inputsSchemas/IrishNationalTideGaugeNetwork_output.ttl&serializationIn=TURTLE&serializationOut=TURTLE&qbPath=/Users/mohade/GoogleDrive/__MYPERSONALBACKUP/TEMP-WAITING-ORGANIZATION/3-workspace/ogi-publishing-pipeline-realtime/outputsCubes/&qbName=IrishNationalTideGaugeNetwork__SRARTED__2017-09-10T18%3A27%3A46__TO__2017-09-11T18%3A27%3A46.ttl"