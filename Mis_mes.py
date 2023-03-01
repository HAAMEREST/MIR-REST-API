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