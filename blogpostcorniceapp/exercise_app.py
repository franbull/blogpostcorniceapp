"""
A script to run to exercise the web application.
TODO: better as automated tests.
"""
import simplejson as json

import requests

task = {
    'name': 'take_out_the_trash',
    'description': ("empty the trashcan and put the bag in the outside trashcan, "
        "don't forget to put a new bag in!"),
    }

if __name__ == '__main__':
    # demonstrate that there are no tasks, then one is added, then the same cannot
    # be added because a Task with that name exists, and there's a good error
    # message.
    response = requests.get('http://localhost:6543/tasks')
    print response.status_code, response.text
    response = requests.post('http://localhost:6543/tasks', json.dumps(task))
    print response.status_code, response.text
    response = requests.post('http://localhost:6543/tasks', json.dumps(task))
    print response.status_code, response.text
