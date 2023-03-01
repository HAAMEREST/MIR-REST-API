# Imports
import requests
from time import sleep
import os
import schedule
import time as tm
import json
import tkinter


# Connect to MIR wifi automatically (??? mb not needed)
# scan available Wifi networks
def wifi():
 os.system('cmd /c "netsh wlan show networks"')
 # input Wifi name
 name_of_router = input('Enter Name/SSID of the Wifi Network you wish to connect to: ')
 # connect to the given wifi network
 os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')

 print("If you're not yet connected, try connecting to a previously connected SSID again!")




# Get  Request
ip = 'mir.com'
host = 'http://' + ip + '/api/v2.0.0/'

# Format Headers
headers = {}
headers['Content-Type'] = 'application/json'
headers['Authorization'] = 'Basic YWRtaW46OGM2OTc2ZTViNTQxMDQxNWJkZTkwOGJkNGRlZTE1ZGZiMTY3YTljODczZmM0YmI4YTgxZjZmMmFiNDQ4YTkxOA=='


def mis_mes():
    first_position = input('your first position name')

    while True:
        mission_message = requests.get(host + "/status")
        print(mission_message.text)

        text_list = json.loads(mission_message)
        c = {}

        for i in text_list:
            c[i['mission_text']] = i
        print(c)

        if c.get('mooving to ' + first_position):
            break



def main_api():
# Getting Mission Data
 get_missions = requests.get(host + 'missions', headers=headers)
 print(get_missions.text)  # // get missions guids

 list_missions = json.loads(get_missions)
 b = {}

 for i in list_missions:
    b[i['name']] = i
 print(b)


# If last action  is done then
# Delete All Missions In Queue
 delete_actions = requests.delete(host + 'mission_queue', headers=headers)
 print(delete_actions)

# Calling Charging Mission #Should be user input
 mission_id_1 = {"mission_id": "8aeff405-ad33-11ed-867c-f44d306ef9de"}
 charging_mission = requests.post(host + 'mission_queue', json=mission_id_1, headers=headers)
 print(charging_mission)
 sleep(15)  # // if delay is needed  // number in () is seconds

# Delete Charging Mission After Time #Should be same with calling mission
 mission_id_2 = mission_id_1
 delete_charging = requests.delete(host + 'mission_queue', json=mission_id_2, headers=headers)
 print(delete_charging)

# Calling Regular Mission Back #Should be user input
 mission_id_3 = {"mission_id": "71440438-ad33-11ed-867c-f44d306ef9de"}
 regular_mission = requests.post(host + 'mission_queue', json=mission_id_3, headers=headers)
 print(regular_mission)



#Setup time
scheduler = input('put your time here')
def timer():
    wifi()
    mis_mes()
    main_api()

    schedule.every().day.at(scheduler).do(timer)


    while True:
        schedule.run_pending()
        tm.sleep(1)