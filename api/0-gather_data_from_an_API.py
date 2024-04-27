#!/usr/bin/python3
'''Somehing useful'''
import requests
import sys


if len(sys.argv) == 2:
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    ruser = requests.get(f"{url}/users/{userId}")
    rtodos = requests.get(f"{url}/users/{userId}/todos")
    ruser = ruser.json()
    rtodos = rtodos.json()
    total = len(rtodos)
    true = 0
    zor = ""

    for i in rtodos:
        if i['completed'] is True:
            zor += f"\t {i['title']}\n"
            true += 1

    print(f"Employee {ruser['name']} is done with tasks({true}/{total}):")
    print(f"{zor}", end="")
