# Imports
import requests
from time import sleep
import os
import schedule
import time as tm
import json
import tkinter

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
        check_status = {}

        for message in text_list:
            check_status[message['mission_text']] = message
        print(check_status)

        if check_status.get('mooving to ' + first_position):
            break

#{"joystick_low_speed_mode_enabled": false, "mission_queue_url": null, "mode_id": 7, "moved": 32490.318683002366, "mission_queue_id": null, "robot_name": "MiR_R411","mission_text": "Waiting for new missions...", "state_text": "Ready"}]



def main_api():
# Getting Mission Data
 get_missions = requests.get(host + 'missions', headers=headers)
 print(get_missions.text)  # // get missions guids

 list_missions = json.loads(get_missions)
 dict_missions = {}

 for mission in list_missions:
    dict_missions[mission['name']] = mission

 list_name_missions =dict_missions .keys()
 create_mission_1 = input()
 create_mission_2 = input()
 guid_1 = dict_missions[create_mission_1]['guid']
 guid_2 = dict_missions[create_mission_2]['guid']







# If last action  is done then
# Delete All Missions In Queue
 delete_actions = requests.delete(host + 'mission_queue', headers=headers)
 print(delete_actions)

# Calling Charging Mission #Should be user input
 mission_id_1 = dict_missions[create_mission_1]['guid']
 charging_mission = requests.post(host + 'mission_queue', json=mission_id_1, headers=headers)
 print(charging_mission)
 sleep(15)  # // if delay is needed  // number in () is seconds

# Delete Charging Mission After Time #Should be same with calling mission
 delete_charging = requests.delete(host + 'mission_queue', json=mission_id_1, headers=headers)
 print(delete_charging)

# Calling Regular Mission Back #Should be user input
 mission_id_2 = dict_missions[create_mission_2]['guid']
 regular_mission = requests.post(host + 'mission_queue', json=mission_id_2, headers=headers)
 print(regular_mission)