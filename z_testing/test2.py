
def encode (URL):
    URI_encoded = urllib.quote_plus(URL)
    #   print URI_encoded
    return URI_encoded

def decode (URL):
    URI_decoded = urllib.unquote(URL)
    #   print URI_encoded
    return URI_decoded


#print encode(time_from)

#print decode(time_from)

import datetime
from datetime import timedelta

print time_from
print datetime.datetime.now().replace(microsecond=0).isoformat()
print encode(datetime.datetime.now().replace(microsecond=0).isoformat())

yesterday = datetime.datetime.now() - timedelta(days=1)
yesterday.strftime('%m%d%y')

print yesterday

print encode(yesterday.replace(microsecond=0).isoformat())

