#! /usr/local/bin/python3

import pyautogui
import time
import random
from directkeys import PressKey, ReleaseKey, dk

g_application = True
g_dungeon = False
g_dungeonLobby = False

#Scan screen for enter dungeon button

def checkEnterButton():
    global g_dungeonLobby
    yesButtonLocation = pyautogui.locateOnScreen('./static/images/yesbutton3.png', confidence=0.9)
    print ("Checking if button exists: {name}".format(name=yesButtonLocation))
    if yesButtonLocation != None:
        randomNumber2 = random.randint(0,2)
        time.sleep(randomNumber2)   
        PressKey(dk['RETURN'])
        time.sleep(.25)
        ReleaseKey(dk['RETURN'])
        g_dungeonLobby = not g_dungeonLobby        
    else:
        print ("COULD NOT FIND YES BUTTON") 
        return
#Check if portal is opened

def checkDungeonPortal():
    global g_dungeonLobby
    dungeonName = pyautogui.locateOnScreen('./static/images/dungeon2.png', confidence=0.9)
    randomnumber1 = random.randint(1,3)   
    print ("Checking if inside the dungeon lobby: {name}".format(name=dungeonName))
    if dungeonName != None:
        PressKey(dk['RIGHT'])
        time.sleep(1.5)
        ReleaseKey(dk['RIGHT'])
        time.sleep(randomnumber1)
        PressKey(dk['GRAVE'])
        time.sleep(0.75)
        ReleaseKey(dk['GRAVE'])
        while (g_dungeonLobby):
            checkIfInDungeon()
            

def checkIfInDungeon():
    global g_dungeonLobby
    global g_dungeon
    while (g_dungeonLobby):
        PressKey(dk['GRAVE'])
        time.sleep(0.75)
        ReleaseKey(dk['GRAVE'])
        time.sleep(0.25)
        dungeonCheck = pyautogui.locateOnScreen('./static/images/inthedungeon8.png', confidence=0.9)
        print ("Checking if inside dungeon: {name}".format(name=dungeonCheck))
        if dungeonCheck != None:
            g_dungeonLobby = not g_dungeonLobby
            g_dungeon = not g_dungeon
            while (g_dungeon):
                checkForSuccess()


def checkForSuccess():
    global g_dungeon
    while (g_dungeon):
        successCheck = pyautogui.locateOnScreen('./static/images/success2.png', confidence=0.9)
        print ("Checking if success image is avaiable: {name} ".format(name=successCheck))
        if successCheck != None:
            g_dungeon = not g_dungeon
            PressKey(dk["F12"])
            time.sleep(0.5)
            ReleaseKey(dk["F12"])
            time.sleep(1)
            PressKey(dk['RETURN'])
            time.sleep(.25)
            ReleaseKey(dk['RETURN'])
            
            



def autoDungeon():
    global g_dungeon
    global g_dungeonLobby   
    while not g_dungeon and not g_dungeonLobby:
        checkEnterButton()
    while (g_dungeonLobby):
        checkDungeonPortal()


def fullApplication():
    global g_application
    while g_application:
        autoDungeon()    
            

if __name__ == '__main__':
    time.sleep(1)
    fullApplication()
    #checkIfInDungeon()
    #checkEnterButton()
    #checkDungeonPortal()
    #checkForSuccess()
    #Press Enter Key if Dungeon Dialog exists
    
