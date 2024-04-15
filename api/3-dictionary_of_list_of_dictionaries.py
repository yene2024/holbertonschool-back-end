#!/usr/bin/python3

import json
import requests

employee_data = requests.get('https://jsonplaceholder.typicode.com/users')
employee_data_json = employee_data.json()

all_tasks = {}

for user in employee_data_json:
    user_id = str(user['id'])
    user_name = user['username']
    todo_data = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' + user_id)
    todo_data_json = todo_data.json()
    task_list = [
        {
            'username': user_name,
            'task': task['title'],
            'completed': task['completed']
        } for task in todo_data_json]
    all_tasks[user_id] = task_list

with open('todo_all_employees.json', 'w') as jsonfile:
    json.dump(all_tasks, jsonfile)

if __name__ == '__main__':
    pass
