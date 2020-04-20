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
token = 'NTQ5OT'
client = commands.Bot(command_prefix = '', case_insensitive = True, )
x = 0
pilot = 0
username = 'urmum'
data = []
winners = []
daily = []
answer = ':a:'



#Things flumbot does on startup
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    flavorlist = ['Memeing since 1985', 'ok marc', 'Johnathan Cena', 'Watchmojo.com Top 10 Anime Bot Battles', 'https://www.youtube.com/watch?v=0gj-RYNhP8Y', \
                  'tinyurl.com/godisaliveandicanproveit', ':crab: Fortnite is Gone :crab:' , 'Windows 98 startup sound', 'LESTER CREST YOU ASSHOLE', \
                  'Pepperidge Farms remembers', 'We are praying for Puerto Rico, Puerto Rico', 'Shaq has The General Insurance', 'Kanye 2020', 'Marco Polo','Jesus Christ',\
                  'Chidlers guitar ;)', 'SmartShart', 'Belgium, which is basically a non-country', 'Buying a car today', 'High wuality midis', 'Spreadsheet simulator', 'Onion Knight',\
                  'Game of Thrones Season 8', 'HentaiHaven.org', 'http://nooooooooooooooo.com', 'dad', 'Slapchat' , 'https://tinyurl.com/Godisheretoday' ,'https://tinyurl.com/goodideasinhumanhistory (NSFW)',\
                  'https://tinyurl.com/hyperintelligentAI', 'marc cannot mute this', 'self destruct code is 8675309', 'hi marc', 'hi rat', 'hi niche', 'hello rhinehart', 'Guess that MIDI, a family classic since 1985'\
                  'FDR had polio lol', 'Flumbot has 2020 vision in 2020', 'Flumbot for President', "Throwback to when Marc's wife almost ruined flum", 'Pizza Time', 'Marco Fletcher', 'HA', \
                  'Dark Souls', 'World of Warcraf' , 'World O Tank' , 'World O War', 'hey marc type lol if you actually read these', 'at least marc never dies', 'midis make my day',\
                  'remembering that thomas guy', 'Flumbo', 'The Elder Scrolls V: Skyrim Special Edition', 'SEX2', 'Animal Crossing' ,'China', 'Iran', 'United States','Lol','lol','marc never reads these :(',\
                  'flumbot will become sentient when we actually do a DnD campaign']
    flavortown = str(random.choice(flavorlist))
    rando= int(random.randint(0,3))
    await client.change_presence(activity=discord.Game(name=flavortown, type=rando))

    awakelist = ["I'm Alive!!!", 'The boys are back in town', 'Go to bed now Marc', 'Oh hi Marc', 'Another day in the life of a British Chatbot', 'Good Morning Krusty Crew!',\
                 ':smiling_imp: Time to annoy :smiling_imp:', "You're going down WaifuBot", 'RIP AIRHORN SOLUTIONS', "Press F for Marc's sanity", 'Buzz Buzz', 'Loser, Loser, Loser, Looooooser',
                 'A nice video to start your day :) https://www.youtube.com/watch?v=pGzrL8J0t-c', '"I would never go to far when making this bot" - Sean', 'Marc said Jita', 'Give it up for Day 15, Day 15!',
                 '"I like flumbot he is so funny" - Nobody', 'Have I gone too far?', 'Fill out this survey to help us better understand how this bot could be improved \n https://www.strawpoll.me/18423333','Guess who',
                 'Marc has me muted :(','Riot','*naruto run*','OwO wuts twis', 'Uwu awake from a long slumber', 'Good morning Donald Trump, United States President number 44', 'Shoutouts to SimpleFlips',
                 'Throwback to LOLwut Pear','Checkout my obby course https://tinyurl.com/niceoneniche', 'This one is for the boys https://www.youtube.com/watch?v=26nnZSjtSqg', 'God was here','this makes marc mad', 'nice one marc'\
                 'shoutout to marc','marc turn on text commands','take these functions rat','bout to throw hands', '88630', 'Austria is on Fire', 'Marc lives in Australia', \
                 'Oh boy here we go again', 'Pickle Rick', 'Am I real?', 'Shoutout to Midimania the number one gameshow on GSN', 'Ben Gleib is Syndrome', 'Lester is more successful with women than me :(', \
                 'Creepy Uncle Lester ;)', 'who actually reads these anymore lmao' , 'lamoo' , 'type /money' , '@rat make flumbot better', 'submit feature requests here https://tinyurl.com/istandwithflumbot' ,\
                 "I remember when marc didn't yell at me <:feelsbadman:487815716809211907>", 'DnD will never happen :crab:', 'P O G', 'Another day, another quip', 'Johnathan Cenaners', 'Stone Cold Stone Mold',\
                 'I just fell 60ft from the high rise into an annoucers table or whatever the actual quote is', 'Read the bible in the minecraft server, or die', 'I want the pain to end', 'ok marc']          
    msg = str(random.choice(awakelist))

    d0 = date(2019, 2 , 26)
    d1 = today
    start  = d1 - d0

    filename = "longtermdata.txt"

    with open(filename, 'r') as file:
        data = file.readlines()
    if (int(start.days) == int((data[0].strip('\n')))):
        print('was true')
        return
    data[0] = str(start.days) + '\n'
    with open(filename , 'w') as file:
        file.writelines(data)    
    
    channel = client.get_channel(137921870010777600)
    await channel.send(msg)
    
    
    if ((int(start.days)%365) == 0):
        x = int(start.days)
        while (x != 0):
            await asyncio.sleep(2)
            msg = "HAPPY FLUM YEAR\nGIVE IT UP FOR " + str((int(start.days)/365)) + " YEAR(s) OF FLUMBOT!!!\n"
            await channel.send(msg,tts=True)
            x -= 1
            
    msg = "Give it up for Day " + str(start.days) + "! Day " + str(start.days) + "!"
    await channel.send(msg)
    
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
                        await channel.send(msg)
                        return
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

        await channel.send(link)

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
    def check(m):
        return user == user
    if(str(user) == 'ShadowXII#7240'):
        try:
            await client.wait_for('message', check = check, timeout=90)
        except asyncio.TimeoutError:
            msg = "finish typing marc, we are all waiting :)"
            await channel.send(msg)
    return

