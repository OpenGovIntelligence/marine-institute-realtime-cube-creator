from subprocess import call
import pycurl
import json

#@TODO check this --> http://druid.io/docs/latest/tutorials/tutorial-streams.html

class DRUID(object):

    def __init__(self):
        print
        'DRUID class of pushing data cube observations from cubiql to druid!'

    def push_observations_to_druid_BATCH(self, druidServer, schemaFile, observations_file_path, method='pycurl'):

        print
        'push to druid using batch -- index file =  ' + str(schemaFile) \
        + ' -- observations file = ' + str(observations_file_path) \
        + ' -- druid server url = ' + str(druidServer)

        # @todo OPTIONAL change observation location
        # read schema file json
        with open(schemaFile, 'r') as sfile:
            schema = json.load(sfile)
        print schema
        schema['spec']['ioConfig']['inputSpec']['paths'] = observations_file_path

        with open(schemaFile, 'w') as sfileW:
            json.dump(schema, sfileW)

        schema = json.dumps(schema)
        print schema

        if method == 'curl':
            # method 'A' pure curl
            """ example curl push
                        ['curl', '-X',
                        'POST', '-H', 'Content-Type:application/json', '--data', '@examples / wikipedia - index.json',
                        'http: // localhost:8090 / druid / indexer / v1 / task']
            """

            # add @ to file name
            schemaFile = '@' + str(schemaFile)

            curlPost_cmd_list_param = ['curl', '-X', 'POST', '-H', 'Content-Type:application/json', '--data',
                                       schemaFile, druidServer]
            call(curlPost_cmd_list_param)

        if method == 'pycurl':
            # method 'B' pyCurl

            pycrl = pycurl.Curl()
            pycrl.setopt(pycrl.URL,
                         druidServer)

            pycrl.setopt(pycrl.POST, 1)
            # pycrl.setopt(pycrl.HTTPPOST, [(pycrl.FORM_FILE, schemaFile)])
            pycrl.setopt(pycurl.HTTPHEADER, ['Content-Type:application/json'])
            pycrl.setopt(pycurl.POSTFIELDS, schema)

            pycrl.perform()
            pycrl.close()

    def push_observations_to_druid_STREAM(self, druidServer, schemaFile, observations_url):
        # @TODO / OPTIONAL
        print
        'push to druid using batch -- index file =  ' + str(schemaFile) \
        + ' -- observations file = ' + str(observations_url) \
        + ' -- druid server url = ' + str(druidServer)


if __name__ == '__main__':
    druid = DRUID()
    ###pycurl
    druid.push_observations_to_druid_BATCH(druidServer='vmogi01.deri.ie:8090/druid/indexer/v1/task',
                                           schemaFile='schema_IWBNetwork.json',
                                           observations_file_path='/home/mohade/ogitesting/druid/druid-0.10.1/datasets/ogi-sample-datasets/for_druid/marine/IWBNetwork/IWBNetwork.json',
                                           method='pycurl')
    ###curl
    druid.push_observations_to_druid_BATCH(druidServer='vmogi01.deri.ie:8090/druid/indexer/v1/task',
                                           schemaFile='schema_IWBNetwork.json',
                                           observations_file_path='/home/mohade/ogitesting/druid/druid-0.10.1/datasets/ogi-sample-datasets/for_druid/marine/IWBNetwork/IWBNetwork.json',
                                           method='curl')
