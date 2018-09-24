# http://www.pythonchallenge.com/pc/def/peak.html
# use pickle to deserialize the banner.p linked in the source
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import pickle


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


response = requestURL('http://www.pythonchallenge.com/pc/def/banner.p')
banner = pickle.load(response)
for line in banner:
    lineString=''
    for character in line:
        for x in range(0, character[1]):
            lineString+=character[0]
    print(lineString)
print('end')


