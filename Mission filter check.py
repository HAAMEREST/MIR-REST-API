# Imports
import requests
import json


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

list_missions = json.loads(get_missions)
b = {}

for i in list_missions:
    b[i['name']] = i
print(b)











#Bellow is the output i get in console, that gives GUIDs of the missions
#{"url": "/v2.0.0/missions/48dcfb99-a7b0-11ed-867c-f44d306ef9de", "guid": "48dcfb99-a7b0-11ed-867c-f44d306ef9de", "name": "Tudeng mission 2"}

# If i write it in the way bellow it doesnt work

#mission_name = {"mission_name": "Tudeng mission 2"}
#charging_mission = requests.post(host + 'mission_queue', json=mission_name, headers=headers)
#print(charging_mission)



# And this one works
mission_id_1 = {"mission_id": "48dcfb99-a7b0-11ed-867c-f44d306ef9de"}
charging_mission = requests.post(host + 'mission_queue', json=mission_id_1, headers=headers)
print(charging_mission)