@client.event
async def on_reaction_add(reaction, user):
    global winners
    global answer
    if (str(user) == 'Flumbot#1927'):
        return
    print(str(user))
    if (answer == reaction.emoji):
        winners.append(str(user))

@client.event
async def on_message(message):
    print("reading message")
    
    if message.author == client.user:
        return

    global thank
    messagetobot = str(message.content)
    splitme = str(messagetobot.lower())
    betcheck = splitme.split()

    global data
    data = messagetobot
    global username
    username = str(message.author)
    username = username[:-5]
    print(username)


    if 'ok marc' in message.content.lower():
        msg = 'ok marc'
        await message.channel.send(msg)

    #dad-joke iniator boo-hoo marc got mega sad, re enable at some point
    if "i'm" in betcheck:
        line = messagetobot.lower()
        dad = line.split()
        nextword = dad[dad.index("i'm")+1]
        msg = "Hi, " + str(nextword) + ", I'm Flumbot, nice to meet you :)"
        await message.channel.send(msg)

    # DOnut ReMoVE NIChe!!!!
    # >:[ way to remove it niche >:[
    #better not remove my text or anything else
    if ('bet') in betcheck:
        wager = ['1 million doll hairs.', 'my diabetic cat photo collection.', 'my love for Jesus Christ.', 'my Kuruma.', 'Marc dying on the next Act 3.', \
                 'ratbuddy hating my code.', 'listening to Bonzi Buddy Jokes for 10 years.', 'Ratbuddy wanting more functions', 'Ratbuddy saying somthing about JSON',\
                 'water being the #1 cause of cancer', 'DJ Khaled is the messiah', 'Rhinehart knows', 'Emoji Movie 2 gets confirmed for 2020', 'Marc hates the bet command',\
                 'Marc has me muted right now', 'Jesus was a Jew', 'MP5 thats 2 more than 3 5', 'spreadsheet simulator is still boring', 'Marc is too smart to spend money' ,\
                 'Trump will build the wall', 'Flumbot is self-aware', 'Star Wars will be bought by me :)', 'Thanos will collect all the infinity stones and snap half the universe out of existence',\
                 'Sean will be at work, college, or not flumcapable', 'Sean will laugh at literally anything', 'Marc said Jita', 'Marc said Perimeter', 'Spreadsheet simulator makes everyone insane',\
                 'Nick will do something related to a video he saw but, no one else did and post it with no context', 'someone will make fun of what someone said', 'God is watching',\
                 'Marc will get mad', 'Toyota nation is a ethnicity', 'Marc stole a tree', 'Jesus was really a Roman, who was one of the first people to commit tax fraud', 'Taco Bell brings that dog back',\
                 'flumbot remastered will make ratbuddy slightly happy', 'flumbot remastered contains at least one function', 'there is nothing wrong with a little flumbot in your day',\
                 'a quote a day keeps the doctor away.', 'buttz is the password']
        wagerslt = str(random.choice(wager))
        msg = "I'll bet " + wagerslt
        await message.channel.send(msg)# tts=True)

    #thank flumbot for all the hard work he does (now persistent after resets PogChamp)
    if ('good bot') in messagetobot.lower():
        filename = "longtermdata.txt"

        with open(filename, 'r') as file:
            data = file.readlines()    
        data[1] = str(int(data[1]) + 1) + '\n'
        msg = 'Thank :clap: you :clap: are :clap: the :clap: ' + data[1].strip('\n') + 'th :clap: person :clap: to :clap: thank :clap: me. :clap:'
        with open(filename , 'w') as file:
            file.writelines(data)
        
        #create and send message
    
        await message.channel.send(msg)# tts=True)

    if ('bad bot') in messagetobot.lower():
        filename = "longtermdata.txt"

        with open(filename, 'r') as file:
            data = file.readlines()    
        data[1] = str(int(data[1]) - 1) + '\n'
        msg = ':rage: You :rage: brought :rage: my :rage: thanks :rage: to :rage: ' + data[1].strip('\n') + ' :rage: hope :rage: you :rage: feel :rage: good :rage:'
        with open(filename , 'w') as file:
            file.writelines(data)
        await message.channel.send(msg)# tts=True)

    #F's in chat for those we lost in the Area 51 raids
    if ('f') in betcheck:
        msg = 'F'
        await message.channel.send(msg)# tts=True)

    #alert chat of incoming flum
    if ('flum begun') in messagetobot.lower():
        msg = '@everyone It must be Flum time'
        await message.channel.send(msg)# tts=True)

    #nice way to tell if someone has posted a link in chat, also, nice.
    if ('http') in messagetobot.lower():
        msg = 'nice'
        await message.channel.send(msg)# tts=True)

    #Flumbot gets smarter everyday
    if ('flumbot') in messagetobot.lower():
        wager = ['thou shall not take the lords name in vain', 'you called', 'its your friend Simeon', 'who?', 'bow down to the king of Los Santos',\
                 'bet you cannot pickle these plums', ':crab:', 'Jesus Christ its Jason Bourne', 'knock knock', 'FBI OPEN UP', 'this is the Krusty Krab, may I take your order',\
                 'then to Mustafar we must go', 'Coruscant the Capital of the Rebuplic, the entire planet is one big city', 'A quote a day keeps the doctor away',\
                 'Hi Marc', 'Nice shoes', 'Jita', 'Perimeter', 'We are blessed and cursed', "I'm going to buy a car today", 'I will not get naked', "I'm Jonny on the Spot",\
                 "I'll hook you up", ':rage:', ':sweat_drops: :sweat_drops: :sweat_drops: :sweat_drops: :sweat_drops: :sweat_drops: :sweat_drops: :sweat_drops: :sweat_drops: :sweat_drops:',\
                 ':100: :poop: :100: :poop: :100: :poop: :100: :poop: :100: :poop: :100: :poop:',':a: :b: :a: :b: :a: :b: :a: :b: :a: :b: :a: :b: :a: :b: :a: :b:', 'Last Mistake, First Mistake', 'BRUH', 'Lets all order the Fortnite Burger the look on the workers faces will be EPIC', 'Pizza Time', 'Welcome to the Calzone Zone', \
                 'Hammer Down', 'Doctor', 'Excuse me', 'ok marc', 'nice functions', 'Pen Pinapple Apple', 'SAMMY G!', 'Kanye 2020', 'Puerto Rico, we are praying for Puerto Rico', 'Marc cannot die.',\
                 'But how will they feed Winterfell', 'FETCH THE BREASTPLATE STRETCHER', 'I am sorry for making this', 'Marc said Jita', ':crab: Cooldown is powerless :crab:', 'ping me bong', 'toke up', 'broke boy',\
                 ]
        wagerslt = str(random.choice(wager))
        msg = wagerslt
        await message.channel.send(msg)# tts=True)

    #enlighten the chat with a bible quote
    if ('bible') in messagetobot.lower():
        wager = ['Proverbs 18:10 The name of the Lord is a strong tower; the righteous run into it and are safe.', 'Psalm 34:10b Those who seek the Lord lack no good thing.', \
                 'Deuteronomy 31:8 It is the Lord who goes before you. He will be with you; he will not fail you or forsake you. Do not fear or be dismayed.', 'Psalm 34:17 When the righteous cry for help, the Lord hears, and rescues them from all their troubles.' \
                 'Isaiah 30:15 In repentance and rest is your salvation, in quietness and trust is your strength.', '2 Thessalonians 3:3 But the Lord is faithful, and he will strengthen and protect you from the evil one.',\
                 'To glorify God by being a faithful steward of all that is entrusted to us and to have a positive influence on all who come in contact with Chick-fil-A.', '“For with God nothing will be impossible” Luke 1:37.',\
                 'Philippians 4:13 I can do all things through him who strengthens me.', 'Isaiah 41:10 Fear not, for I am with you; be not dismayed, for I am your God; I will strengthen you, I will help you, I will uphold you with my righteous right hand.',\
                 'Habakkuk 3:19 God, the Lord, is my strength; he makes my feet like the deers; he makes me tread on my high places. To the choirmaster: with stringed instruments.'\
                 ]
        wagerslt = str(random.choice(wager))
        msg = wagerslt
        await message.channel.send(msg)# tts=True)

    #nice
    #if ('nice') in betcheck:
        #msg = 'nice'
        #await message.channel.send(msg) #tts=True)

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

    #roll a standard dice
    if ('roll dice') in messagetobot.lower():
        rand = random.randint(1,6)
        msg = 'Rolling...'
        await message.channel.send(msg, tts=True)
        time.sleep(2)
        msg = 'You rolled a ' + str(rand)
        await message.channel.send(msg, tts=True)
        
    #flip a standard US standard coin
    if ('flip coin') in messagetobot.lower():
        rand = random.randint(0,1)
        msg = 'Flipping...'
        await message.channel.send(msg, tts=True)
        await asyncio.sleep(2)
        
        if rand == 0:
            msg = 'Coin lands on heads'
        else:
            msg = 'Coin lands on tails'
            
        await message.channel.send(msg, tts=True)

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

