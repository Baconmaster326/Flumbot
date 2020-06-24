from __future__ import unicode_literals
from random_word import RandomWords
import discord
import ffmpeg
import asyncio
import random
import time
import os
import string
import librosa
import urllib.request
import datetime
import re
import youtube_dl
import shutil
import daystart
import messager
import voicememe
from gtts import gTTS
from googleapiclient.discovery import build
from itertools import cycle
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
from sys import argv
from os import system
from urllib.error import HTTPError
from random import choice
from datetime import date
#import big_smoke#
#import mad marc#

today = date.today()
now = datetime.datetime.now()
token = 'gamer'
client = commands.Bot(command_prefix = '', case_insensitive = True, )
x = 0
pilot = 0
username = 'urmum'
data = []
winners = []
cheaters = []
answer = ':a:'


#Things flumbot does on startup
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    presence = ['']
    await client.change_presence(activity = daystart.activity())     
    channel = client.get_channel(137921870010777600)
    deltaday = daystart.days()


    if(daystart.datecheck() == 0):
        print('already spammed chat today do not send wake message')
        return
    if((deltaday%365) == 0):
        x = deltaday
        days = deltaday
        while (x != 0):
            await asyncio.sleep(2)
            msg = "HAPPY FLUM YEAR\nGIVE IT UP FOR " + str(deltaday/365) + " YEAR(s) OF FLUMBOT!!!\n"
            #await channel.send(msg,tts=True)
            print('wrong')
            x -= 1

    msg = daystart.awake()
    await channel.send(msg)
    
    msg = "Give it up for Day " + str(deltaday) + "! Day " + str(deltaday) + "!"
    await channel.send(msg)
    
    await channel.send(daystart.link())

#if anyone deletes a message do this I'll have no hidden messages from me
@client.event
async def on_message_delete(message):
    author = str(message.author)
    content = str(message.content)
    msg = 'Ladies and gentlemen, ' + '@' + author + " said, " + \
               content + ", which they promptly deleted. Making them tonight's biggest loser"
    await message.channel.send(msg)

@client.event
async def on_typing(channel,user,when):
    name = str(user)
    name = name[:-5]
    def check(m):
        return user == user
    try:
        await client.wait_for('message', check = check, timeout=5)
    except asyncio.TimeoutError:
        msg = "finish typing " + name + ", we are all waiting :)"
        await channel.send(msg)
    return

@client.event
async def on_reaction_add(reaction, user):
    global winners
    global answer
    global cheaters
    print(user)
    if (str(user) in winners or str(user) in cheaters):
        print(str(user) + ' already answered')
        return
    if (str(user) == 'Flumbot#1927'):
        return
    if (answer == reaction.emoji):
        if(str(user) == 'BOOF#4284'):
            winners.append(str(user))
        if(str(user) == 'ratbuddy#9913'):
            winners.append(str(user))
        if(str(user) == 'ShadowXII#7240'):
            winners.append(str(user))
        if(str(user) == 'Baconmaster#3725'):
            winners.append(str(user))
        else:
            winners.append(str(user))
        return
    cheaters.append(str(user))
        

@client.event
async def on_message(message):
    print("reading message")
    if message.author == client.user:
        return
    global thank
    messagetobot = str(message.content)
    splitme = str(messagetobot.lower())
    betcheck = splitme.split()
    global username
    username = str(message.author)
    username = username[:-5]
    print(username)

    msg,flag = messager.check(splitme)
    if (msg != 'oop'):
        await message.channel.send(msg, tts = flag)

    #Do you have a clear vision?
    if ('i see') in messagetobot.lower():
        await message.channel.send(file=discord.File('./Pics/doyou.png'))
        await asyncio.sleep(5)
        await message.channel.send(file=discord.File('./Pics/hedo.png'))

    #never forget when :b: was standard
    if ('b-time') in messagetobot.lower():
        msg = 'Its :b:o time'
        frythis = 'b'
        await message.channel.send(msg)# tts=True)
        if frythis in messagetobot:
            msg = messagetobot
            msg2 = msg.replace('b',':b:')
            await message.channel.send(msg2)# tts=True)
        

    if ('trigger self destruct flumbot code 8675309') in messagetobot.lower():
        msg = '\n Type cancel to cancel the self destruct! \n'
        await message.channel.send(msg, tts=True)
        msg = ':rage: :100: :ok_hand:'
        global x
        x = 1
        while x > 0:
            await message.channel.send(msg, tts=True)
            x += 1

    print("No specific phrases said, proceed to read commands")
    await client.process_commands(message)


        

    ###################################
    #End Text commands                #
    #Proceed to complex voice commands#
    ###################################

    
@client.command(pass_context=True, name = 'football', help ='The new John Madden game sounds pretty good.')
@commands.cooldown(1,10,commands.BucketType.user)
async def football(ctx, *args):    
    msg = "HI EVERYONE AND WELCOME TO JOHN MADDEN FOOTBALL!!!"
    await ctx.send(msg)
    cliplocation = './Clips/Futbol.mp3'
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'MidiMania', help ='The hit new game hosted by yours truly')
@commands.cooldown(1,10,commands.BucketType.user)
async def MidiMania(ctx, *args):
    global cheaters
    cheaters.clear()
    global answer
    answer,printable = await voicememe.midimania(ctx,client)
    await asyncio.sleep(30)
    global winners
    await voicememe.winnerlist(ctx,client,winners,printable,20)
    winners.clear()
    return



