#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her task list progress
"""

import json
import requests
import sys

# Get the employee id from command line
employee_id = sys.argv[1]

# Get request to api for employee data
employee_data = requests.get(
    'https://jsonplaceholder.typicode.com/users/' + employee_id)

# Parse data as json
employee_data_json = employee_data.json()

# Get employee name from key name
employee_name = employee_data_json['name']

# Get request to api for todo data
todo_data = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)

# Parse data as json
todo_data_json = todo_data.json()

# Use len to calculate total number of tasks
total_todos = str(len(todo_data_json))

# Calculate completed tasks
completed_todos = str(sum(1 for task in todo_data_json if task['completed']))

# Print output with provided format
print("Employee " + employee_name + " is done with tasks(" +
      completed_todos + "/" + total_todos + "):")

# List completed tasks titles
for task in todo_data_json:
    if task['completed']:
        print('\t ' + task['title'])

# Check if the script is being run directly as the main program
if __name__ == '__main__':
    # Code inside this block will only run if this script is executed directly
    pass
