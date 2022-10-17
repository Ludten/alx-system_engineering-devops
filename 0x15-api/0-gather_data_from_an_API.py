#!/usr/bin/python3
"""
A module that gathers data from an API
"""

if __name__ == "__main__":
    import requests
    import sys

    ident = int(sys.argv[1])
    name = requests.get(
        'https://jsonplaceholder.typicode.com/users/{:d}'
        .format(ident))
    r = requests.get(
        'https://jsonplaceholder.typicode.com/users/{:d}/todos'
        .format(ident))
    try:
        ename = name.json()['name']
        body = r.json()
        donet = [items for items in body if items['completed'] is True]
        print('Employee {} is done with tasks({}/{}):'.format(
            ename, len(donet), len(body)))
        for task in donet:
            print('\t {}'.format(task['title']))
    except Exception:
        pass
