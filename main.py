import requests
import time
import random
import threading

multithreading = input("Multithreading? Y/N -> ").upper()
length = int(input("Length -> "))
letters = input("Letters? Y/N -> ").upper()
numbers = input("Numbers? Y/N -> ").upper()
underscore = input("Underscore? Y/N -> ").upper()
lowerOrUppercase = input("Uppercase/Lowercase? U/L -> ").upper()

Characters = ""

if letters == "Y":
    Characters = Characters + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if numbers == "Y":
    Characters = Characters + "0123456789"

if lowerOrUppercase == "L":
    Characters = Characters.lower()

uCharacters = Characters

if underscore:
    uCharacters = uCharacters + "_"

if underscore == "Y":
    underscore = True
else:
    underscore = False

if not length or length < 5:
    length = 5
elif length > 20:
    length = 20


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

    if is_filtered(newString):
        getRandomStr()
    else:
        return newString


def getUser():
    theStr = getRandomStr()
    req = requests.post("https://users.roblox.com/v1/usernames/users", {'usernames': [theStr]})

    if req.status_code == 200:
        load = req.json()

        if len(load["data"]) == 0:
            return theStr
        else:
            return False


def Do():
    result = getUser()
    if result:
        print(result)


while True:
    if multithreading == "Y":
        threading.Thread(target=Do).start()
    else:
        Do()
    time.sleep(.1)