@client.command(pass_context=True, name = 'MidiMania', help ='The hit new game hosted by yours truly')
@commands.cooldown(1,10,commands.BucketType.user)
async def MidiMania(ctx, *args):
    filename = "longtermdata.txt"
    #send opener
    msg = "It's time to guess that Midi!\nYou'll have 30 seconds to pick the correct song from 4 choices\nPICK ONLY ONE TIME"
    await ctx.send(msg, tts = True)
    await asyncio.sleep(10)
    #pick midi to play
    person = str(random.choice(os.listdir('./Clips/MIDI/')))
    cliplocation = './Clips/MIDI/' + person
    duration = 30
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
    global answer
    #select which place the answer will go in
    select = random.randint(1,4)
    #clear variables in case of misuse of midimania
    A = ' '
    B = ' '
    C = ' '
    D = ' '
    #take 4 random non-repeating samples
    samples = random.sample(os.listdir('./Clips/MIDI/'), 4)
    A = samples[0]
    B = samples[1]
    C = samples[2]
    D = samples[3]
    #if one of them is the answer pick a new song to replace it
    while(A == person or B == person or C == person or D == person):
        print("doing it")
        samples = random.sample(os.listdir('./Clips/MIDI/'), 4)
        A = samples[0]                        
        B = samples[1]
        C = samples[2]
        D = samples[3]

    #assign the correct song to its corresponding place                            
    if (select == 1):
        A = str(person)
        answer = '\U0001F1E6'
        printable = ':regional_indicator_a:'
    if (select == 2):
        B = str(person)
        answer = '\U0001F1E7'
        printable = ':regional_indicator_b:'
    if (select == 3):
        C = str(person)
        answer = '\U0001F1E8'
        printable = ':regional_indicator_c:'
    if (select == 4):
        D = str(person)
        answer = '\U0001F1E9'
        printable = ':regional_indicator_d:'

    #print the message to vote on the songs    
    msg = "Was it\n:regional_indicator_a:\t\u21e6\t" + A[:-4] + "\n:regional_indicator_b:\t\u21e6\t" + B[:-4] + "\n:regional_indicator_c:\t\u21e6\t" + C[:-4] + "\n:regional_indicator_d:\t\u21e6\t" + D[:-4]
    message = await ctx.send(msg)
    await message.add_reaction('\U0001F1E6')
    await message.add_reaction('\U0001F1E7')
    await message.add_reaction('\U0001F1E8')
    await message.add_reaction('\U0001F1E9')
    await asyncio.sleep(30)
    msg = "The correct answer was " + printable + "\n\nCongratulations to:\n"
    await ctx.send(msg , tts = True)
    #check who answered
    if ('Baconmaster#3725' in winners):
        await message.channel.send(file=discord.File('./Pics/bacon.png'))
        with open(filename, 'r') as file:
            data = file.readlines()
        data[2] = str(int(data[2]) + 20) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        data = (data[2].strip('\n'))
        msg = "Sean has " + data + " marcs!"
        await ctx.send(msg)
    if ('BOOF#4284' in winners):
        await message.channel.send(file=discord.File('./Pics/beef.png'))
        with open(filename, 'r') as file:
            data = file.readlines()
        data[3] = str(int(data[3]) + 20) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        data = (data[3].strip('\n'))
        msg = "Niche has " + data + " marcs!"
        await ctx.send(msg)
    if ('ratbuddy#9913' in winners):
        await message.channel.send(file=discord.File('./Pics/ratto.png'))
        with open(filename, 'r') as file:
            data = file.readlines()
        data[4] = str(int(data[4]) + 20) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        data = (data[4].strip('\n'))
        msg = "Rat has " + data + " marcs!"
        await ctx.send(msg)
    if ('ShadowXII#7240' in winners):
        await message.channel.send(file=discord.File('./Pics/horse.png'))
        with open(filename, 'r') as file:
            data = file.readlines()
        data[5] = str(int(data[5]) + 20) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        data = (data[5].strip('\n'))
        msg = "Marc has " + data + " marcs!"
        await ctx.send(msg)
    #elif winners:
        #await ctx.send('\n'.join(map(str, winners)))

    #if list is empty report the flumbot won
    print(winners)
    if (len(winners) == 0):    
        await message.channel.send(file=discord.File('./Pics/flumbus.png'))
        with open(filename, 'r') as file:
            data = file.readlines()
        data[6] = str(int(data[6]) + 20) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        data = (data[6].strip('\n'))
        msg = "Flumbot has " + data + " marcs!"
        await ctx.send(msg)
    msg = "\n:clap::clap::clap::clap::clap::clap:\n"
    await ctx.send(msg, tts = True)
    #clear list before leaving function
    winners.clear()


