# add outer modules
import sys

# sys.path.insert(0, '/home/mohade/workspace/marine-institute-realtime-cube-creator/shared')
sys.path.append('/home/mohade/workspace/marine-institute-realtime-cube-creator/shared')

# libraries
import rdflib
import pprint
from SPARQLWrapper import SPARQLWrapper, RDF, JSON, POST, SELECT
import subprocess, shlex
import os

# from rdflib.store import Store
# from rdflib.plugin import get as plugin
from rdflib.plugins.stores import sparqlstore

# objects
from util.mLogger import logee

# vars
from util.config import log_dir, log_name, log_file
from util.config import endpoint_password, endpoint_rdf_store_url, endpoint_user_name, prefixes, endpoint_rdf_store_url_crud, testing_graph_name


class RDFStoreAPI:

    def __init__(self):

        # initiate logger object
        global log
        log = logee(log_dir, log_file, log_name)

        # global Virtuoso
        # Virtuoso = plugin("Virtuoso", Store)

        # global store
        # store = Virtuoso("DSN=VOS;UID=dba;PWD=dba;WideAsUTF16=Y")

    def push_to_rdf_datastore(self, rdf_file_path):
        print "waiting logic"

    """
    I have to use direct curl within my code because:
    (1) can't load a whole file to virtuoso http api
    (2) parsing the file using RDFlib and sending it to virtuso is also failing because of (blanknodes) support in rdflib
    """

    def push_curl(self, file_path):
        file_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'rdfDataStoreAPI')) + "/"

        curl = 'curl -X POST --digest -u "' + endpoint_user_name + ':' + endpoint_password + '"' \
               + ' -T "' + file_path + '"' \
               + ' -G "' + endpoint_rdf_store_url_crud + '"' \
               + ' --data-urlencode "' + testing_graph_name + '"'

        """
        curl -X PUT/POST --digest -u "dba:deriegovvirtuoso" -T "/Users//test.ttl" -G "http://vmogi01.deri.ie:8000/sparql-graph-crud-auth" --data-urlencode "graph=http://someaddress:8890/db"

        """

        print curl
        bash_com = shlex.split(curl)
        subprocess.Popen(bash_com)
        # output = subprocess.check_output(['bash', '-c', bash_com])
        # print output
        print "done"

    def get_triples(self, file_path, file_name):

        rdfFile = file_path + file_name

        graph = rdflib.Graph()

        try:

            # graph.open("store", create=True)
            graph.parse(rdfFile, format="n3")

            print("graph has %s statements." % len(graph))

            # print out all the triples in the graph
            for subj, pred, obj in graph:

                if (subj, pred, obj) not in graph:
                    raise Exception("It better be!")

            # for stmt in graph:
            #   pprint.pprint(stmt)

            return graph
        except Exception as e:
            log.logger.error(e)

        return graph

    def test_virtuso(self):

        query = """
               INSERT IN GRAPH <http://mytest.org>
               {
               <#book1> <http://purl.org/dc/elements/1.1/title> "Fundamentals of Compiler Design" .
               }
               """

        # import rdflib

        store = sparqlstore.SPARQLUpdateStore(endpoint_rdf_store_url, virtuoso=True)
        gs = rdflib.ConjunctiveGraph(store)

        gs.open((endpoint_rdf_store_url, endpoint_rdf_store_url))
        gs1 = gs.get_context(rdflib.URIRef('http://localhost:8890/DAV'))
        gs1 = self.get_triples("", "test.ttl")
        gs1.update(query)

    def test_virt(self, g):

        query = """
        INSERT IN GRAPH <http://test.nidm.org>
        {
        %s
        }
        """ % g.rdf().serialize(format='nt')

        import requests
        session = requests.Session()
        session.headers = {'Accept': 'text/html'}  # HTML from SELECT queries
        data = {'query': query}
        result = session.post(endpoint_rdf_store_url, data=data)
        print result

    def test_virtuso(self, g):

        gs = rdflib.ConjunctiveGraph('SPARQLUpdateStore', identifier='http://fs.net/')
        gs.open((endpoint_rdf_store_url, endpoint_rdf_store_url))

        print ("OK - ")
        print("graph has %s statements." % len(g))
        count = 0
        for stmt in g:  # just add 1 statement
            print count
            pprint.pprint(stmt)
            gs.add(stmt)

            pprint.pprint(stmt)
            print ("OK - - Done!")
            count += 1

    def test_sparqlwrapper(self, g):

        # statement = ""
        sparql_insert = ""
        queryString_head = "INSERT DATA { GRAPH <http://example.com/> { \n"
        queryString_tail = "\n . } }"
        query_line = ""

        sparql = SPARQLWrapper(endpoint_rdf_store_url)

        print ("OK - ")
        print("graph has %s statements." % len(g))
        count = 0

        for s, p, o in g:
            query_line = ""
            sparql_insert = ""

            print (s, p, o)

            if type(s) == rdflib.term.URIRef:
                query_line += "<" + s + ">" + " "

            else:

                query_line += s + " "

            if type(p) == rdflib.term.URIRef:
                query_line += "<" + p + ">" + " "

            else:

                query_line += p + " "

            if type(o) == rdflib.URIRef:
                query_line += "<" + o + ">" + " "

            elif type(o) == rdflib.term.Literal:
                query_line += '"' + o + '"' + " "
            else:
                # TODO resolve datatype issue

                query_line += o + " "

            # print s, p , o
            # print (s, p, o)
            # if type(o) == rdflib.term.Literal:
            #    output.append(o.toPython())
            #    print output

            sparql_insert += prefixes
            sparql_insert += queryString_head
            sparql_insert += query_line
            sparql_insert += queryString_tail
            print sparql_insert

            # gs.add(stmt)

            # pprint.pprint(queryString)
            # print ("OK - - Done!")
            # count += 1

            sparql.setQuery(sparql_insert)
            sparql.method = 'POST'
            sparql.query()


"""
        for stmt in g:  # just add 1 statement
            #print count
            print stmt
            print(stmt[0])
            print(stmt[1])
            print(stmt[2])
            #if stmt[2][1]:
               # print stmt[2][1]

            if type(stmt[2]) == rdflib.term.Literal:
                print stmt[2].toPython()

"""
#
# test = RDFStoreAPI()
# # test.test_virtuso()
# # g = test.get_triples("","test.ttl")
# # test.test_virtuso()
# # test.test_virt(g)
# # test.test_virtuso(g)
# # test.test_sparqlwrapper(g)
#
# test.push_curl("", "test.ttl")
