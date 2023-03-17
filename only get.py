import requests
from time import sleep
import os
import schedule
import time as tm
import json
import tkinter

# Get  Request
ip = 'mir.com'
host = 'http://' + ip + '/api/v2.0.0/'

# Format Headers
headers = {}
headers['Content-Type'] = 'application/json'
headers['Authorization'] = 'Basic YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='


get_missions = requests.get(host + 'missions', headers=headers)
print(get_missions.text)  # // get missions guids

mission_id_1 = {"mission_id": "0ff51cfe-a7b0-11ed-867c-f44d306ef9de"}
charging_mission = requests.post(host + 'mission_queue', json=mission_id_1, headers=headers)
print(charging_mission)

#missions/71440438-ad33-11ed-867c-f44d306ef9de



#Output
