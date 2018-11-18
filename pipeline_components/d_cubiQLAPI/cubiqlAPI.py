
# communicate with django cube consumer to retrive josn-pivot-druid ready format





class cubiqlAPI(object):

    def __init__(self, ):
        print 'get data from cubiql'

    def getLatestData(self, startDate, EndDate):

        # communicate with cube consumer - or cubiql directlty to get latest observatins in json format - ready for druid and pivot.js
        print 'start getting data from django'

