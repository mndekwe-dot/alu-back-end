#!/usr/bin/python3
"""Gather data from an API and display employee TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get("{}/todos?userId={}".format(base_url, user_id)).json()

    name = user.get("name")
    done = [t for t in todos if t.get("completed")]
    total = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(name, len(done), total))
    for task in done:
        print("\t {}".format(task.get("title")))
