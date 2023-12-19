#!/usr/bin/python3
""" script to export data in the JSON format."""
import json
import requests

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    """ user information """
    user_response = requests.get(f"{API_URL}/users/").json()

    """ todo list for the given user """
    todo_response = requests.get(f"{API_URL}/todos").json()

    """ create dictionnary for task users """
    task_user = {}
    for task in todo_response:
        user_id = task['userId']
        if user_id is not task_user:
            task_user[user_id] = []
            task_user[user_id].append({
                "task": task['title'],
                "completed": task['completed'],
                "username": next(user['username']
                                 for user in user_response
                                 if user['id'] == user_id)
            })

    """ to json file """
    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(task_user, json_file)
