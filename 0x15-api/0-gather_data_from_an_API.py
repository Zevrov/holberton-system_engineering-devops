#!/usr/bin/python3
"""pulls todo from a given employee id"""

import requests
from sys import argv


if __name__ == "__main__":
    employeeRequest = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + argv[1])
    employeeDict = employeeRequest.json()

    todoRequest = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1])
    todoList = todoRequest.json()

    employeeName = employeeDict.get("name")
    numberOfTasks = len(todoList)
    completedTasks = [
        dict for dict in todoList if dict.get("completed") is True]

    print('Employee {} is done with tasks({}/{}):'.format(
        employeeName,
        len(completedTasks),
        numberOfTasks))

    for completeTask in completedTasks:
        print("\t {}".format(completeTask.get("title")))
