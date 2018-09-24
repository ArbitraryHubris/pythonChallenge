# http://www.pythonchallenge.com/pc/def/linkedlist.php

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import re


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

nothing='8022'
urlBase = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
for x in range(1,400):
    response = requestURL(urlBase + nothing)
    responseString = response.read().decode('utf-8')
    print(responseString)
    nothing = re.search('[0-9]+$',responseString).group()