import requests 

BASE = "http://127.0.0.1:5000/"




data = [{"video_name":"Suits clips", "video_likes":10, "video_views":1000000},
        {"video_name":"Cooking videos", "video_likes":10, "video_views":10000000},
        {"video_name":"Coding tutorials", "video_likes":10, "video_views":1}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), json = data[i])
    print(response)

input()
response = requests.get(BASE + "video/1")
print(response.json())
