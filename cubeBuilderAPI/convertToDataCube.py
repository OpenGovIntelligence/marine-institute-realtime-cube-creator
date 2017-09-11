






def transform_to_rdfcube(self, api, csv_file_path, csv_file_name, qbpath, qbname):
    response = ""
    if api == "IWaveBNetwork30Min":
        csv = csv_file_path + csv_file_name  # inputFileNameAndLocation
        schema = api  # marineInstituteDatasetId
        serialization = "turtle"  # serlization" #
        qbPath = qbpath  # outputFileLocation
        qbName = qbname  # outputFileName
        url = cube_builder_API + "csv=" + csv + "&" + "schema=" + schema + "&" + "serialization=" + serialization + "&" + "qbPath=" + qbPath + "&" + "qbName=" + qbName
        print url

        response = requests.get(url).content

    return response
