#!/usr/bin/python3
"""Export all employees TODO list to JSON format."""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(base_url)).json()
    all_tasks = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        all_tasks[user_id] = []

        todos = requests.get("{}/todos?userId={}".format(base_url, user_id)).json()
        for task in todos:
            all_tasks[user_id].append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

    filename = "todo_all_employees.json"
    with open(filename, mode="w", encoding="utf-8") as jsonfile:
        json.dump(all_tasks, jsonfile)

