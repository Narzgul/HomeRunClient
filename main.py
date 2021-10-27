import requests
from datetime import datetime
import gpx

url = "http://localhost:1337/api"
path = './gpx_tests/test_run_api.gpx'   # Path to the .gpx file
distance = gpx.get_distance(path)
ele_pos = gpx.get_elevation(path, positive=True)    # Positive elevation (=up)
ele_neg = gpx.get_elevation(path, positive=False)   # Negative elevation (=down)

files = {
    'title' : "API test tour 2",
    'date': str(datetime.utcnow()),
    'distance': str(distance),
    'ele_pos': str(ele_pos),
    'ele_neg': str(ele_neg),
    'file': open(path, 'r')
}
 
r = requests.post(url, files=files)
print(r)