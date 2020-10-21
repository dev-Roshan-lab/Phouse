from firebase import firebase # firebase library
import pyautogui as pg #for controlling
import io # used for converting screenshots to json serializable string
from PIL import ImageGrab #takes the screenshot
import base64 # encoding screeshots to base64
firebase = firebase.FirebaseApplication("__FB REALTIME DATABASE URL__", None) # Connect to the db


pg.FAILSAFE = True # Obviously you dont want your Device to GO mad
while True:
    # Take Screenshot and convert them to json serializable string so that you can update in the Realtime DB
    buffer = io.BytesIO()
    img = ImageGrab.grab()
    img.save(buffer, format='PNG')
    img.close()
    # encode the base64 string
    b64_str = base64.b64encode(buffer.getvalue())
    # Decode to make it json serializable
    image = b64_str.decode()
    # put() to update 
    firebase.put('/airmouse/data','image', image)
    print("Updated")
    # get() to revieve the data from db
    data = firebase.get('/airmouse/data', '')
    # save the key "dir" data for moving the mouse
    mouse = data["dir"]
    # move the mouse based on how the user rotates the phone 
    # the coordinates are obviously incorrect wrt to string "mouse", it is wer to the mobile !
    if mouse == "topleft":
        pg.moveRel(-10, -10)
    elif mouse == "downright":
        pg.moveRel(10, 10)
    elif mouse == "downleft":
        pg.moveRel(-10, 10)
    elif mouse == "topright":
        pg.moveRel(10, -10)
    else :
        print("Null")
    # First Cycle Completed
    print("done")  
