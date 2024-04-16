#!/usr/bin/python3
""" using this REST API in CSV format"""
import json
import requests
from sys import argv


API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    USER_ID = argv[1]

    """ check user's informations """
    user_response = requests.get(f"{API_URL}/users/{USER_ID}").json()

    """ check user's to do list """
    todo_response = requests.get(f"{API_URL}/todos?userId={USER_ID}").json()

    """ export data in json file """
    data = {
        USER_ID: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_response['username']
            }
            for task in todo_response
        ]
    }

    """ write to json file """
    with open(f"{USER_ID}.json", mode='w') as json_file:
        json.dump(data, json_file)

    print(f"Data as been exported to {USER_ID}.json")
