#!/usr/bin/python3
"""Returns to-do list information about an employee based on their ID."""
import json
from requests import get
from sys import argv

if __name__ == '__main__':
    # Base URL for the JSONPlaceholder API
    APIurl = "https://jsonplaceholder.typicode.com"

    # Fetch employee data and to-do list from the API
    employee = get(APIurl + "/users/{}".format(argv[1])).json()
    to_do_list = get(APIurl + "/todos", params={"userId": argv[1]}).json()

    # Extract the username of the employee
    username = employee.get("username")

    # Write to-do list data to a JSON file named after the employee ID
    with open("{}.json".format(argv[1]), "w") as jsonfile:
        json.dump({argv[1]: [
            {
                "task": i.get("title"),
                "completed": i.get("completed"),
                "username": username
            } for i in to_do_list]}, jsonfile)
