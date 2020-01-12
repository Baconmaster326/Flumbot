import discord
import ffmpeg
import asyncio
import random
import time
import os
import pickle
import string
import librosa
import urllib.request
import datetime
import re
import schedule
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
token = 'NTQ5OTk2NDI0NDIzNTM4Njg4.Xa5wag.65OhPogV4EGoncB5tUVnqSKdUSA'
client = commands.Bot(command_prefix = '', case_insensitive = True, )
thankin = open("thank.pickle" , "rb")
thank = int(pickle.load(thankin))
thankin.close()
x = 0
pilot = 0
winners = []
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
                  'Dark Souls', 'World of Warcraf' , 'World O Tank' , 'World O War']
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
                 'Creepy Uncle Lester ;)']          
    msg = str(random.choice(awakelist))
    
    channel = client.get_channel(137921870010777600)
    await channel.send(msg)
    d0 = date(2019, 2 , 26)
    d1 = today
    start  = d1 - d0
    
    if ((int(start.days)%365) == 0):
        x = int(start.days)
        while (x != 0):
            await asyncio.sleep(2)
            msg = "HAPPY FLUM YEAR\nGIVE IT UP FOR " + str((int(start.days)/365)) + " YEAR(s) OF FLUMBOT!!!\n"
            await channel.send(msg,tts=True)
            x -= 1
            
    msg = "Give it up for Day " + str(start.days) + "! Day " + str(start.days) + "!"
    await channel.send(msg)
    


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

#if anyone deletes a message do this I'll have no hidden messages from me
@client.event
async def on_message_delete(message):
    author = str(message.author)
    content = str(message.content)
    msg = 'Ladies and gentlemen, ' + '@' + author + " said, " + \
               content + ", which they promptly deleted. Making them tonight's biggest loser"
    await message.channel.send(msg)

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
        time.sleep (10)

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
        time.sleep(10)

    #thank flumbot for all the hard work he does (now persistent after resets PogChamp)
    if ('good bot') in messagetobot.lower():
        #get thank counter
        #increment by 1
        thank += 1
        #create and send message
        msg = 'Thank :clap: you :clap: are :clap: the :clap:' + str(thank) + 'th :clap: person :clap: to :clap: thank :clap: me. :clap:'
        await message.channel.send(msg)# tts=True)
        #save and dump the new thank counter
        thankout = open("thank.pickle", "wb")
        #lol pickle.dump
        pickle.dump(thank, thankout)
        thankout.close()
        time.sleep (10)

    if ('bad bot') in messagetobot.lower():
        #decrement by 1
        thank -= 1
        #create and send message
        msg = ':rage: You :rage: brought :rage: my :rage: thanks :rage: to :rage: ' + str(thank) + ' :rage: hope :rage: you :rage: feel :rage: good :rage:'
        await message.channel.send(msg)# tts=True)
        #save and dump the new thank counter
        thankout = open("thank.pickle", "wb")
        #lol pickle.dump
        pickle.dump(thank, thankout)
        thankout.close()
        time.sleep (10)

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
        time.sleep (10)

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
        time.sleep (10)

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
        time.sleep(2)
        
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
async def football(ctx):    
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
async def MidiMania(ctx):    
    msg = "It's time to guess that Midi!\nYou'll have 30 seconds to pick the correct song from 4 choices\nPICK ONLY ONE TIME"
    await ctx.send(msg, tts = True)
    await asyncio.sleep(10)
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
    select = random.randint(1,4)
    print(select)
    A = ' '
    B = ' '
    C = ' '
    D = ' '
    #Garbage follows, rewrite this to use random sample instead of random.choice with a bunch of duplicate checking
    if (select == 1):
        A = str(person)
        answer = '\U0001F1E6'
        printable = ':regional_indicator_a:'
        B = str(random.choice(os.listdir('./Clips/MIDI/')))
        if B == A:
            while (B == A):
                B = str(random.choice(os.listdir('./Clips/MIDI/')))
                
        C = str(random.choice(os.listdir('./Clips/MIDI/')))
        if (C == A or C == B):
            while (C == A or C == B):
                C = str(random.choice(os.listdir('./Clips/MIDI/')))
                
        D = str(random.choice(os.listdir('./Clips/MIDI/')))
        if (D == A or D == C or D == B):
            while (D == A or D == C or D == B):
                D = str(random.choice(os.listdir('./Clips/MIDI/')))
    if (select == 2):
        B = str(person)
        answer = '\U0001F1E7'
        printable = ':regional_indicator_b:'
        A = str(random.choice(os.listdir('./Clips/MIDI/')))
        if B == A:
            while (B == A):
                A = str(random.choice(os.listdir('./Clips/MIDI/')))
                
        C = str(random.choice(os.listdir('./Clips/MIDI/')))
        if (C == A or C == B):
            while (C == A or C == B):
                C = str(random.choice(os.listdir('./Clips/MIDI/')))
                
        D = str(random.choice(os.listdir('./Clips/MIDI/')))
        if (D == A or D == C or D == B):
            while (D == A or D == C or D == B):
                D = str(random.choice(os.listdir('./Clips/MIDI/')))
    if (select == 3):
        C = str(person)
        answer = '\U0001F1E8'
        printable = ':regional_indicator_c:'
        B = str(random.choice(os.listdir('./Clips/MIDI/')))
        if B == C:
            while (B == C):
                B = str(random.choice(os.listdir('./Clips/MIDI/')))
                
        A = str(random.choice(os.listdir('./Clips/MIDI/')))
        if (C == A or C == B):
            while (C == A or C == B):
                A = str(random.choice(os.listdir('./Clips/MIDI/')))
                
        D = str(random.choice(os.listdir('./Clips/MIDI/')))
        if (D == A or D == C or D == B):
            while (D == A or D == C or D == B):
                D = str(random.choice(os.listdir('./Clips/MIDI/')))
    if (select == 4):
        D = str(person)
        answer = '\U0001F1E9'
        printable = ':regional_indicator_d:'
        A = str(random.choice(os.listdir('./Clips/MIDI/')))
        if D == A:
            while (D == A):
                A = str(random.choice(os.listdir('./Clips/MIDI/')))
                
        C = str(random.choice(os.listdir('./Clips/MIDI/')))
        if (C == A or C == D):
            while (C == A or C == D):
                C = str(random.choice(os.listdir('./Clips/MIDI/')))
                
        B = str(random.choice(os.listdir('./Clips/MIDI/')))
        if (B == A or B == C or D == B):
            while (B == A or B == C or D == B):
                B = str(random.choice(os.listdir('./Clips/MIDI/')))
    msg = "Was it\n:regional_indicator_a:\t\u21e6\t" + A[:-4] + "\n:regional_indicator_b:\t\u21e6\t" + B[:-4] + "\n:regional_indicator_c:\t\u21e6\t" + C[:-4] + "\n:regional_indicator_d:\t\u21e6\t" + D[:-4]
    message = await ctx.send(msg)
    await message.add_reaction('\U0001F1E6')
    await message.add_reaction('\U0001F1E7')
    await message.add_reaction('\U0001F1E8')
    await message.add_reaction('\U0001F1E9')
    await asyncio.sleep(30)
    msg = "The correct answer was " + printable + "\n\nCongratulations to:\n"
    await ctx.send(msg , tts = True)
    if ('Baconmaster#3725' in winners):
        await message.channel.send(file=discord.File('./Pics/bacon.png'))
    if ('BOOF#4284' in winners):
        await message.channel.send(file=discord.File('./Pics/beef.png'))
    if ('ratbuddy#9913' in winners):
        await message.channel.send(file=discord.File('./Pics/ratto.png'))
    # why is this an elif? shadow should be treated like everyone else.. also rewrite to use a list of players
    # instead of hardcoding everyone
    elif ('ShadowXII#7240' in winners):
        await message.channel.send(file=discord.File('./Pics/horse.png'))
    #elif winners:
        #await ctx.send('\n'.join(map(str, winners)))
    # next should not be an else, should be an if that checks count of winners
    else:
        await message.channel.send(file=discord.File('./Pics/flumbus.png'))
    msg = "\n:clap::clap::clap::clap::clap::clap:\n"
    await ctx.send(msg, tts = True)
    winners.clear()
    

