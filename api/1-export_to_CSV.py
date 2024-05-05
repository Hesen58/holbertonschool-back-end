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
        w = csv.writer(f)
        for i in rTodos:
            w.writerow([userId, rUser['name'],
                        i['completed'], i['title']])
