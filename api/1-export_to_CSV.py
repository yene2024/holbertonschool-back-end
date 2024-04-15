#!/usr/bin/python3

import requests
import csv
from sys import argv, exit

if __name__ == "__main__":
    """
    Fetches the TODO list of an employee and exports it to a CSV file.

    The script accepts an integer as a parameter, which is the employee ID.
    It fetches the employee's TODO list and exports it to a CSV file.
    """

    # Ensure correct usage
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        exit(1)

    # Parse employee ID from command line arguments
    employee_id = int(argv[1])

    # Base URL for the JSONPlaceholder API
    base_url = 'https://jsonplaceholder.typicode.com'

    # URL to fetch user data using employee ID
    user_url = f'{base_url}/users/{employee_id}'

    # URL to fetch TODO list for the given employee ID
    todo_url = f'{base_url}/todos?userId={employee_id}'

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Extract employee name
    employee_name = user_data['username']

    # Fetch TODO list
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Prepare CSV file name
    csv_filename = f'{employee_id}.csv'

    # Write TODO list to CSV file
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME",
                         "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            writer.writerow([employee_id, employee_name,
                             task['completed'], task['title']])

    print(f"TODO list exported to {csv_filename}")
