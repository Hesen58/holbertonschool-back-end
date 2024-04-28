#!/usr/bin/python3
'''Something useful'''
import json
import requests
import sys

if len(sys.argv) == 2:
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    rUser = requests.get(f"{url}/users/{userId}")
    rTodos = requests.get(f"{url}/users/{userId}/todos")
    rUser = rUser.json()
    rTodos = rTodos.json()
    res = {f"{userId}": []}
    for i in rTodos:
        res[f"{userId}"].append({"task": i['title'],
                                  "completed": i['completed'],
                                  "username": rUser['username']})
    with open(f"{userId}.json", "w") as f:
        json.dump(res, f)
