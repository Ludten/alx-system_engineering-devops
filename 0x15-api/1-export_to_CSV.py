#!/usr/bin/python3
"""
A module that gathers data from an API and exports to csv
format
"""


def save_to_file_csv(list_objs, id):
    import csv
    """
        converts todo instances to their csv representation
        and saves them as text files
    """
    if list_objs is not None and list_objs != []:
        fieldname = []
        for keys in list_objs[0]:
            fieldname.append(keys)
        with open("{:d}.csv".format(id), 'w',
                  encoding="utf-8") as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=fieldname, quoting=csv.QUOTE_ALL)
            for dicts in list_objs:
                writer.writerow(dicts)
        # else:
        #     with open("{:d}.csv".format(id), 'w',
        #               encoding="utf-8") as f:
        #         f.write("")


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
        csvlist = []
        for item in body:
            csvdict = {}
            csvdict['USER_ID'] = item['userId']
            csvdict['USERNAME'] = euname
            csvdict['TASK_COMPLETED_STATUS'] = item['completed']
            csvdict['TASK_TITLE'] = item['title']
            csvlist.append(csvdict)
        save_to_file_csv(csvlist, ident)
    except Exception:
        pass
