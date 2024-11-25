import json
from urllib import response
from urllib.request import urlopen

url='http://ipinfo.io/json'

response=urlopen(url)
data=json.load(response)
print(data)
print(f"sir You are in {data.get('city')} {data.get('region')}")
