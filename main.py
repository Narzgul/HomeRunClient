import requests
from datetime import datetime

url1 = "http://localhost:1337/api"
url2 = "http://localhost:1337/api/file"
my_json = {'title': "API test tour", 'date': str(datetime.utcnow())}
my_files = {'document': open('./gpx_tests/test_run.gpx', 'rb')}

response1 = requests.post(url=url1, json=my_json)
response2 = requests.post(url=url2, files=my_files)

print(response1)
print(response2)