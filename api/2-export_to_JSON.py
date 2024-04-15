#!/usr/bin/python3

import json
import requests
import sys

employee_id = sys.argv[1]

employee_data = requests.get('https://jsonplaceholder.typicode.com/users/' +
                             employee_id)
employee_data_json = employee_data.json()

employee_username = employee_data_json['username']

todo_data = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                         employee_id)
todo_data_json = todo_data.json()

total_todos = str(len(todo_data_json))
completed_todos = str(sum(1 for task in todo_data_json if task['completed']))

with open(f'{employee_id}.json', 'w') as jsonfile:
    json.dump({employee_id: [
        {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_username
        } for task in todo_data_json]}, jsonfile)
