import datetime
import datetime
import schedule
import time
import urllib
from datetime import timedelta


class TimeOperations(object):
    def encode(self, URL):
        URI_encoded = urllib.quote_plus(URL)
        #   print URI_encoded
        return URI_encoded

    def decode(self, URL):
        URI_decoded = urllib.unquote(URL)
        #   print URI_encoded
        return URI_decoded

    # get yesterday time
    def getTimeFromEncoded(self):

        # print encode(time_from)

        # print decode(time_from)

        # print time_from
        # print datetime.datetime.now().replace(microsecond=0).isoformat()
        # print self.encode(datetime.datetime.now().replace(microsecond=0).isoformat())

        yesterday = datetime.datetime.now() - timedelta(days=1)
        # yesterday.strftime('%m%d%y')

        print yesterday

        # print self.encode(yesterday.replace(microsecond=0).isoformat())
        # @TODO uncomment second line if initial download -- to get all the data since 2010
        time_from = self.encode(yesterday.replace(microsecond=0).isoformat())
        # time_from = "2010-01-01T00%3A00%3A00Z"

        print time_from

        return time_from

    # get today time
    def getTimeToEncoded(self):
        time_to = "time%3E=2017-06-07T00%3A00%3A00Z"

        # print encode(time_from)

        # print decode(time_from)

        # print time_to
        # print datetime.datetime.now().replace(microsecond=0).isoformat()
        # print self.encode(datetime.datetime.now().replace(microsecond=0).isoformat())

        today = datetime.datetime.now()
        # today.strftime('%m%d%y')

        print today

        # print self.encode(today.replace(microsecond=0).isoformat())

        time_to = self.encode(today.replace(microsecond=0).isoformat())

        print time_to

        return time_to

    def getTimeFrom(self):

        # print encode(time_from)

        # print decode(time_from)

        # print time_from

        yesterday = datetime.datetime.now() - timedelta(days=1)
        # yesterday.strftime('%m%d%y')

        # print yesterday

        # @TODO uncomment second line if initial download -- to get all the data since 2010
        time_from = yesterday.replace(microsecond=0).isoformat()
        # time_from = "2010-01-01T00%3A00%3A00Z"

        print time_from
        return time_from

    def getTimeTo(self):
        time_to = "time%3E=2017-06-07T00%3A00%3A00Z"

        # print encode(time_from)

        # print decode(time_from)

        # print time_to
        # print datetime.datetime.now().replace(microsecond=0).isoformat()
        # print self.encode(datetime.datetime.now().replace(microsecond=0).isoformat())

        today = datetime.datetime.now()
        # today.strftime('%m%d%y')

        print today

        # print self.encode(today.replace(microsecond=0).isoformat())

        time_to = self.encode(today.replace(microsecond=0).isoformat())

        print self.decode(time_to)

        return self.decode(time_to)


if __name__ == "__main__":
    test = TimeOperations()
    # test.getTimeToEncoded()
    # test.getTimeTo()
    test.getTimeFrom()
    test.getTimeFromEncoded()
