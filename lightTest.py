import requests
import json
url = 'http://192.168.1.117/api/5020c25b696a73b540fbee2c7bcbde38/lights/1/'
response = requests.get(url).json()
print response
#response = response.json()
if(response["state"]["on"]):
	data = '{"on":false}'
else:
	data = '{"on":true, "sat":254, "bri":254,"hue":10000}'
response = requests.put(url+'state', data=data)
print response.json()
