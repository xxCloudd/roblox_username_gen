import requests
import time
import random
import json


length = int(input("Length -> "))
letters = input("Letters? Y/N -> ")
numbers = input("Numbers? Y/N -> ")
underscore = input("Underscore? Y/N -> ")

Characters = ""

if letters == "Y":
    Characters = Characters + "abcdefghijklmnopqrstuvwxyz"

if numbers == "Y":
    Characters = Characters + "0123456789"

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


def filtered(str):
    for swear_word in ["FCK","COCK","DICK","PENIS","FUCK","SHIT","CUM","ASS","SEX","ROBUX","BUX","MILF","FKK","FUX","GAY","DCK","KKK","FUK","FUC","455","69","420","88","18","6_9","1_8","8_8"]:
        if str.find(swear_word):
            return True

def getRandomStr():
    newStr = Characters[random.randint(len(Characters))-1]

    
    for i in range(length - 2):
        newStr = newStr + uCharacters[random.randint(len(uCharacters))-1]

    return newStr + Characters[random.randint(len(Characters))-1]


def getUser():
    theStr = getRandomStr()
    req = requests.get("https://api.roblox.com/users/get-by-username?username=" + theStr)
    load = json.loads(req)
    if load["Id"]:
        return theStr
    else:
        return False
        
while time.sleep(1):
    result = getUser()
    if result:
        print(result)