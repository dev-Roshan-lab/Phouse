from firebase import firebase
import pyautogui as pg
import io
from PIL import ImageGrab
import base64
import cv2
import json
firebase = firebase.FirebaseApplication("https://server-65459.firebaseio.com/", None)


pg.FAILSAFE = True
#while True:
while True:
    buffer = io.BytesIO()
    img = ImageGrab.grab()
    img.save(buffer, format='PNG')
    img.close()
    
    b64_str = base64.b64encode(buffer.getvalue())
    #print(b64_str)
    #b64_str[2:]
    #print(b64_str)
    image = b64_str.decode()
    firebase.put('/airmouse/data','image', image)
    print("Updated")
    data = firebase.get('/airmouse/data', '')
    mouse = data["dir"]
    
    if mouse == "topleft":
        #print("Left")
        pg.moveRel(-10, -10)
    elif mouse == "downright":
        #print("Right")
        pg.moveRel(10, 10)
    elif mouse == "downleft":
        pg.moveRel(-10, 10)
    elif mouse == "topright":
        pg.moveRel(10, -10)
    else :
        print("Null")
    
    print("done")  