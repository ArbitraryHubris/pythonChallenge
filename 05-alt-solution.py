from urllib.request import Request, urlopen
import sys
import pickle
data = pickle.loads(urlopen(
    'http://www.pythonchallenge.com/pc/def/banner.p').read())
for line in data:
    for char, count in line:
        sys.stdout.write(char * count)
    sys.stdout.write("\n")