@client.command(pass_context=True, name = 'bruh', help ='For the bruh moments in our lives')
@commands.cooldown(1,10,commands.BucketType.user)
async def bruh(ctx):
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
async def baba(ctx):
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
async def thomas(ctx):
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
async def fridge(ctx):
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
async def clap(ctx):
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
async def keyboard(ctx):
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
async def chum(ctx):
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
async def knock(ctx):
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
async def cocaine(ctx):
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
async def futbol(ctx):
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
async def gamble(ctx):
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
async def spongebob(ctx):
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
async def alexjones(ctx):
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
async def ramsay(ctx):
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
async def gleib(ctx):
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
async def bigsmoke(ctx):
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
async def cancel(ctx):
    global x
    x = -999999999999999999999


@client.command(pass_context=True, name = 'prequel', help ='wut')
@commands.cooldown(1,10,commands.BucketType.user)
async def bigsmoke(ctx):
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
async def meme(ctx):
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
async def agent(ctx):
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
async def trevor(ctx):
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
async def lester(ctx):
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
async def joke(ctx):
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
async def IASIP(ctx):
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
async def trump(ctx):
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
async def got(ctx):
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
async def fact(ctx):
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
async def wwe(ctx):
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
async def sports(ctx):
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
async def surprise(ctx):
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

@client.command(pass_context=True, name = 'autopilot', help ='Let flumbot gamble his life away')
@commands.cooldown(1,10,commands.BucketType.user)
async def autopilot(ctx):
    global pilot
    pilot = 1
    timer = 0
    msg = 'AutoPilot engaged, to turn off type "off"'
    await ctx.send(msg)
    while (pilot == 1):
        if (timer > 2500):
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


        
@client.command(pass_context=True, name = 'off' , help ='Turn off autopilot :(')
@commands.cooldown(1,10,commands.BucketType.user)
async def off(ctx):
    global pilot
    pilot = 0
    print('autopilot off')

@client.command(pass_context=True, name = 'stop' , help ='Ruin the fun for everyone')
@commands.cooldown(1,10,commands.BucketType.user)
async def stop(ctx):
    await ctx.voice_client.disconnect()


client.run(token)
