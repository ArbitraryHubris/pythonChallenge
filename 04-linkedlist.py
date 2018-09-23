# http://www.pythonchallenge.com/pc/def/linkedlist.php

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def requestURL(req):
    try:
        response = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        return response