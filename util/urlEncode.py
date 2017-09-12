import urllib


class EncodeDecode:



    def encode(self, URL):
        URI_encoded = urllib.quote_plus(URL)
        #   print URI_encoded
        return URI_encoded

    def decode(self, URL):
        URI_decoded = urllib.unquote(URL)
        #   print URI_encoded
        return URI_decoded