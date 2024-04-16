#!/usr/bin/python3
"""
Python script to export data in the JSON format
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

# Get employee username from key username
employee_username = employee_data_json['username']

# Get request to api for todo data
todo_data = requests.get(
     'https://jsonplaceholder.typicode.com/todos?userId=' + employee_id)

# Parse data as json
todo_data_json = todo_data.json()

# Open a JSON file with the name based on the employee ID and write the data
with open(f'{employee_id}.json', 'w') as jsonfile:
    # Dump a dictionary with employee ID as key and a list of tasks as value
    json.dump({employee_id: [
        {
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_username
        } for task in todo_data_json]}, jsonfile)

# Check if the script is being run directly as the main program
if __name__ == '__main__':
    # Code inside this block will only run if this script is executed directly
    pass
