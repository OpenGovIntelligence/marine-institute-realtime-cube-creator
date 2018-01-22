#libraries
import rdflib
import pprint
from SPARQLWrapper import SPARQLWrapper, RDF, JSON, POST, SELECT
import subprocess, shlex
import os

#from rdflib.store import Store
#from rdflib.plugin import get as plugin
from rdflib.plugins.stores import sparqlstore

#objects
from util_bk.mLogger import logee

#vars
from util_bk.config import log_dir, log_name, log_file
from util_bk.config import endpoint_password, endpoint_rdf_store_url,\
    endpoint_user_name, prefixes, endpoint_rdf_store_url_crud, testing_graph_name


class RDFStoreAPI:


    def __init__(self, ):

        # initiate logger object
        global log
        log = logee(log_dir, log_file, log_name)

        #global Virtuoso
        #Virtuoso = plugin("Virtuoso", Store)


        #global store
        #store = Virtuoso("DSN=VOS;UID=dba;PWD=dba;WideAsUTF16=Y")





    def push_to_druid_datastore(self, rdf_file_path):
        print "waiting logic"

    """
    I have to use direct curl within my code because:
    (1) can't load a whole file to virtuoso http api
    (2) parsing the file using RDFlib and sending it to virtuso is also failing because of (blanknodes) support in rdflib
    """

    def push_curl(self, file_path, file_name):
        file_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'rdfDataStoreAPI')) +"/"

        curl = 'curl -X POST --digest -u "'+endpoint_user_name+':'+endpoint_password+'"'\
               +' -T "'+ file_dir + file_name+'"'\
                +' -G "'+endpoint_rdf_store_url_crud+'"'\
                    +' --data-urlencode "' + testing_graph_name +'"'

        """
        curl -X PUT/POST --digest -u "dba:deriegovvirtuoso" -T "/Users/mohade/GoogleDrive/__MYPERSONALBACKUP/TEMP-WAITING-ORGANIZATION/3-workspace/ogi-publishing-pipeline-realtime/rdfDataStoreAPI/test.ttl" -G "http://vmogi01.deri.ie:8000/sparql-graph-crud-auth" --data-urlencode "graph=http://someaddress:8890/db"
        
        """



        print curl
        bash_com = shlex.split(curl)
        subprocess.Popen(bash_com)
       # output = subprocess.check_output(['bash', '-c', bash_com])
        #print output
        print "done"




test.push_curl("","test.ttl")