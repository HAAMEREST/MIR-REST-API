# Imports
import requests, json
from time import sleep

# Get  Request
ip = 'mir.com'
host = 'http://' + ip + '/api/v2.0.0/'

# Format Headers
headers = {}
headers['Content-Type'] = 'application/json'
headers['Authorization'] = 'Basic YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='

# Getting Mission Data
get_missions = requests.get(host + 'missions', headers=headers)
print(get_missions.text)  # // get missions guids

# Delete All Missions In Queue
delete_actions = requests.delete(host + 'mission_queue', headers=headers)
print(delete_actions)

# Calling Charging Mission
mission_id = {"mission_id": "0c9226f4-eb14-11ec-8cd1-94c691a73491"}
charging_mission = requests.post(host + 'mission_queue', json=mission_id, headers=headers)
print(charging_mission)
sleep(15)  # // if delay is needed  // number in () is seconds

# Delete Charging Mission After Time
mission_id = {"mission_id": "0c9226f4-eb14-11ec-8cd1-94c691a73491"}
delete_charging = requests.delete(host + 'mission_queue', json=mission_id, headers=headers)
print(delete_charging)

# Calling Regular Mission
mission_id = {"mission_id": "430e5abe-ec84-11ec-b1a4-94c691a73491"}
regular_mission = requests.post(host + 'mission_queue', json=mission_id, headers=headers)
print(regular_mission)