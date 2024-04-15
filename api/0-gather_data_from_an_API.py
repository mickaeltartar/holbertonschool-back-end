#!/usr/bin/python3
""" using this REST API """

import requests
from sys import argv


API_URL = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':

    """ check user's informations """
    user_response = requests.get(f"{API_URL}/users/{argv[1]}")
    user_data = user_response.json()

    """ check user's to do list """
    todo_response = requests.get(f"{API_URL}/todos?userId={argv[1]}")
    todo_data = todo_response.json()

    """ filter for task completed """
    completed_task = [task for task in todo_data if task['completed']]

    """ display progression """
    employee_name = user_data["name"]
    num_task_completed = len(completed_task)
    total_task = len(todo_data)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_task_completed, total_task))

    for task in completed_task:
        print(f"\t {task['title']}")
