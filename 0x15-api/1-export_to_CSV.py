#!/usr/bin/python3
"""import data from an api is csv format"""

import csv
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

    with open("{}.csv".format(argv[1]), "w") as task:
        taskWriter = csv.writer(
            task,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL)
        for dict in todoList:
            taskWriter.writerow([
                employeeDict.get("id"),
                employeeDict.get("username"),
                dict.get("completed"),
                dict.get("title")])
