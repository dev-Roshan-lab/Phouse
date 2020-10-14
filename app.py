#importing important libraries
from firebase import firebase
import pyautogui as pg

#set up your firebase 
firebase = firebase.FirebaseApplication("https://server-65459.firebaseio.com/", None)
phno = input("Enter your Phone Number : ")# you obviously dont want me to control ur device, so phone number is unique hence you read only your data that is stored and updated under only your number

pg.FAILSAFE = True #just in case if ur device go wild!
while True:
    data = firebase.get('/airmouse/'+phno+'/'+phno+'/', '')#data sorce 
    mouse = data["z"]#check the key "z"
    #dont worry about the (x, y) of pyautogui of course they are wrong corresponding to the labels 
    if mouse == "topright":
        pg.moveRel(-10, -10)
    elif mouse == "downleft":
        pg.moveRel(10, 10)
    elif mouse == "downright":
        pg.moveRel(-10, 10)
    elif mouse == "topleft":
        pg.moveRel(10, -10)
    else :
        print("Null")
 
