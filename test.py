import requests

BASEURL = "http://127.0.0.1:5000/"

#response = requests.get(BASEURL + "helloworld/mike")
#print (response.json())

#response = requests.post(BASEURL + "helloworld")
#print (response.json())

#response = requests.patch(BASEURL + "dogs/1", {"name":"Tazzy", "age":3})
#print (response)



response = requests.put(BASEURL + "dogs/1", {"name":"Tazzy", "age":5, "breed":"bulldog"})
#response = requests.put(BASEURL + "dogs/2", {"name":"Tazzy2", "age":6, "breed":"spaniel"})
#response = requests.put(BASEURL + "dogs/3", {"name":"Tazzy3", "age":7, "breed":"terrier"})
#response = requests.put(BASEURL + "dogs/4", {"name":"Tazzy4", "age":8, "breed":"Collie"})
#response = requests.put(BASEURL + "dogs/5", {"name":"Tazzy5", "age":1, "breed":"husky"})
#print (response.json())


#response = requests.delete(BASEURL + "dogs/1")
#print (response)



response = requests.get(BASEURL + "dogs/1")
print (response.json())
#response = requests.get(BASEURL + "dogs/2")
#print (response.json())
#response = requests.get(BASEURL + "dogs/3")
#print (response.json())
#response = requests.get(BASEURL + "dogs/6")
#print (response.json())
#response = requests.delete(BASEURL + "dogs/1")
#print (response)
#response = requests.get (BASEURL + "dogs/1")
#print (response.json())


