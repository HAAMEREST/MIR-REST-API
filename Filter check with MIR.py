# Imports
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
headers['Authorization'] = 'Basic dHVkZW5nOmQ2NmQ4MDJiNjQ5NDkxMjY3Njk5NTU1MGUxNGY3MzQ5NGNjYzIxZmJiZWVjOGZiMThhM2RlMGU3YjQwMjNjYzY='


def main_api():
# Getting Mission Data
 get_missions = requests.get(host + 'missions', headers=headers)
 print(get_missions.text)  # // get missions guids

 list_missions = json.loads(get_missions.content)
 dict_missions = {}

 for mission in list_missions:
  dict_missions[mission['name']] = mission

 list_name_missions =dict_missions .keys()
 create_mission_1 = input('enter your charging mission name here :')
 create_mission_2 = input('enter your regular mission name here :')
 guid_1 = dict_missions[create_mission_1]['guid']
 guid_2 = dict_missions[create_mission_2]['guid']

 guid_id_1 = json.loads(guid_1.content)
 guid_id_2 = json.loads(guid_2.content)



# If last action  is done then
# Delete All Missions In Queue
 #delete_actions = requests.delete(host + 'mission_queue', headers=headers)
 #print(delete_actions)

# Calling Charging Mission #Should be user input
 mission_id_1 = guid_id_1
 charging_mission = requests.post(host + 'mission_queue', json=mission_id_1, headers=headers)
 print(charging_mission)
 sleep(150)  # // if delay is needed  // number in () is seconds

# Delete Charging Mission After Time #Should be same with calling mission
 #delete_charging = requests.delete(host + 'mission_queue', json=mission_id_1, headers=headers)
 #print(delete_charging)

# Calling Regular Mission Back #Should be user input
 mission_id_2 = guid_id_2
 regular_mission = requests.post(host + 'mission_queue', json=mission_id_2, headers=headers)
 print(regular_mission)

main_api()


#400 Argument error or Missing content type application/json on the
#header or Bad request or Invalid JSON

#204 The element has been deleted successfully