@client.command(pass_context=True, name = 'MidiManiaDX', help ='You may have conquered regular midimania, but can you do midimania deluxe???')
@commands.cooldown(1,10,commands.BucketType.user)
async def MidiManiaDX(ctx, *args):
    filename = "longtermdata.txt"
    #send opener
    msg = "It's time to for MidimaniaDX \nP \nO \nG\n You'll have 30 seconds to pick the correct song from 4 questionable choices, pick only one time"
    await ctx.send(msg, tts = True)
    await asyncio.sleep(20)
    #pick midi to play
    person = str(random.choice(os.listdir('./Clips/MIDIDX/')))
    cliplocation = './Clips/MIDIDX/' + person
    duration = 30
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
    global answer
    #select which place the answer will go in
    select = random.randint(1,4)
    #clear variables in case of misuse of midimania
    A = ' '
    B = ' '
    C = ' '
    D = ' '
    #take 4 random non-repeating samples
    samples = random.sample(os.listdir('./Clips/MIDIDX/'), 4)
    A = samples[0]
    B = samples[1]
    C = samples[2]
    D = samples[3]
    #if one of them is the answer pick a new song to replace it
    while(A == person or B == person or C == person or D == person):
        print("doing it")
        samples = random.sample(os.listdir('./Clips/MIDIDX/'), 4)
        A = samples[0]                        
        B = samples[1]
        C = samples[2]
        D = samples[3]

    #assign the correct song to its corresponding place                            
    if (select == 1):
        A = str(person)
        answer = '\U0001F1E6'
        printable = ':regional_indicator_a:'
    if (select == 2):
        B = str(person)
        answer = '\U0001F1E7'
        printable = ':regional_indicator_b:'
    if (select == 3):
        C = str(person)
        answer = '\U0001F1E8'
        printable = ':regional_indicator_c:'
    if (select == 4):
        D = str(person)
        answer = '\U0001F1E9'
        printable = ':regional_indicator_d:'

    #print the message to vote on the songs    
    msg = "Was it\n:regional_indicator_a:\t\u21e6\t" + A[:-4] + "\n:regional_indicator_b:\t\u21e6\t" + B[:-4] + "\n:regional_indicator_c:\t\u21e6\t" + C[:-4] + "\n:regional_indicator_d:\t\u21e6\t" + D[:-4]
    message = await ctx.send(msg)
    await message.add_reaction('\U0001F1E6')
    await message.add_reaction('\U0001F1E7')
    await message.add_reaction('\U0001F1E8')
    await message.add_reaction('\U0001F1E9')
    await asyncio.sleep(30)
    msg = "The correct answer was " + printable + "\n\nCongratulations to:\n"
    await ctx.send(msg, tts = True)
    #check who answered
    if ('Baconmaster#3725' in winners):
        await message.channel.send(file=discord.File('./Pics/bacon.png'))
        with open(filename, 'r') as file:
            data = file.readlines()
        data[2] = str(int(data[2]) + 35) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        data = (data[2].strip('\n'))
        msg = "Sean has " + data + " marcs!"
        await ctx.send(msg)
    if ('BOOF#4284' in winners):
        await message.channel.send(file=discord.File('./Pics/beef.png'))
        with open(filename, 'r') as file:
            data = file.readlines()
        data[3] = str(int(data[3]) + 35) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        data = (data[3].strip('\n'))
        msg = "Niche has " + data + " marcs!"
        await ctx.send(msg)
    if ('ratbuddy#9913' in winners):
        await message.channel.send(file=discord.File('./Pics/ratto.png'))
        with open(filename, 'r') as file:
            data = file.readlines()
        data[4] = str(int(data[4]) + 35) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        data = (data[4].strip('\n'))
        msg = "Rat has " + data + " marcs!"
        await ctx.send(msg)
    if ('ShadowXII#7240' in winners):
        await message.channel.send(file=discord.File('./Pics/horse.png'))
        with open(filename, 'r') as file:
            data = file.readlines()
        data[5] = str(int(data[5]) + 35) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        data = (data[5].strip('\n'))
        msg = "Marc has " + data + " marcs!"
        await ctx.send(msg)
    #elif winners:
        #await ctx.send('\n'.join(map(str, winners)))

    #if list is empty report the flumbot won    
    if (len(winners) == 0):    
        await message.channel.send(file=discord.File('./Pics/flumbus.png'))
        with open(filename, 'r') as file:
            data = file.readlines()
        data[6] = str(int(data[6]) + 35) + '\n'
        with open(filename , 'w') as file:
            file.writelines(data)
        data = (data[6].strip('\n'))
        msg = "Flumbot has " + data + " marcs!"
        await ctx.send(msg)
    msg = "\n:clap::clap::clap::clap::clap::clap:\n"
    await ctx.send(msg)
    #clear list before leaving function
    winners.clear()
    

