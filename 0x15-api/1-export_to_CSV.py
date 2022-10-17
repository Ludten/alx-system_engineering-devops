#!/usr/bin/python3
"""
A module that gathers data from an API and exports to csv
format
"""


if __name__ == "__main__":
    import requests
    import sys
    import csv

    ident = int(sys.argv[1])
    name = requests.get(
        'https://jsonplaceholder.typicode.com/users/{:d}'
        .format(ident))
    r = requests.get(
        'https://jsonplaceholder.typicode.com/users/{:d}/todos'
        .format(ident))
    try:
        euname = name.json()['username']
        body = r.json()
        with open("{:d}.csv".format(ident), 'w',
                  encoding="utf-8") as csvfile:
            writer = csv.writer(
                csvfile, quoting=csv.QUOTE_ALL)
            for item in body:
                writer.writerow([item['userId'], euname, item['completed'],
                                item['title']])
    except Exception:
        pass
