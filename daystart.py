import json
import os
import random
import shutil
import string
import urllib.request
from datetime import date
from random import choice
from PIL import Image
from urllib.error import HTTPError

import discord
import requests


def game():
    quips = './bin/en_data/quips.json'
    with open(quips, "r") as file:
        line = json.load(file)
    game = str(random.choice(line['gamemsg']))
    return game


def getad():
    quips = './bin/en_data/quips.json'
    with open(quips, "r") as file:
        line = json.load(file)
    ad = str(random.choice(line['adlinks']))
    return ad


def awake():
    quips = './bin/en_data/quips.json'
    with open(quips, "r") as file:
        line = json.load(file)
    awake = str(random.choice(line['startmsg']))
    return awake


def activity():
    quips = './bin/en_data/quips.json'
    with open(quips, "r") as file:
        line = json.load(file)
    if random.randint(0, 100) > 75:
        return discord.Game(name=game())
    else:
        return discord.Streaming(name=game(), url=str(random.choice(line['ytlinks'])))


def days():
    today = date.today()
    start = today - date(2019, 2, 26)
    return int(start.days)


def datecheck():
    today = date.today()
    start = today - date(2019, 2, 26)
    filename = './bin/en_data/userdata.json'
    altfilename = './bin/en_data/longtermdata.json'
    with open(altfilename, "r") as file:
        data = json.load(file)
    with open(filename, "r") as file:
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
        with open(filename, "w") as file:
            json.dump(userdata, file)
        with open(altfilename, "w") as file:
            json.dump(data, file)
        return 1


async def profile(client):
    if random.randint(1, 100) > 10:
        selector = random.randint(0, 1)
        with open('./Pics/big' + str(selector) + '.png', 'rb') as f:
            await client.edit_profile(avatar=f.read())
        return
    else:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/78.0.3904.108 Safari/537.36 '
        }
        currentDir = os.getcwd()
        path = currentDir  # saving images to Images folder
        url = 'https://www.thispersondoesnotexist.com/image'
        attempts = 0
        while attempts < 5:  # retry 5 times
            try:
                filename = 'image.jpg'
                r = requests.get(url, headers=headers, stream=True, timeout=5)
                if r.status_code == 200:
                    with open(os.path.join(path, filename), 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                break
            except Exception as e:
                attempts += 1
                print(e)
        image = Image.open('image.jpg')
        width, height = image.size
        image = image.crop(((width/4), ((height/4)+50), (3*width/4), ((3*height/4)+100)))
        image.save('image.jpg')
        with open('image.jpg', 'rb') as f:
            await client.user.edit(avatar=f.read())
        os.remove('image.jpg')


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
