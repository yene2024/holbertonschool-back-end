#!/usr/bin/python3

import json
import requests
import sys

# Get the employee ID from command-line arguments
employee_id = sys.argv[1]

# Fetch employee data from the API
employee_data = requests.get('https://jsonplaceholder.typicode.com/users/'
                             + employee_id)
employee_data_json = employee_data.json()

# Extract employee name from the retrieved JSON
employee_name = employee_data_json['name']

# Fetch to-do list data for the employee from the API
todo_data = requests.get('https://jsonplaceholder.typicode.com/todos?userId='
                         + employee_id)
todo_data_json = todo_data.json()

# Calculate total and completed tasks
total_todos = str(len(todo_data_json))
completed_todos = str(sum(1 for task in todo_data_json if task['completed']))

# Print employee's name and task completion status
print("Employee " + employee_name + " is done with tasks(" +
      completed_todos + "/" + total_todos + "):")

# Print titles of completed tasks
for task in todo_data_json:
    if task['completed']:
        print('\t ' + task['title'])

if __name__ == '__main__':
    pass
