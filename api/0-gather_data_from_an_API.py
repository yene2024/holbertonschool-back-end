#!/usr/bin/python3

import json
import requests
import sys

employee_id = sys.argv[1]

employee_data = requests.get('https://jsonplaceholder.typicode.com/users/' + employee_id)
employee_data_json = employee_data.json()

employee_name = employee_data_json['name']

todo_data = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)
todo_data_json = todo_data.json()

total_todos = str(len(todo_data_json))
completed_todos = str(sum(1 for task in todo_data_json if task ['completed']))

print("Employee " + employee_name + " is done with tasks(" +
      completed_todos + "/" + total_todos + "):")

for task in todo_data_json:
      if task['completed']:
            print('\t ' + task['title'])

if __name__ == '__main__':
    pass
