import requests 

BASE = "http://127.0.0.1:5000/"

headers = {"Content-Type": "application/json; charset=utf-8"}


data = [{"name":"Suits clips", "likes":10, "views":1000000},
        {"name":"Cooking videos", "likes":10, "views":10000000},
        {"name":"Coding tutorials", "likes":10, "views":1}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), json = data[i], headers=headers)
    print(response.json())

input()
response = requests.get(BASE + "video/1")
print(response.json())
input()
response = requests.delete(BASE + "video/1")
print(response)
input()
response = requests.get(BASE + "video/1")
print(response)