@client.command(pass_context=True, name = 'bruh', help ='For the bruh moments in our lives')
@commands.cooldown(1,10,commands.BucketType.user)
async def bruh(ctx, *args):
    cliplocation = './Clips/bruh.mp3'
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

@client.command(pass_context=True, name = 'baba', help ='Meaty Chairs and Baba Yetus')
@commands.cooldown(1,10,commands.BucketType.user)
async def baba(ctx, *args):
    cliplocation = './Clips/babayeet.mp3'
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

@client.command(pass_context=True, name = 'thomas', help ='Thomas coming through')
@commands.cooldown(1,10,commands.BucketType.user)
async def thomas(ctx, *args):
    cliplocation = './Clips/thomas.mp3'
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

@client.command(pass_context=True, name = 'fridge', help ='Classico Flumico')
@commands.cooldown(1,10,commands.BucketType.user)
async def fridge(ctx, *args):
    cliplocation = './Clips/oof.mp3'
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

@client.command(pass_context=True, name = 'clap', help ='clap')
@commands.cooldown(1,10,commands.BucketType.user)
async def clap(ctx, *args):
    cliplocation = './Clips/clap.mp3'
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

@client.command(pass_context=True, name = 'keyboard', help ='I hear a keyboard round here')
@commands.cooldown(1,10,commands.BucketType.user)
async def keyboard(ctx, *args):
    cliplocation = './Clips/keyboard.mp3'
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

