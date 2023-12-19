#!/usr/bin/python3
""" script to export data in the JSON format """
import json
import requests

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    """ user information """
    user_response = requests.get(f"{API_URL}/users/").json()

    """ todo list for the given user """
    todo_response = requests.get(f"{API_URL}/todos").json()

    """ create dictionary of tasks grouped by user"""
    task_by_user = {}
    for task in todo_response:
        user_id = task['userId']
        if user_id not in task_by_user:
            task_by_user[user_id] = []
        task_by_user[user_id].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": next(user[
                'username'] for user in user_response if user['id'] == user_id)
        })

    """ Write to JSON file """
    with open("todo_all_employees.json", mode='w') as json_file:
        json.dump(task_by_user, json_file)