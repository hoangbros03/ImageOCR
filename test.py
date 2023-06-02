# import requests

# BASE = "http://127.0.0.1:8000/"

# data=[{"name":"ratok", "likes":100, "view":2},
#       {"name":"rato", "likes":1000, "view":3},
#       {"name":"rat", "likes":10000, "view":4}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), json = data[i])
#     print(response.json())

# input()
# response = requests.get(BASE + "video/6")
# print(response.json())

# import os
# print(os.path.abspath("../src/main.py"))