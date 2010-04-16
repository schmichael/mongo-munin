
import urllib
import urllib2
import sys

try:
    import json
except ImportError:
    import simplejson as json


def getServerStatus(params=None):
    url = "http://127.0.0.1:28017/_status"
    if params:
        url += "?%s" % urllib.urlencode(params)
    return json.load(urllib2.urlopen(url))["serverStatus"]
