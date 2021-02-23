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
    
    value = input("Enter 'c' to take a picture or 'v' to take 10 secs video, Type \"stop\" to exit:\n")
    
    if(value == "stop"):
        exit()
    
    if(value == "c"):
        x = datetime.datetime.now()
        picture = "/home/pi/Desktop/license"+str(x)+".jpeg"
        print('smile!')
        camera.start_preview()
        #sleep(5)
        camera.capture(picture, quality=30) #quality range 0-100
        camera.stop_preview()
        allpicslist.append(str(x))
        #print(allpicslist)
        
        url = "https://api.aiforthai.in.th/lpr-v2"
        payload = {'crop': '1', 'rotate': '1'}
        files = {'image': open(picture, 'rb')}
        headers = {
            'Apikey': "9fyO2hLVgXRem15kSZ86XVOC2fgJwcqR",
        }
        
        from PIL import Image
        im = Image.open(picture)
        #im = im.resize((620,480), Image.ANTIALIAS)
        images = np.array(im,dtype=np.uint8)

        response = requests.post(url, files=files, headers=headers)
        if response.status_code == 204:
            print("..")
            continue
        print(response.json())
        data = response.json()
        try:
            temp = data[0]
        except:
            print("can't recognize license plate")
            continue
        print(temp['lpr'])
        #for item in data:
        #    _object = (item['lpr'])
        #    xLeftTop = int(item['bbox']['xLeftTop'])
        #    yleftTop = int(item['bbox']['yLeftTop'])
        #    xRightBottom = int(item['bbox']['xRightBottom']) / 3
        #   yRightBottom = int(item['bbox']['yRightBottom']) / 3

        #    figure, get_axis = plot.subplots(1)
        #    get_axis.imshow(images)
        #   rect = patches.Rectangle((xLeftTop, yleftTop), xRightBottom, yRightBottom, linewidth=5, edgecolor='#7FFF00',
        #                            facecolor='none')
        #   get_axis.add_patch(rect)
        #   plot.text(xLeftTop, yleftTop - 50, _object, fontname='Carlito', fontsize='20', color='#7FFF00')
        #   plot.show()
        
        
    elif(value == "v"):
        print('smile!')
        x = datetime.datetime.now()
        filename = "/home/pi/Desktop/vid"+str(x)+".h264"
        camera.start_preview()
        camera.start_recording(filename)
        sleep(10)
        camera.stop_recording()
        camera.stop_preview()
    else:
        print("Please type 'c' or 'v'")





