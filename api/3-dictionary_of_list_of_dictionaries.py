#!/usr/bin/python3
"""Export all employees TODO list data to JSON format."""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    data = {}
    for user in users:
        uid = str(user.get("id"))
        username = user.get("username")
        data[uid] = [
            {
                "username": username,
                "task": t.get("title"),
                "completed": t.get("completed")
            } for t in todos if t.get("userId") == user.get("id")
        ]

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
