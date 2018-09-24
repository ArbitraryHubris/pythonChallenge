# http://www.pythonchallenge.com/pc/def/linkedlist.php

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def requestURL(req):
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        return response


response = requestURL(
    'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
print(response)

