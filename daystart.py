import random
import discord
import urllib.request
import string
import json
from random import choice
from datetime import date
from urllib.error import HTTPError


def game():
    filename = './quips/gamemsg.txt'
    with open(filename, 'r') as file:
        data = file.readlines()
    game = str(random.choice(data))
    return game


def getad():
    filename = './quips/adlist.txt'
    with open(filename, 'r') as file:
        data = file.readlines()
    ad = str(random.choice(data))
    return ad


def awake():
    filename = './quips/awakemsg.txt'
    with open(filename, 'r') as file:
        data = file.readlines()
    awake = str(random.choice(data))
    return awake


def activity():
    if random.randint(0, 1) == 1:

        return discord.Game(name=game())

    else:
        filename = './quips/flumvideos.txt'
        with open(filename, 'r') as file:
            data = file.readlines()

        return discord.Streaming(name=game(), url=str(random.choice(data)))


def days():
    today = date.today()
    start = today - date(2019, 2, 26)
    return int(start.days)


def datecheck():
    today = date.today()
    start = today - date(2019, 2, 26)

    with open("longtermdata.json", "r") as file:
        data = json.load(file)
    with open("userdata.json", "r") as file:
        userdata = json.load(file)
    # check if bot has restarted today already
    if int(start.days) == data['dayvalues']['days']:
        return 0

    # else check if new year is upon us
    if (int(start.days) % 365) == 0:
        data[0] = str(start.days) + '\n'
        with open("longtermdata.json", "w") as file:
            json.dump(data, file)
        return int(start.days)

    # else must be a new day so start new day proto-call
    else:
        data['dayvalues']['days'] = start.days
        data['dayvalues']['game'] = 'not set'
        data['dayvalues']['check-in'] = 'empty'
        for x in userdata:
            try:
                userdata[x]['status'] = 0
            except KeyError:
                userdata[x] = userdata[x]
                userdata[x]['status'] = 0
            if x == 'ratbuddy#9913' or x == 'Dunsparce#0080':
                userdata[x]['status'] = -1
        with open("userdata.json", "w") as file:
            json.dump(userdata, file)
        with open("longtermdata.json", "w") as file:
            json.dump(data, file)
        return 1


def link():
    opener = urllib.request.build_opener()
    opener.add_headers = [("User-agent", "Mozilla/5.0")]

    chars = string.ascii_letters + string.digits

    while True:

        imgPart = ''
        for i in range(5):
            imgPart += choice(chars)
        url = "http://i.imgur.com/" + imgPart

        try:
            opener.open(url)
            print(url)
            msg = "||" + url + "||"
            return msg
            if open:
                system("open " + url)
        except HTTPError:
            print("found one that don't work")
