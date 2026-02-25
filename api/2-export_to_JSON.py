#!/usr/bin/python3
"""Export employee TODO list to JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    username = user.get("username")

    todos = requests.get(
        "{}/todos?userId={}".format(base_url, user_id)
    ).json()

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {user_id: tasks}
    filename = "{}.json".format(user_id)

    with open(filename, mode="w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)

