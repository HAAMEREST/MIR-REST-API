# Imports
import requests
from time import sleep
import os
from threading import Thread
import datetime
import schedule
from datetime import time,timedelta,datetime
import time as tm
import json

# Get  Request
ip = 'mir.com'
host = 'http://' + ip + '/api/v2.0.0/'

# Format Headers
headers = {}
headers['Content-Type'] = 'application/json'
headers['Authorization'] = 'Basic dHVkZW5nOmQ2NmQ4MDJiNjQ5NDkxMjY3Njk5NTU1MGUxNGY3MzQ5NGNjYzIxZmJiZWVjOGZiMThhM2RlMGU3YjQwMjNjYzY='

def mis_mes():
    mis_mes()
    first_position = "käru test_1"

    while True:
        mission_message = requests.get(host + "/status")
        print(mission_message.text)

        text_list = json.loads(mission_message.content)
        c = {}

        for i in text_list:
            c[i['mission_text']] = i
        print(c)

        if c.get('mooving to' + first_position):
            break


get_missions = requests.get(host + 'missions', headers=headers)
print(get_missions.text)  # // get missions guids

mission_id_1 = {"mission_id": "mirconst-guid-0000-0004-actionlist00"}
charging_mission = requests.post(host + 'mission_queue', json=mission_id_1, headers=headers)
print(charging_mission)

