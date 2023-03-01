#Setup Crontab
# ??? Probably not needed anymore

# Imports
import requests
from time import sleep
import os
from threading import Thread
import datetime
import schedule
from datetime import time,timedelta,datetime
import time as tm

# Connect to MIR wifi automatically (??? mb not needed)
# scan available Wifi networks
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

# Getting Mission Message
#while True:
     #do_something()
     #if condition  ():
        #break or pass

def mis_mes():
    mission_message = requests.get(host + "/status")
    print(mission_message.text)


schedule.every().second.do(mis_mes)

while True:
    schedule.run_pending()
    tm.sleep(1)


#mission_message = requests.get(host + "/status")
#print(mission_message.text)
# Need to loop mission_message function to get updated info every x time
# If mission_text = 'moving to pos 1 '
# Change robot state to continue, if it is paused
# And then start the main part

#Trying to get time using REST API, not crontab or windows task sheduler
get_distance = requests.get(host+ '/Distance_statistics', headers = headers)
print(get_distance.text)

#OR
get_path = requests.get(host+ '/Path', headers = headers)
print(get_path.text)

#OR PutStatus  datetime optional





#MB Schedule script with Python
def check_api():
    # ... your code here ...
    pass

def schedule_api():
    while datetime.datetime.now().minute % 5 != 0:
        sleep(1)
    check_api()
    while True:
        sleep(300)
        check_api()

thread = Thread(target=schedule_api)
thread.start()



def main_api():
# Getting Mission Data
 get_missions = requests.get(host + 'missions', headers=headers)
 print(get_missions.text)  # // get missions guids

# Sort by name not guid ( we can try to use mission_name instead of mission_id)
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