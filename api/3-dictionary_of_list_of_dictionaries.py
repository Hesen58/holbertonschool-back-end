#!/usr/bin/python3
'''Something useful'''
import json
import requests

url = "https://jsonplaceholder.typicode.com"
rUsers = requests.get(f"{url}/users/").json()
res = {}

for i in rUsers:
    rTodos = requests.get(f"{url}/users/{i['id']}/todos").json()
    res[i['id']] = []
    for j in rTodos:
        res[i['id']].append({"task": j['title'],
                             "completed": j['completed'],
                             "username": i['username']})

with open("todo_all_employees.json", "w") as f:
    json.dump(res, f)