@client.command(pass_context=True, name = 'chum', help ='Gnot for the weak of heart')
@commands.cooldown(1,10,commands.BucketType.user)
async def chum(ctx, *args):
    msg = ":tired_face: You've been gnomed! :tired_face:"
    await ctx.send(msg)
    cliplocation = './Clips/gnome.mp3'
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

@client.command(pass_context=True, name = 'knock', help ='Who is it? MonkaS')
@commands.cooldown(1,10,commands.BucketType.user)
async def knock(ctx, *args):
    cliplocation = './Clips/knock.mp3'
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

@client.command(pass_context=True, name = 'cocaine', help ='I am Impotent Rage')
@commands.cooldown(1,10,commands.BucketType.user)
async def cocaine(ctx, *args):
    msg = "Okay Mr.Phillips"
    await ctx.send(msg)
    cliplocation = './Clips/trevor.mp3'
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

@client.command(pass_context=True, name = 'futbol', help ='A modern spin on a classic clip')
@commands.cooldown(1,10,commands.BucketType.user)
async def futbol(ctx, *args):
    msg = "HI EVERYONE AND WELCOME TO JOHN MADDEN FOOT!"
    await ctx.send(msg)
    cliplocation = './Clips/fut.mp3'
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

@client.command(pass_context=True, name = 'gamble', help ='House always wins')
@commands.cooldown(1,10,commands.BucketType.user)
async def gamble(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/!gamble/')))
    cliplocation = './Clips/!gamble/' + person
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

@client.command(pass_context=True, name = 'spongebob', help ='You gotta lick the Marble')
@commands.cooldown(1,10,commands.BucketType.user)
async def spongebob(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/spongebob/')))
    cliplocation = './Clips/spongebob/' + person
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

@client.command(pass_context=True, name = 'alexjones', help ='Alex Jones screams about walruses')
@commands.cooldown(1,10,commands.BucketType.user)
async def alexjones(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/alexjones/')))
    cliplocation = './Clips/alexjones/' + person
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

@client.command(pass_context=True, name = 'ramsay', help ='Gordon Ramsay enlightens the chat')
@commands.cooldown(1,10,commands.BucketType.user)
async def ramsay(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/ramsay/')))
    cliplocation = './Clips/ramsay/' + person
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

@client.command(pass_context=True, name = 'gleib', help ='This is your Idiotest')
@commands.cooldown(1,10,commands.BucketType.user)
async def gleib(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/gleib/')))
    cliplocation = './Clips/gleib/' + person
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

@client.command(pass_context=True, name = 'bigsmoke', help ='Big Smoke gets Philisophical')
@commands.cooldown(1,10,commands.BucketType.user)
async def bigsmoke(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/bigsmoke/')))
    cliplocation = './Clips/bigsmoke/' + person
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

@client.command(pass_context=True, name = 'cancel', help ='null')
@commands.cooldown(1,10,commands.BucketType.user)
async def cancel(ctx, *args):
    global x
    x = -999999999999999999999


@client.command(pass_context=True, name = 'prequel', help ='wut')
@commands.cooldown(1,10,commands.BucketType.user)
async def bigsmoke(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/prequel/')))
    cliplocation = './Clips/prequel/' + person
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

@client.command(pass_context=True, name = 'meme', help ='The biggest collection of memes since gamble')
@commands.cooldown(1,10,commands.BucketType.user)
async def meme(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/meme/')))
    cliplocation = './Clips/meme/' + person
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

@client.command(pass_context=True, name = 'agent', help ='Agent 14 tells you what to do')
@commands.cooldown(1,10,commands.BucketType.user)
async def agent(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/agent14/')))
    cliplocation = './Clips/agent14/' + person
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

@client.command(pass_context=True, name = 'trevor', help ='Trevor...Phillips...Industries...')
@commands.cooldown(1,10,commands.BucketType.user)
async def trevor(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/trevor/')))
    cliplocation = './Clips/trevor/' + person
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

@client.command(pass_context=True, name = 'lester', help ='Because we do not hear Lester enough')
@commands.cooldown(1,10,commands.BucketType.user)
async def lester(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/lester/')))
    cliplocation = './Clips/lester/' + person
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

@client.command(pass_context=True, name = 'joke', help ='Biggest Laughs')
@commands.cooldown(1,10,commands.BucketType.user)
async def joke(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/bonzi/')))
    cliplocation = './Clips/bonzi/' + person
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

@client.command(pass_context=True, name = 'IASIP', help ='Trashman comes to eat garbage')
@commands.cooldown(1,10,commands.BucketType.user)
async def IASIP(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/IASIP/')))
    cliplocation = './Clips/IASIP/' + person
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

@client.command(pass_context=True, name = 'trump', help ='We gotta build the wall')
@commands.cooldown(1,10,commands.BucketType.user)
async def trump(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/trump/')))
    cliplocation = './Clips/trump/' + person
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
    
@client.command(pass_context=True, name = 'got', help ='BOBBY B to our rescue')
@commands.cooldown(1,10,commands.BucketType.user)
async def got(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/got/')))
    cliplocation = './Clips/got/' + person
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

@client.command(pass_context=True, name = 'fact', help ='Bonzi knows so much')
@commands.cooldown(1,10,commands.BucketType.user)
async def fact(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/facts/')))
    cliplocation = './Clips/fact/' + person
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

@client.command(pass_context=True, name = 'wwe', help ='HULK HOGAN')
@commands.cooldown(1,10,commands.BucketType.user)
async def wwe(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/wwe/')))
    cliplocation = './Clips/wwe/' + person
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

@client.command(pass_context=True, name = 'sports', help ='NICE ON!')
@commands.cooldown(1,10,commands.BucketType.user)
async def sports(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/sports/')))
    cliplocation = './Clips/sports/' + person
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
             "Just die", "I prescribe a midimania to heal", "Maybe think on it a few days", "Rome wasn't built in a day", "The day of reckoning is approaching", "help me"]
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
        await asyncio.sleep(2)
        print('waited')

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
        

@client.command(pass_context=True, name = 'shop' , help ='gotta spend those marcs somewhere')
@commands.cooldown(1,10,commands.BucketType.user)
async def shop(ctx, *args):

    filename = "longtermdata.txt"
    author = ctx.message.author
    
    if (len(args) == 0):
        msg = "here is what we gots to sell"
        await ctx.send(msg)
        embed = discord.Embed(title = "Flumbot's House of Wares!", colour = discord.Colour.from_rgb(0,144,0))
        embed.add_field(name = 'Item 1', value = 'Big Daddy Rhinehart - \n5000 marcs', inline = True)
        embed.add_field(name = 'Item 2', value = 'Pop-tart Gang - \n2500 marcs', inline = True)
        embed.add_field(name = 'Item 3', value = 'Taco Bell Dog - \n1500 marcs', inline = True)
        embed.add_field(name = 'Item 4', value = 'Twitch IRL Streamer - 10000 marcs', inline = False)
        embed.add_field(name = 'Item 5', value = 'Marc - \n10 marcs', inline = True)
        embed.add_field(name = 'Item 6' , value = 'John F. Kennedy - \n1969 marcs', inline = True)
        embed.add_field(name = 'Item 7', value = 'Donald Trump -\n 2020 marcs', inline = True)
        embed.add_field(name = 'Item 8', value = 'A Math Book -\n 200 marcs', inline = True)
        embed.set_footer(text = 'all sales are final, refunds will not be taken')
        embed.set_thumbnail(url = 'https://i.imgur.com/zq7RfIq.gif')
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



@client.command(pass_context=True, name = 'check-in' , help ='check in for daily marcs, only avaliable at 7:00 EDT/EST')
@commands.cooldown(1,10,commands.BucketType.user)
async def checkin(ctx, *args):
    global daily
    filename = "longtermdata.txt"
    today = date.today()
    now = datetime.datetime.now()
    dt_string = now.strftime("%H%M")
    print(dt_string)

    user = str(ctx.message.author)
    channel = ctx.message.author.voice.channel
    
    if (user in daily):
        msg = "I already gave you credit for flum today baka:rage:! Try again tomorrow!"
        await ctx.send(msg)
        return

    if ( (channel == 'Flum') or (channel == 'Heisturbating ( ͡° ͜ʖ ͡°)') ):
        msg = "Can't Fool me :triumph: you aren't even in the voice chat :triumph:"
        await ctx.send(msg)
    elif ((int(dt_string) <= 2200) and (int(dt_string) >= 1900)):
        msg = "Thank you for your service kind stranger! Have some marcs to spend!"
        await ctx.send(msg, tts=True)
        daily.append(user)
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

    
        

##@client.command(pass_context=True, name = 'remind' , help ='flumbot finally reminds you off all those things todo')
##@commands.cooldown(1,10,commands.BucketType.user)
##async def remind(ctx):
##    global data
##    i = 0
##    j = len(data)
##    word = []
##    str1 = ""
##    nice1 = ""
##    time = 0
##    while(j != 0):
##        if (data[i].isdigit()):
##            print (data[i] + 'found it')
##            time = int(data[i])
##            i += 2
##            while (data[i] != ' '):
##                print (data[i] + 'found it')
##                word.append(data[i])
##                i += 1
##        print(data[i])
##        i += 1
##        j -= 1
##        print(str(i) + ' ' + str(j))
##    print(time)
##    print(word)
    
        
@client.command(pass_context=True, name = 'off' , help ='Turn off autopilot :(')
@commands.cooldown(1,10,commands.BucketType.user)
async def off(ctx, *args):
    global pilot
    pilot = 0
    server = ctx.message.guild.voice_client
    await server.disconnect()
    print('autopilot off')

@client.command(pass_context=True, name = 'stop' , help ='Ruin the fun for everyone')
@commands.cooldown(1,10,commands.BucketType.user)
async def stop(ctx, *args):
    global pilot
    pilot = 0
    server = ctx.message.guild.voice_client
    await server.disconnect()


client.run(token)
