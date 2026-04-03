#!/usr/bin/python3
"""Export employee TODO list to CSV format."""
import csv
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

    filename = "{}.csv".format(user_id)

    with open(filename, mode="w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

