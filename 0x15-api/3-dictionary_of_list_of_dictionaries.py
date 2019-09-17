#!/usr/bin/python3
"""Module to connect to an api and grab data"""

import collections
import csv
import json
import requests
from sys import argv
import sys

if __name__ == "__main__":
    employeeRequest = requests.get(
        "https://jsonplaceholder.typicode.com/users/")
    employeeDict = employeeRequest.json()

    todoRequest = requests.get(
        "https://jsonplaceholder.typicode.com/todos")
    todoList = todoRequest.json()

    taskData = []
    jsonData = collections.OrderedDict()

    for person in employeeDict:
        for thing in todoList:
            if person.get("id") == thing.get("userId"):
                taskDict = {
                    "username": person.get("username"),
                    "task": thing.get("title"),
                    "completed": thing.get("completed"),}
                taskData.append(taskDict)
        jsonData["{}".format(person.get("id"))] = taskData
        taskData = []

    with open("todo_all_employees.json", "w") as people:
        json.dump(jsonData, people)
