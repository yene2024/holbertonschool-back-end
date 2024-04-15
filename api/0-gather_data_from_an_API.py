#!/usr/bin/python3

import requests
import sys


def fetch_todo_progress(employee_id):
    """
    Fetches and displays the progress of an employee's TODO list.

    The function prints the employee's name, the number of completed tasks,
    and the total number of tasks, followed by the titles of completed tasks.
    """

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
    employee_name = user_data['name']

    # Fetch TODO list
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Count completed tasks
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    # Print progress
    print(f"Employee {employee_name} is done with tasks
          ({completed_tasks}/{total_tasks}): ")
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    # Ensure correct usage
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Parse employee ID from command line arguments
    employee_id = int(sys.argv[1])

    # Fetch and display TODO list progress
    fetch_todo_progress(employee_id)
