#!/usr/bin/python3
""" export data in CSV format """

import csv
import requests
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    USER_ID = argv[1]

    """ information user """
    user_response = requests.get(f"{API_URL}/users/{USER_ID}").json()

    """ to do list for the user """
    todo_response = requests.get(f"{API_URL}/todos?userId={USER_ID}").json()

    """ write to CSV file """
    with open(f"{USER_ID}.csv", mode='w') as csv_file:
        writter = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todo_response:
            writter.writerow([
                user_response['id'],
                user_response['username'],
                task['completed'],
                task['title']
            ])

        print(f"Data as been exported to {USER_ID}.csv")
