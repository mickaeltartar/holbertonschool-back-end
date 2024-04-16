#!/usr/bin/python3
""" Script to export data in json format for all employees """

import json
import requests
from sys import argv


API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':

    """ check user's informations """
    user_response = requests.get(f"{API_URL}/users/").json()

    """ check user's to do list """
    todo_response = requests.get(f"{API_URL}/todos").json()

    """ export data in json format """
    data = {}
    for task in todo_response:
        user_id = task['userId']
        if user_id not in data:
            data[user_id] = []
        data[user_id].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": next(user[
                'username'] for user in user_response
                if user['id'] == user_id)
        })

    """ write to json file """
    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(data, json_file)
