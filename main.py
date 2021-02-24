import numpy as np
import json
import matplotlib.pyplot as plot
import matplotlib.patches as patches
import requests

from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()
camera.rotation = 90

allpicslist = []

picture = ""

while(True):
    
    value = input("Enter 'c' to take a picture, Type \"stop\" to exit:\n")
    
    if(value == "stop"):
        exit()
    
    if(value == "c"):
        x = datetime.datetime.now()
        picture = "/home/pi/Desktop/license"+str(x)+".jpeg"
        print('smile!')
        camera.start_preview()
        sleep(5)
        camera.capture(picture, quality=30) #quality range 0-100
        camera.stop_preview()
        allpicslist.append(str(x))
        #print(allpicslist)
        
        #url = "https://api.aiforthai.in.th/lpr-v2"
        url = "https://api.aiforthai.in.th/panyapradit-lpr"
        #payload = {'crop': '1', 'rotate': '1'}
        files = {'file': open(picture, 'rb')}
        headers = {
            'Apikey': "9fyO2hLVgXRem15kSZ86XVOC2fgJwcqR",
        }
        
       

        response = requests.post(url, files=files, headers=headers)
        if response.status_code == 204:
            print("..")
            continue
        
        try:
            data = response.json()
            #print(data)
            r_char = data['r_char']
            r_digit = data['r_digit'].lstrip("0")
            r_province = data['r_province']
            print(r_char,r_digit,r_province)
            
        except:
            print("can't recognize license plate")
            continue
        #print(temp['lpr'])
        #print(temp['recognition'])
        
        
        
    else:
        print("Please type 'c' or 'v'")






