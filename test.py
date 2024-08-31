import requests

BASEURL = "http://127.0.0.1:5000/"

response = requests.get(BASEURL + "helloworld")
print (response.json())

response = requests.post(BASEURL + "helloworld")
print (response.json())
