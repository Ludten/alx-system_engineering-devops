#!/usr/bin/python3
"""
A module that gathers data from an API and exports to JSON
format
"""

import json


def save_to_file(obj, id):
    """
    converts todo instances to their json representation
    and saves them as text files
    """
    j_obj = json.dumps(obj)
    with open("{}.json".format(id), 'w',
              encoding="utf-8") as f:
        f.write(j_obj)


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
        euname = name.json()['username']
        body = r.json()
        jlist = []
        for item in body:
            jdict = {}
            jdict['task'] = item['title']
            jdict['completed'] = item['completed']
            jdict['username'] = euname
            jlist.append(jdict)
        jsdict = {}
        jsdict['{}'.format(ident)] = jlist
        save_to_file(jsdict, ident)
    except Exception:
        pass
