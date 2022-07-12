import requests
import keyboard as k
import time
import random
import threading
import os

print("made by bvthxry, press . to stop")
print()
multithreading = input("multithreading (y/n): ").upper()
length = input("length (5-20): ")
letters = input("letters (y/n): ").upper()
numbers = input("numbers (y/n): ").upper()
underscore = input("underscore (y/n): ").upper()
lowerOrUppercase = input("uppercase/lowercase (u/l): ").upper()

running = True

def onPress(key):
    global running
    if key.name == ".":
        running = False

k.on_press(onPress)

os.system("cls")

Characters = ""

if letters == "Y":
    Characters = Characters + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if numbers == "Y":
    Characters = Characters + "0123456789"

if lowerOrUppercase == "L":
    Characters = Characters.lower()

uCharacters = Characters

if underscore == "Y":
    uCharacters = uCharacters + "_"

if type(length) != "int" or (type(length) == "int" and int(length) < 5):
    length = 5
elif (type(length) == "int" and int(length) > 20):
    length = 20
    

cached_users = []

def isCached(Str):
    global cached_users
    if not Str in cached_users:
        cached_users.append(Str)
        return False
    else:
        return True

def is_filtered(str):
    for swear_word in ["FCK", "COCK", "DICK", "PENIS", "FUCK", "SHIT", "CUM", "ASS", "SEX", "ROBUX", "BUX", "MILF",
                       "FKK", "FUX", "GAY", "DCK", "KKK", "FUK", "FUC", "455", "69", "420", "88", "18", "6_9", "1_8",
                       "8_8"]:
        if (str.upper()).find(swear_word) != -1:
            return True


def getRandomStr():
    newString = Characters[random.randint(1, len(Characters)) - 1]

    for i in range(length - 2):
        if not newString.find("_") != -1:
            newString = newString + uCharacters[random.randint(1, len(uCharacters)) - 1]
        else:
            newString = newString + Characters[random.randint(1, len(Characters)) - 1]

    newString = newString + Characters[random.randint(1, len(Characters)) - 1]

    if is_filtered(newString) or isCached(newString):
        getRandomStr()
    else:
        return newString


def getUsers():
    users = []
    
    for _ in range(100):
        users.append(getRandomStr())
    
    req = requests.post("https://users.roblox.com/v1/usernames/users", {'usernames': users, 'excludeBannedUsers': True})

    if req.status_code == 200:
        loaded = req.json()

        for user in loaded["data"]:
            if user["name"].lower() == user["requestedUsername"].lower(): # exists
                users.remove(user["requestedUsername"])


    return users

iresults = 1

def Do():
    global iresults
    
    results = getUsers()

    if results:
        for user in results:
            if user != None:
                print(str(iresults)+":"+user)
                iresults += 1


while running:
    if multithreading == "Y":
        threading.Thread(target=Do).start()
    else:
        Do()
    time.sleep(.1)

print("\nstopped")
os.system("pause")