@client.command(pass_context=True, name = 'MidiManiaDX', help ='You may have conquered regular midimania, but can you do midimania deluxe???')
@commands.cooldown(1,10,commands.BucketType.user)
async def MidiManiaDX(ctx, *args):
    global cheaters
    cheaters.clear()
    global answer
    answer,printable = await voicememe.midimaniadx(ctx,client)
    await asyncio.sleep(30)
    global winners
    await voicememe.winnerlist(ctx,client,winners,printable,35)
    winners.clear()
    return


@client.command(pass_context=True, name = 'bruh', help ='For the bruh moments in our lives')
@commands.cooldown(1,10,commands.BucketType.user)
async def bruh(ctx, *args):
    cliplocation = './Clips/bruh.mp3'
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'baba', help ='Meaty Chairs and Baba Yetus')
@commands.cooldown(1,10,commands.BucketType.user)
async def baba(ctx, *args):
    cliplocation = './Clips/babayeet.mp3'
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'thomas', help ='Thomas coming through')
@commands.cooldown(1,10,commands.BucketType.user)
async def thomas(ctx, *args):
    cliplocation = './Clips/thomas.mp3'
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'fridge', help ='Classico Flumico')
@commands.cooldown(1,10,commands.BucketType.user)
async def fridge(ctx, *args):
    cliplocation = './Clips/oof.mp3'
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'clap', help ='clap')
@commands.cooldown(1,10,commands.BucketType.user)
async def clap(ctx, *args):
    cliplocation = './Clips/clap.mp3'
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'keyboard', help ='I hear a keyboard round here')
@commands.cooldown(1,10,commands.BucketType.user)
async def keyboard(ctx, *args):
    cliplocation = './Clips/keyboard.mp3'
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'chum', help ='Gnot for the weak of heart')
@commands.cooldown(1,10,commands.BucketType.user)
async def chum(ctx, *args):
    msg = ":tired_face: You've been gnomed! :tired_face:"
    await ctx.send(msg)
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'knock', help ='Who is it? MonkaS')
@commands.cooldown(1,10,commands.BucketType.user)
async def knock(ctx, *args):
    cliplocation = './Clips/knock.mp3'
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'cocaine', help ='I am Impotent Rage')
@commands.cooldown(1,10,commands.BucketType.user)
async def cocaine(ctx, *args):
    msg = "Okay Mr.Phillips"
    await ctx.send(msg)
    cliplocation = './Clips/trevor.mp3'
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'futbol', help ='A modern spin on a classic clip')
@commands.cooldown(1,10,commands.BucketType.user)
async def futbol(ctx, *args):
    msg = "HI EVERYONE AND WELCOME TO JOHN MADDEN FOOT!"
    await ctx.send(msg)
    cliplocation = './Clips/fut.mp3'
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'gamble', help ='House always wins')
@commands.cooldown(1,10,commands.BucketType.user)
async def gamble(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/!gamble/')))
    cliplocation = './Clips/!gamble/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'spongebob', help ='You gotta lick the Marble')
@commands.cooldown(1,10,commands.BucketType.user)
async def spongebob(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/spongebob/')))
    cliplocation = './Clips/spongebob/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'alexjones', help ='Alex Jones screams about walruses')
@commands.cooldown(1,10,commands.BucketType.user)
async def alexjones(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/alexjones/')))
    cliplocation = './Clips/alexjones/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'ramsay', help ='Gordon Ramsay enlightens the chat')
@commands.cooldown(1,10,commands.BucketType.user)
async def ramsay(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/ramsay/')))
    cliplocation = './Clips/ramsay/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'gleib', help ='This is your Idiotest')
@commands.cooldown(1,10,commands.BucketType.user)
async def gleib(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/gleib/')))
    cliplocation = './Clips/gleib/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)
    
@client.command(pass_context=True, name = 'bigsmoke', help ='Big Smoke gets Philisophical')
@commands.cooldown(1,10,commands.BucketType.user)
async def bigsmoke(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/bigsmoke/')))
    cliplocation = './Clips/bigsmoke/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'prequel', help ='wut')
@commands.cooldown(1,10,commands.BucketType.user)
async def bigsmoke(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/prequel/')))
    cliplocation = './Clips/prequel/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'meme', help ='The biggest collection of memes since gamble')
@commands.cooldown(1,10,commands.BucketType.user)
async def meme(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/meme/')))
    cliplocation = './Clips/meme/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'agent', help ='Agent 14 tells you what to do')
@commands.cooldown(1,10,commands.BucketType.user)
async def agent(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/agent14/')))
    cliplocation = './Clips/agent14/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'trevor', help ='Trevor...Phillips...Industries...')
@commands.cooldown(1,10,commands.BucketType.user)
async def trevor(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/trevor/')))
    cliplocation = './Clips/trevor/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'lester', help ='Because we do not hear Lester enough')
@commands.cooldown(1,10,commands.BucketType.user)
async def lester(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/lester/')))
    cliplocation = './Clips/lester/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'joke', help ='Biggest Laughs')
@commands.cooldown(1,10,commands.BucketType.user)
async def joke(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/bonzi/')))
    cliplocation = './Clips/bonzi/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'IASIP', help ='Trashman comes to eat garbage')
@commands.cooldown(1,10,commands.BucketType.user)
async def IASIP(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/IASIP/')))
    cliplocation = './Clips/IASIP/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'trump', help ='We gotta build the wall')
@commands.cooldown(1,10,commands.BucketType.user)
async def trump(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/trump/')))
    cliplocation = './Clips/trump/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)
    
@client.command(pass_context=True, name = 'got', help ='BOBBY B to our rescue')
@commands.cooldown(1,10,commands.BucketType.user)
async def got(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/got/')))
    cliplocation = './Clips/got/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'fact', help ='Bonzi knows so much')
@commands.cooldown(1,10,commands.BucketType.user)
async def fact(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/facts/')))
    cliplocation = './Clips/fact/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'wwe', help ='HULK HOGAN')
@commands.cooldown(1,10,commands.BucketType.user)
async def wwe(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/wwe/')))
    cliplocation = './Clips/wwe/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True, name = 'sports', help ='NICE ON!')
@commands.cooldown(1,10,commands.BucketType.user)
async def sports(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/sports/')))
    cliplocation = './Clips/sports/' + person
    await voicememe.playclip(cliplocation,ctx,client,0)

@client.command(pass_context=True)
@commands.cooldown(1,10,commands.BucketType.user)
async def surprise(ctx, *args):
    if len(argv) > 1:
            open = True

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
                    msg = url
                    await ctx.send(url)
                    return
                    if open:
                            system("open " + url)
            except HTTPError:
                    print("found one that don't work")

@client.command(pass_context=True, name = 'miracle' , help ='autopilot just got 10 times better')
@commands.cooldown(1,10,commands.BucketType.user)
async def miracle(ctx, *args):
    #remove current list of mp3 files if leftovers exist
    file_list = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f)) and f.endswith('.mp3')]
    while (len(file_list) != 0):
        os.remove(str(random.choice(file_list)))
        file_list = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f)) and f.endswith('.mp3')]
        print(file_list)
        print('removing mess')
    #do miracle    
    r = RandomWords()
    global pilot
    pilot = 1
    timer = 0
    msg = 'I Bless the Rains down in Africa'
    await ctx.send(msg)
    while (pilot == 1):
        if (timer > 1500):
            timer = 0
        await asyncio.sleep(timer)
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

        channel = client.get_channel(509879962346586122)
        await channel.send(link)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

        file_list = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f)) and f.endswith('.mp3')]

        songsource = str(file_list[0])
        cliplocation = songsource
        duration = librosa.get_duration(filename=cliplocation)
        duration += 1
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        source = FFmpegPCMAudio(cliplocation)
        source = discord.PCMVolumeTransformer(source)
        source.volume = 1.5
        player = voice.play(source)
        await asyncio.sleep(duration)
        player = voice.stop()
        await ctx.voice_client.disconnect()
        timer = timer + random.randint(30, 100)
        print ('waiting ' + str(timer) + ' seconds before next clip')
        os.remove(songsource)
  
@client.command(pass_context=True, name = 'autopilot', help ='Let flumbot gamble his life away')
@commands.cooldown(1,10,commands.BucketType.user)
async def autopilot(ctx, *args):
    global pilot
    pilot = 1
    timer = 0
    msg = 'AutoPilot engaged, to turn off type "off"'
    await ctx.send(msg)
    while (pilot == 1):
        if (timer > 1500):
            timer = 0
        await asyncio.sleep(timer)
        person = str(random.choice(os.listdir('./Clips/!gamble/')))
        cliplocation = './Clips/!gamble/' + person
        await voicememe.playclip(cliplocation,ctx,client,0)
        timer = timer + random.randint(30, 100)
        print ('waiting ' + str(timer) + ' seconds before next clip')

@client.command(pass_context=True, name = 'revelation' , help ='Generate random youtube video')
@commands.cooldown(1,10,commands.BucketType.user)
async def revelation(ctx, *args):
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

    await ctx.send(link)

@client.command(pass_context=True, name = 'tts' , help ='For the blind or those without a second monitor')
@commands.cooldown(1,10,commands.BucketType.user)
async def tts(ctx, *args):
    global pilot
    global data
    global username
    pilot = 1
    os.remove('text.mp3')
    while(pilot !=0):
        if (data == 'null' or data == 'tts'):
            await asyncio.sleep(1)
            continue
        text = username + ' said... ' + str(data)
        langlist = ['en-ca']
        language = random.choice(langlist)
        speech = gTTS(text = text, lang = language, slow = False)
        speech.save("text.mp3")
        cliplocation = 'text.mp3'
        duration = librosa.get_duration(filename=cliplocation)
        duration += 1
        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        source = FFmpegPCMAudio(cliplocation)
        source = discord.PCMVolumeTransformer(source)
        source.volume = 1.5
        player = voice.play(source)
        await asyncio.sleep(duration)
        player = voice.stop()
        await ctx.voice_client.disconnect()
        os.remove('text.mp3')
        data = 'null'

@client.command(pass_context=True, name = 'restart' , help ='kill flumbot only to make him stronger')
@commands.cooldown(1,10,commands.BucketType.user)
async def restart(ctx, *args):
    os.startfile('restart.py')
    exit()

@client.command(pass_context=True, name = '8-ball' , help ='let flumbot make the decisions now')
@commands.cooldown(1,10,commands.BucketType.user)
async def ball(ctx, *args):
    chance = int(random.randrange(0,1000))
    msg = "Let me think on what you have told me"
    await ctx.send(msg, tts = True)
    await asyncio.sleep(4)
    msg = ":thinking:"
    
    if (chance == 69):
        print('it happened')
        msg = "give me a couple hours to contemplate the results"
        await ctx.send(msg, tts = True)
        time.sleep(10800)
        guess = ['yes', 'no', 'poop', 'penile fracture', 'was somebody who was 4 wrote this code']
        msg = random.choice(guess)
        await ctx.send(msg, tts = True)
        
    else:
        await ctx.send(msg, tts = True)
        await asyncio.sleep(6)
        wager = ['It would be wise to persue other ventures', 'History does not side with you', 'no lol', 'I reccomend you dab', 'You do you', "Just don't steal a tree",\
             "The future looks bright", "It is unlikely", "Pray on it", "Ask marc", "Ask rat", "Ask niche", "Ask yourself", "best @everyone with your question",\
             "yes", "the future you seek has already happened", "marc said he will do it for you", "only t-dubs will know the answer to your question", "Ask again", "It is certain", \
             "It is decidedly so", "Most likely", "Meh", "Signs point to yes", "Without a doubt", "Outlook good", "Outlook not so good", "You may rely on it", "Cannot predict now", \
             "Just die", "I prescribe a midimania to heal", "Maybe think on it a few days", "Rome wasn't built in a day", "The day of reckoning is approaching", "help me"\
             "Fo Sure", "Nah", "I don't feel like it", "behind you is the answer you seek"]
        msg = random.choice(wager)   
        await ctx.send(msg, tts = True)
        
@client.command(pass_context=True, name = 'music' , help ='lo-fi hiphop beats to relax/study to')
@commands.cooldown(1,10,commands.BucketType.user)
async def music(ctx, *args):
    global pilot
    pilot = 1
    while (pilot == 1):
        person = str(random.choice(os.listdir('./Clips/MIDI/')))
        cliplocation = './Clips/MIDI/' + person
        await voicememe.playclip(cliplocation,ctx,client,0)
        await asyncio.sleep(2)
        print('waited, playing next song')

@client.command(pass_context=True, name = 'inventory' , help ='checkout your cool stuff')
@commands.cooldown(1,10,commands.BucketType.user)
async def inventory(ctx, *args):
    user = str(ctx.message.author)
    filename = "longtermdata.txt"

    with open(filename, 'r') as file:
        data = file.readlines()

    if(user == 'Baconmaster#3725'):
        embed = discord.Embed(title = "Baconmaster's Inventory", colour = discord.Colour.from_rgb(255,0,255))
        money = data[2].strip('\n')
        a = int(data[7])
    if(user == 'BOOF#4284'):
        embed = discord.Embed(title = "BOOF's Inventory", colour = discord.Colour.from_rgb(0,0,0))
        money = data[3].strip('\n')
        a = int(data[8])
    if(user == 'ratbuddy#9913'):
        embed = discord.Embed(title = "ratbuddy's Inventory", colour = discord.Colour.from_rgb(44,47,51))
        money = data[4].strip('\n')
        a = int(data[9])
    if(user == 'ShadowXII#7240'):
        embed = discord.Embed(title = "ShadowXII's Inventory", colour = discord.Colour.from_rgb(255,0,0))
        money = data[5].strip('\n')
        a = int(data[10])

    b = 2
    msg = "You have " + money + " marcs!"
    if (a == 0):
        embed.add_field(name = 'Empty', value = 'Maybe spend some marcs')
        await ctx.send(embed = embed)
    b = 2
    if (a & b == b):
        embed.add_field(name = 'Big Daddy Rhinehart', value ='World Renowned Doctor, and Football Coach, now in your pocket!')
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/137921870010777600/695021109891825754/a_god.jpeg')
        await ctx.send(embed = embed)
    b = b*2
    if (a & b == b):
        embed.add_field(name = 'Pop-tart Gang', value = 'Gang shit, thats why and who made this blessed image')
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/402876560165830657/693255972508139630/gang.png')
        await ctx.send(embed = embed)
    b = b*2
    if (a & b == b):
        embed.add_field(name = 'Taco Bell Dog', value = 'The long forgotten mascot of ol Taco Bell, too racist to ever return')
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/549996148643856389/696824107169218620/897414028-banner_33.png')
        await ctx.send(embed = embed)
    b = b*2
    if (a & b == b):
        embed.add_field(name = "Twitch IRL Streamer", value = "Twitch sure has changed, maybe for the better, don't worry maybe one day I will make this something better")
        embed.set_image(url = 'https://i.imgur.com/86wH1kX.mp4')
        await ctx.send(embed = embed)
    b = b*2
    if (a & b == b):
        embed.add_field(name = "Marc", value = "ok marc, here is your cheap item, before you even ask for it")
        embed.set_image(url = 'https://www.bgt.nz/tmp/testimonialstalent/marco-fletcher/images/medium/Screen_Shot_2016-04-29_at_11.49.43_AM.png')
        await ctx.send(embed = embed)
    b = b*2
    if (a & b == b):
        embed.add_field(name = "John F. Kennedy", value = "He did stuff in Cuba, and got shot in the head")
        embed.set_image(url = 'https://thumbs.gfycat.com/AdorableDifferentArmednylonshrimp-small.gif')
        await ctx.send(embed = embed)
    b = b*2
    if (a & b == b):
        embed.add_field(name = "Donald Trump", value = "45th President of the United States. Says China, and Mexico a lot")
        embed.set_image(url = 'https://media3.giphy.com/media/sUrqLJoLNpFa8/source.gif')
        await ctx.send(embed = embed)
    b = b*2
    if (a & b == b):
        embed.add_field(name = "A Math Book", value = "Ran out of Ideas lol, but here is a math book")
        embed.set_image(url = 'https://images-na.ssl-images-amazon.com/images/I/41bv5SmS6NL._SX368_BO1,204,203,200_.jpg')
        await ctx.send(embed = embed)
    return


@client.command(pass_context=True, name = 'flum' , help ='check or set flum status')
async def flumstatus(ctx, *args):
    y = list(args)
    filename = "longtermdata.txt"
    author = str(ctx.message.author)
    gamer = 'not set'
    lister = list(args)
    
    if ('game' in lister):
        x = lister.index('game')
        with open(filename, 'r') as file:
            data = file.readlines()
        data[14] = str(lister[x+1:]) + '\n'
        data[14] = ''.join(c for c in data[14] if c not in "'[],")
        with open(filename , 'w') as file:
                file.writelines(data) 
        return

    if ('begun' or 'begun?') in lister:
        msg = '@everyone it must be flum time'
        await ctx.send(msg, tts = True)
        
    if ('nay' in args):
        with open(filename, 'r') as file:
            data = file.readlines()
        if(author == "Baconmaster#3725"):
            data[11] = '-1\n'
        if(author == "ShadowXII#7240"):
            data[12] = '-1\n'
        if(author == "BOOF#4284"):
            data[13] = '-1\n'
        with open(filename , 'w') as file:
                file.writelines(data) 
        return
        
    if ('yea' in args):
        with open(filename, 'r') as file:
                data = file.readlines()
        if(author == "Baconmaster#3725"):
            data[11] = '0\n'
        if(author == "ShadowXII#7240"):
            data[12] = '0\n'
        if(author == "BOOF#4284"):
            data[13] = '0\n'
        with open(filename , 'w') as file:
                file.writelines(data)   
        return

    if ('flavortext' in args):
        filename = './quips/gamemsg.txt'
        y.remove('flavortext')
        y =  str(y) + '\n'
        print(y)
        char_list = ["'", "[" , "]", ","]
        for i in char_list:
            y = y.replace(i, '')
        with open(filename, "a") as file:
            file.write(y)
        msg = 'succesfully added ' + "'" + y.strip('\n') + "'" + ' to flavortext list'
        await ctx.send(msg)

    if ('awake' in args):
        filename = './quips/awakemsg.txt'
        y.remove('awake')
        y =  str(y) + '\n'
        print(y)
        char_list = ["'", "[" , "]", ","]
        for i in char_list:
            y = y.replace(i, '')
        with open(filename, "a") as file:
            file.write(y)
        msg = 'succesfully added ' + "'" + y.strip('\n') + "'" + ' to the startup message list'
        await ctx.send(msg)

    if ('name' in args):
        filename = './quips/botlist.txt'
        y.remove('name')
        y =  str(y) + '\n'
        print(y)
        char_list = ["'", "[" , "]", ","]
        for i in char_list:
            y = y.replace(i, '')
        with open(filename, "a") as file:
            file.write(y)
        msg = 'succesfully added ' + "'" + y.strip('\n') + "'" + ' to flumbot response list'
        await ctx.send(msg)

    if ('bet' in args):
        filename = './quips/betlist.txt'
        y.remove('bet')
        y =  str(y) + '\n'
        print(y)
        char_list = ["'", "[" , "]", ","]
        for i in char_list:
            y = y.replace(i, '')
        with open(filename, "a") as file:
            file.write(y)
        msg = 'succesfully added ' + "'" + y.strip('\n') + "'" + ' to bet list'
        await ctx.send(msg)

    if ('ad' in args):
        filename = './quips/adlist.txt'
        y.remove('ad')
        y =  str(y) + '\n'
        print(y)
        char_list = ["'", "[" , "]", ","]
        for i in char_list:
            y = y.replace(i, '')
        with open(filename, "a") as file:
            file.write(y)
        msg = 'succesfully added ' + "'" + y.strip('\n') + "'" + ' to list of ads'
        await ctx.send(msg)

    if ('video' in args):
        filename = './quips/flumvideos.txt'
        y.remove('video')
        y =  str(y) + '\n'
        print(y)
        char_list = ["'", "[" , "]", ","]
        for i in char_list:
            y = y.replace(i, '')
        with open(filename, "a") as file:
            file.write(y)
        msg = 'succesfully added ' + "'" + y.strip('\n') + "'" + ' to list of flumbot streams'
        await ctx.send(msg)
    
    if ('status' in args):
        with open(filename, 'r') as file:
            data = file.readlines()
        if(int(data[11]) < 0):
            shar = ':x:'
        else:
            shar = ':+1:'
        if(int(data[12]) < 0):
            marc = ':x:'
        else:
            marc = ':+1:'
        if(int(data[13]) < 0):
            niche = ':x:'
        else:
            niche = ':+1:'
        gamer = str(data[14])
        
        embed = discord.Embed(title = "Flumcababilty of Compatriots", colour = discord.Colour.from_rgb(0,144,0))
        embed.add_field(name = 'Sean', value = shar)
        embed.add_field(name = 'Marc', value = marc)
        embed.add_field(name = 'Nick', value = niche)
        embed.add_field(name = 'Game of Tonight', value = gamer)
        embed.set_thumbnail(url = daystart.getad())
        await ctx.send(embed = embed)
        

@client.command(pass_context=True, name = 'shop' , help ='gotta spend those marcs somewhere')
@commands.cooldown(1,10,commands.BucketType.user)
async def shop(ctx, *args):

    filename = "longtermdata.txt"
    author = ctx.message.author
    
    if (len(args) == 0):
        msg = "here is what we gots to sell"
        await ctx.send(msg)
        embed = discord.Embed(title = "Welcome to the WarStone!", colour = discord.Colour.from_rgb(0,144,0))
        embed.add_field(name = 'Item 1', value = 'Big Daddy Rhinehart - \n5000 marcs', inline = True)
        embed.add_field(name = 'Item 2', value = 'Pop-tart Gang - \n2500 marcs', inline = True)
        embed.add_field(name = 'Item 3', value = 'Taco Bell Dog - \n1500 marcs', inline = True)
        embed.add_field(name = 'Item 4', value = 'Twitch IRL Streamer - 10000 marcs', inline = False)
        embed.add_field(name = 'Item 5', value = 'Marc - \n10 marcs', inline = True)
        embed.add_field(name = 'Item 6' , value = 'John F. Kennedy - \n1969 marcs', inline = True)
        embed.add_field(name = 'Item 7', value = 'Donald Trump -\n 2020 marcs', inline = True)
        embed.add_field(name = 'Item 8', value = 'A Math Book -\n 200 marcs', inline = True)
        embed.set_footer(text = 'all sales are final, refunds will not be taken')
        embed.set_thumbnail(url = daystart.getad())
        await ctx.send(embed = embed)
        return
    if (len(args) > 1):
        msg = "don't write a book, just put a number after shop"
        await ctx.send(msg)
        return
    try:
        args = int(*args)
    except ValueError:
        msg = "enter a number after shop if you are looking to buy"
        await ctx.send(msg)
        return
    args = int(args)
    if (args >= 9 or args <= 0):
        msg = "try selecting a number we actually have next time"
        await ctx.send(msg)
        return
    msg = "you want to buy item " + str(args) + "?"
    await ctx.send(msg)
    def check(m):
        return m.content == 'yes' and ctx.message.author == author
    try:
        await client.wait_for('message', check = check, timeout=20)
    except asyncio.TimeoutError:
        msg = "that's ok take your time"
        await ctx.send(msg)
        return
    user = str(ctx.message.author)

    args = int(args)

    if (args == 1):
        price = 1000
    if (args == 2):
        price = 2500
    if (args == 3):
        price = 1500
    if (args == 4):
        price = 10000
    if (args == 5):
        price = 10
    if (args == 6):
        price = 1969
    if (args == 7):
        price = 2020
    if(args == 8):
        price = 200
        
    item = pow(2,args)

    if(user == 'Baconmaster#3725'): 
        with open(filename, 'r') as file:
            data = file.readlines()
        if(int(data[2]) - price < 0 ):
                msg = "broke boy"
                await ctx.send(msg)
                return
        data[7] = int(data[7])
        a = data[7]
        b = item
        if((a & b) == b):
                msg = "you already own this"
                await ctx.send(msg)
                return
        data[2] = str(int(data[2]) - price) + '\n'
        data[7] = str(int(data[7]) + item) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        data = (data[2].strip('\n'))
        msg = "you now have " + data + " marcs!\nThank you for Shopping Flumbot!"
        await ctx.send(msg)
    if(user == 'BOOF#4284'): 
        with open(filename, 'r') as file:
            data = file.readlines()
        if(int(data[3]) - price < 0 ):
                msg = "broke boy"
                await ctx.send(msg)
                return
        data[8] = int(data[8])
        a = data[8]
        b = item
        if((a & b) == b):
                msg = "you already own this"
                await ctx.send(msg)
                return
        data[3] = str(int(data[3]) - price) + '\n'
        data[8] = str(int(data[8]) + item) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        data = (data[3].strip('\n'))
        msg = "You now have " + data + " marcs!\nThank you for Shopping Flumbot!"
        await ctx.send(msg)
    if(user == 'ratbuddy#9913'): 
        with open(filename, 'r') as file:
            data = file.readlines()
        if(int(data[4]) - price < 0 ):
                msg = "broke boy"
                await ctx.send(msg)
                return
        data[9] = int(data[9])
        a = data[9]
        b = item
        if((a & b) == b):
                msg = "you already own this"
                await ctx.send(msg)
                return
        data[4] = str(int(data[4]) - price) + '\n'
        data[9] = str(int(data[9]) + item) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        data = (data[4].strip('\n'))
        msg = "you now have " + data + " marcs!\nThank you for Shopping Flumbot!"
        await ctx.send(msg)
    if(user == 'ShadowXII#7240'): 
        with open(filename, 'r') as file:
            data = file.readlines()
        if(int(data[5]) - price < 0 ):
                msg = "broke boy"
                await ctx.send(msg)
                return
        data[10] = int(data[10])
        a = data[10]
        b = item
        if((a & b) == b):
                msg = "you already own this"
                await ctx.send(msg)
                return
        data[5] = str(int(data[5]) - price) + '\n'
        data[10] = str(int(data[10]) + item) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        data = (data[5].strip('\n'))
        msg = "you now have " + data + " marcs!\nThank you for Shopping Flumbot!"
        await ctx.send(msg)    
    return

@client.command(pass_context=True, name = 'flip' , help ='flip a standard US coin')
@commands.cooldown(1,10,commands.BucketType.user)
async def flip(ctx, *args):
    x = list(args)
    if('coin' in x):
        if(random.randint(0,1) == 1):
            result = 'Heads'
        else:
            result = 'Tails'
        msg = 'Flipping...'
        await ctx.send(msg, tts = True)
        await asyncio.sleep(4)
        msg = 'Coin is ' + result + ' side up.'
        await ctx.send(msg, tts = True)

@client.command(pass_context=True, name = 'roll' , help ='roll any dice flumbot has')
async def roll(ctx, *args):
    x = list(args)
    dicerol = 1
    if('dice' and 'sided' and ('times' or 'time') in x):
        sides = x[x.index('sided') - 1]
        times = x[x.index('times') - 1]
        while (times != 0):
            msg = 'Dice ' + str(dicerol) + ' rolled a ' + str(random.randint(1,int(sides)))
            await asyncio.sleep(2)
            await ctx.send(msg)
            times = int(times) - 1
            dicerol = dicerol + 1
        return
    elif('dice' and 'sided') in x:
        sides = x[x.index('sided') -1]
        print(sides)
        roll = str(random.randint(1,int(sides)))
        if (int(sides) == 20):
            if(int(roll) == 20):
                await asyncio.sleep(2)
                msg = '<:PogChamp:583814253484441601>'
                await ctx.send(msg)
                msg = 'You rolled a ' + roll + '!'
                await ctx.send(msg)
                return
            if(int(roll) == 1):
                await asyncio.sleep(2)
                msg = '<:monkaS:583814789298651154>'
                await ctx.send(msg)
                msg = 'You rolled a ' + roll + '!'
                await ctx.send(msg)
                return
        msg = 'You rolled a ' + roll + '!'
        await asyncio.sleep(2)
        await ctx.send(msg)
        return
    elif('d20' in x or 'd10' in x or 'd4' in x or 'd6' in x or 'd8'  in x or 'd12' in x or 'd100' in x):
        if 'd10' in x:
            sides = 10
        elif 'd20' in x:
            sides = 20
        elif 'd4' in x:
            sides = 4
        elif 'd6' in x:
            sides = 6
        elif 'd8' in x:
            sides = 8
        elif 'd12' in x:
            sides = 12
        elif 'd100' in x:
            sides = 100
        else:
            msg = 'not a valid dice, try again'
            await ctx.send(msg)
            return
        dicerol = 1
        if('x' in x):
            if('+' in x):
                mod = x[x.index('+') + 1]
                extra = ' + '
            else:
                mod = ''
                extra = ''
            times = x[x.index('x') +1]
            while (times != 0):
                msg = 'Dice ' + str(dicerol) + ' rolled a ' + str(random.randint(1,sides)) + extra + mod + '!'
                await asyncio.sleep(2)
                await ctx.send(msg)
                times = int(times) - 1
                dicerol = dicerol + 1
            return
        roll = str(random.randint(1,sides))
        if ((int(roll) == 20) and (sides == 20)):
            await asyncio.sleep(2)
            msg = '<:PogChamp:583814253484441601>'
            await ctx.send(msg)
            if('+' in x):
                mod = x[x.index('+') + 1]
                extra = ' + '
            else:
                mod = ''
                extra = ''
            msg = 'You rolled a ' + roll + extra + mod + '!'
            await ctx.send(msg)
            return
        if((int(roll) == 1) and (sides == 20)):
            await asycnio.sleep(2)
            msg = '<:monkaS:583814789298651154>'
            await ctx.send(msg)
            if('+' in x):
                mod = x[x.index('+') + 1]
                extra = ' + '
            else:
                mod = ''
                extra = ''
            msg = 'You rolled a ' + roll + extra + mod + '!'
            await ctx.send(msg)
            return
        if('+' in x):
            mod = x[x.index('+') + 1]
            extra = ' + '
        else:
            mod = ''
            extra = ''
        msg = 'You rolled a ' + roll + extra + mod + '!'
        await asyncio.sleep(2)
        await ctx.send(msg)
        return
    else:
        msg = 'try wording it better\nexamples are:\n"roll a 20 sided dice 5 times"\n"roll a 20 sided dice"\n"roll d20 x 5 + 2"'
        await ctx.send(msg)
        return
    

@client.command(pass_context=True, name = 'check-in' , help ='check in for daily marcs, only avaliable at 7:00 EDT/EST')
@commands.cooldown(1,10,commands.BucketType.user)
async def checkin(ctx, *args):
    filename = "longtermdata.txt"
    with open(filename, 'r') as file:
        data = file.readlines()
    today = date.today()
    now = datetime.datetime.now()
    dt_string = now.strftime("%H%M")
    print(dt_string)

    user = str(ctx.message.author)
    channel = ctx.message.author.voice.channel
    
    if (user in data[15]):
        msg = "I already gave you credit for flum today baka:rage:! Try again tomorrow!"
        await ctx.send(msg)
        return

    if ( (channel == 'Flum') or (channel == 'Heisturbating ( ͡° ͜ʖ ͡°)') ):
        msg = "Can't Fool me :triumph: you aren't even in the voice chat :triumph:"
        await ctx.send(msg)
    elif ((int(dt_string) <= 2200) and (int(dt_string) >= 1900)):
        msg = "Thank you for your service kind stranger! Have some marcs to spend!"
        await ctx.send(msg, tts=True)
        if (data[15] == 'empty\n'):
            data[15] = str(user) + '\n'
        else:
            data[15] = data[15].strip('\n')
            data[15] = data[15] + ' ' + str(user) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        if (user == 'Baconmaster#3725'):
            with open(filename, 'r') as file:
                data = file.readlines()
            data[2] = str(int(data[2]) + 75) + '\n'
            with open(filename , 'w') as file:
                file.writelines(data)
            data = (data[2].strip('\n'))
            msg = "Sean has " + data + " marcs!"
            await ctx.send(msg)
        if (user == 'BOOF#4284'):
            with open(filename, 'r') as file:
                data = file.readlines()
            data[3] = str(int(data[3]) + 75) + '\n'
            with open(filename , 'w') as file:
                file.writelines(data)
            data = (data[3].strip('\n'))
            msg = "Niche has " + data + " marcs!"
            await ctx.send(msg)
        if (user == 'ratbuddy#9913'):
            with open(filename, 'r') as file:
                data = file.readlines()
            data[4] = str(int(data[4]) + 75) + '\n'
            with open(filename , 'w') as file:
                file.writelines(data)
            data = (data[4].strip('\n'))
            msg = "Rat has " + data + " marcs!"
            await ctx.send(msg)
        if (user == 'ShadowXII#7240'):
            with open(filename, 'r') as file:
                data = file.readlines()
            data[5] = str(int(data[5]) + 75) + '\n'
            with open(filename , 'w') as file:
                file.writelines(data)
            data = (data[5].strip('\n'))
            msg = "Marc has " + data + " marcs!"
            await ctx.send(msg)
    else:
        bet = int(dt_string) - 1900
        if (bet > 0):
            msg = "Too late! Try tommorow at 7:00 p.m. like everyone else"
            await ctx.send(msg)
        else:
            msg = "Appreciate the enthusiam but, wait till everyone else is awake and flumcabale"
            await ctx.send(msg)

    
@client.command(pass_context=True, name = 'off' , help ='Turn off autopilot :(')
@commands.cooldown(1,10,commands.BucketType.user)
async def off(ctx, *args):
    global pilot
    pilot = 0
    server = ctx.message.guild.voice_client
    await server.disconnect()
    print('autopilot off')

@client.command(pass_context=True, name = 'cancel', help ='null')
@commands.cooldown(1,10,commands.BucketType.user)
async def cancel(ctx, *args):
    global x
    x = -999999999999999999999

@client.command(pass_context=True, name = 'stop' , help ='Ruin the fun for everyone')
@commands.cooldown(1,10,commands.BucketType.user)
async def stop(ctx, *args):
    global pilot
    pilot = 0
    server = ctx.message.guild.voice_client
    await server.disconnect()


client.run(token)
