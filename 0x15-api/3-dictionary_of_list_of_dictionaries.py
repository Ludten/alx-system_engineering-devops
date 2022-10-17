#!/usr/bin/python3
"""
A module that gathers data from an API and exports to JSON
format
"""

import json


def save_to_file(obj):
    """
    converts todo instances to their json representation
    and saves them as text files
    """
    j_obj = json.dumps(obj)
    with open("todo_all_employees.json", 'w',
              encoding="utf-8") as f:
        f.write(j_obj)


if __name__ == "__main__":
    import requests

    name = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    try:
        body = name.json()
        jsdict = {}
        for item in body:
            user_id = item['id']
            r = requests.get(
                'https://jsonplaceholder.typicode.com/users/{:d}/todos'
                .format(user_id)).json()
            jlist = []
            for task in r:
                jdict = {}
                jdict['username'] = item['username']
                jdict['task'] = task['title']
                jdict['completed'] = task['completed']
                jlist.append(jdict)
            jsdict['{}'.format(user_id)] = jlist
        save_to_file(jsdict)
    except Exception:
        pass
