import urllib3


class Encode:


    def encode (self,URl):
        URl_encoded = urllib3.quote_plus(URl)
        #   print URI_encoded
        return URl_encoded