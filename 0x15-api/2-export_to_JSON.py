#!/usr/bin/python3
"""grab data from an api and export to JSON"""

import csv
import json
import requests
from sys import argv
import sys

if __name__ == "__main__":
    employeeRequest = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + argv[1])
    employeeDict = employeeRequest.json()

    todoRequest = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1])
    todoList = todoRequest.json()

    taskData = []
    taskDict = {}

    for thing in todoList:
        taskDict = {
            "task": thing.get("title"),
            "completed": thing.get("completed"),
            "username": employeeDict.get("username"),
        }
        taskData.append(taskDict)

    jsonData = {argv[1]: taskData}

    with open("{}.json".format(argv[1]), "w") as emp:
        json.dump(jsonData, emp)
