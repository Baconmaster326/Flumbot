import random
import discord
import urllib.request
import string
from googleapiclient.discovery import build
from random import choice
from datetime import date
from random_word import RandomWords
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
    if (random.randint(0,1) == 1):
    
        return discord.Game(name = game())
    
    else:
        filename = './quips/flumvideos.txt'
        with open(filename, 'r') as file:
            data = file.readlines()

        return discord.Streaming(name = game(), url = str(random.choice(data)))

def days():
    today = date.today()
    start = today - date(2019, 2, 26)
    return int(start.days)

def datecheck():
    today = date.today()
    start  = today - date(2019, 2, 26)
    
    filename = "longtermdata.txt"
    with open(filename, 'r') as file:
        data = file.readlines()
    if (int(start.days) == int((data[0].strip('\n')))):
        return 0
    
    if ((int(start.days)%365) == 0):
        data[0] = str(start.days) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        return int(start.days)
    
    else:
        data[11] = '0\n'
        data[12] = '0\n'
        data[13] = '0\n'
        data[14] = 'not set\n'
        data[15] = 'empty\n'
        data[0] = str(start.days) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        return 1

def link():
    selector = ((random.randint(0,100)) % 2)

    if (selector == 0):
        #if len(argv) > 1:
                #open = True

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
                        
    else:
        r = RandomWords()
        searchterm = r.get_random_word()
        print(searchterm)
        DEVELOPER_KEY = 'AIzaSyD7x3CwhZKtXsR1xr9xJON77qFmyog_ATY'
        YOUTUBE_API_SERVICE_NAME = 'youtube'
        YOUTUBE_API_VERSION = 'v3'

        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

        search_response = youtube.search().list( q= str(searchterm), videoDuration = 'short', part='snippet', type = 'video', maxResults=5).execute()

        videos = []

        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                videos.append('%s' % (search_result['id']['videoId']))
                
        link = "https://www.youtube.com/watch?v=" + str(videos[random.randint(0, 2)])
        link = "||" + link + "||"
        return link
    

