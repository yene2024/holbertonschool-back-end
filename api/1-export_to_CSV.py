#!/usr/bin/python3
"""Returns to-do list information about an employee based on their ID."""
import csv
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

    # Write to-do list data to a CSV file named after the employee ID
    with open("{}.csv".format(argv[1]), "w", newline="") as csvfile:
        writeCSV = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # Write each task as a row in the CSV file
        [writeCSV.writerow([argv[1], username, i.get("completed"),
                            i.get("title")]) for i in to_do_list]
