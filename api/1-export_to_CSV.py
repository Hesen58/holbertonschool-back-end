#!/usr/bin/python3
'''Something useful'''
import csv
import requests
import sys


if len(sys.argv) == 2:
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    rUser = requests.get(f"{url}/users/{userId}")
    rTodos = requests.get(f"{url}/users/{userId}/todos")
    rUser = rUser.json()
    rTodos = rTodos.json()
    result = ""
    with open(f"{userId}.csv", "w") as f:
        for i in rTodos:
            result += (f"\"{userId}\",\"{rUser['username']}\"," +
            f"\"{i['completed']}\",\"{i['title']}\"\n")
        f.write(result)
