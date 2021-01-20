from __future__ import unicode_literals
import discord
import asyncio
import random
import os
import datetime
import miditoaudio
import basics
import daystart
import messager
import backup
import voicememe
import librosa
import json
import psutil
import pathlib
from discord.ext.commands import CommandNotFound
from PIL import Image, ImageFont, ImageDraw
from gtts import gTTS
from discord.ext import commands
from datetime import date

# import big_smoke#
# import mad marc#

today = date.today()
now = datetime.datetime.now()
token = 'notokentoday'
client = commands.Bot(command_prefix='', case_insensitive=True, )
x = 0
pilot = 0
skip = 0
username = 'urmum'
data = []
winners = []
cheaters = []
answer = ':a:'


# Things flumbot does on startup
@client.event
async def on_ready():
    print('---------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------')
    
    os.chdir(str(os.environ['USERPROFILE'] + "\Desktop\Flumbot"))

    altfilename = './bin/en_data/longtermdata.json'

    with open(altfilename, "r") as file:
        data = json.load(file)
    await client.change_presence(activity=daystart.activity())
    if daystart.datecheck() == 0:
        print('\n-----already spammed chat today do not send wake message-----\n')
        return
    
    await daystart.profile(client)
    link = daystart.link()

    for channel in data['dayvalues']['channels']:
        channel = client.get_channel(channel)
        deltaday = daystart.days()
        if (deltaday % 365) == 0:
            x = deltaday
            while x != 0:
                await asyncio.sleep(2)
                msg = "HAPPY FLUM YEAR\nGIVE IT UP FOR " + str(deltaday / 365) + " YEAR(s) OF FLUMBOT!!!\n"
                await channel.send(msg, tts=True)
                print('wrong')
                x -= 1
        if (deltaday % 30) == 0:
            user = await client.fetch_user(100562084894371840)
            await backup.backup(user)
        msg = daystart.awake()
        await channel.send(msg)
        msg = "Give it up for Day " + str(deltaday) + "! Day " + str(deltaday) + "!"
        await channel.send(msg)
        await channel.send(file=discord.File(link))

    os.remove(link)


# if anyone deletes a message do this I'll have no hidden messages from me
@client.event
async def on_message_delete(message):
    author = str(message.author)
    content = str(message.content)
    if content.lower() in 'roulette random common rare strange legendary flumbot pot keep start stop ready! skip flum game start inventory shop name color pass':
        return
    if author == 'Flumbot#1927':
        return
    msg = 'Ladies and gentlemen, ' + '@' + author + " said, '" + content + "', which they promptly deleted. Making them tonight's biggest loser"
    await message.channel.send(msg)


@client.event
async def on_guild_remove(guild):
    print('we lost one :(')
    await basics.killed(client, guild)

@client.event
async def on_guild_join(guild):
    print('we got a new one boys!!!!!!')
    await basics.welcome(client, guild)

@client.event
async def on_typing(channel, user, when):
    name = str(user)
    name = name[:-5]
    print("waiting for typing")

    def check(m):
        return user == user
    
    try:
        await client.wait_for('message', check=check, timeout=90)
    except asyncio.TimeoutError:
        msg = "finish typing " + name + ", we are all waiting :)"
        await channel.send(msg)
    return


@client.event
async def on_reaction_add(reaction, user):
    global winners
    global answer
    global cheaters
    if str(user) in winners or str(user) in cheaters:
        print(str(user) + ' already answered')
        return
    if str(user) == 'Flumbot#1927':
        return
    if answer == reaction.emoji:
        winners.append(str(user))
        return
    cheaters.append(str(user))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    messagetobot = str(message.content)
    splitme = str(messagetobot.lower())
    global username
    global dater
    dater = messagetobot
    username = str(message.author)
    username = username[:-5]
    print(username + " said " + message.content + "\nin #" + message.channel.name + " || " + message.channel.guild.name )
    print("\n-----reading message-----\n")
    
    msg, flag = messager.check(splitme)
    if msg != 'oop':
        await message.channel.send(msg, tts=flag)

    # Do you have a clear vision?
    if 'i see' in messagetobot.lower():
        await message.channel.send(file=discord.File('./Pics/doyou.png'))
        await asyncio.sleep(5)
        await message.channel.send(file=discord.File('./Pics/hedo.png'))

    if 'default dance' in messagetobot.lower():
        await messager.default_dance(message,client)

    if 'hey peter' in messagetobot.lower():
        await messager.peter(message)

    if 'ok marc' in messagetobot.lower():
        await message.channel.send('ok marc', tts = True)
        
    # never forget when :b: was standard
    if 'b-time' in messagetobot.lower():
        msg = 'Its :b:o time'
        frythis = 'b'
        await message.channel.send(msg)  # tts=True)
        if frythis in messagetobot:
            msg = messagetobot
            msg2 = msg.replace('b', ':b:')
            await message.channel.send(msg2)  # tts=True)

    if 'trigger self destruct flumbot code 8675309' in messagetobot.lower():
        msg = '\n Type cancel to cancel the self destruct! \n'
        await message.channel.send(msg, tts=True)
        msg = ':rage: :100: :ok_hand:'
        global x
        x = 1
        while x > 0:
            await message.channel.send(msg, tts=True)
            x += 1

    if len(message.content.split()) == 1:
        try:
            print(username + " is attempting to continue the count with the number " + str(int(message.content)))
            altfilename = './bin/en_data/longtermdata.json'
            username = str(message.author)
            with open(altfilename, "r") as file:
                data = json.load(file)
            filename = './bin/en_data/userdata.json'
            with open(filename, "r") as file:
                userdata = json.load(file)
            if data["count"][0] != username:
                if int(message.content) == data["count"][1] + 1:
                    data["count"][0] = username
                    data["count"][1] = int(message.content)
                    if data["count"][2] < int(message.content):
                        await message.add_reaction('🏆')
                        data["count"][2] = int(message.content)
                    try:
                        userdata[username]["score"] = userdata[username]["score"] + int(message.content)
                    except KeyError:
                        try:
                            userdata[username]["score"] = int(message.content)
                        except KeyError:
                            userdata[username] = {}
                            userdata[username]["score"] = int(message.content)
                    with open('./bin/en_data/emoji.json', "r", encoding="utf8") as file:
                        emoji = json.load(file)
                    key = list(emoji.keys())
                    key = random.choice(key)
                    emoji = random.choice(emoji[key])['emoji']
                    while emoji == '💦':
                        key = list(emoji.keys())
                        key = random.choice(key)
                        emoji = random.choice(emoji[key])['emoji']
                    await message.add_reaction(emoji)
                else:
                    await message.channel.send(username[:-5] + " ruined the count at " + str(data["count"][1]) + ". They typed the wrong number!")
                    data["count"][0] = "Flumbot#1927"
                    data["count"][1] = 0
                    await message.add_reaction('💦')
                    try:
                        userdata[username]["score"] = userdata[username]["score"] - data["count"][1]
                    except KeyError:
                        try:
                            userdata[username]["score"] = 0
                        except KeyError:
                            userdata[username] = {}
                            userdata[username]["score"] = 0
            else:
                await message.channel.send(username[:-5] + " ruined the count at " + str(data["count"][1]) + ". They counted twice...")
                data["count"][0] = "Flumbot#1927"
                data["count"][1] = 0
                await message.add_reaction('💦')
                try:
                    userdata[username]["score"] = userdata[username]["score"] - data["count"][1]
                except KeyError:
                    try:
                        userdata[username]["score"] = 0
                    except KeyError:
                        userdata[username] = {}
                        userdata[username]["score"] = 0

            with open(filename, "w") as file:
                json.dump(userdata, file)
            with open(altfilename, "w") as file:
                json.dump(data, file)
        except ValueError:
            print("not a number, continuing")




    print("\n-----No specific phrases said, proceed to read commands-----\n")
    await client.process_commands(message)

    ###################################
    # End Text commands                #
    # Proceed to complex voice commands#
    ###################################


@client.command(pass_context=True, name='football', help='The new John Madden game sounds pretty good.')
@commands.cooldown(1, 10, commands.BucketType.user)
async def football(ctx, *args):
    msg = "HI EVERYONE AND WELCOME TO JOHN MADDEN FOOTBALL!!!"
    await ctx.send(msg)
    cliplocation = './Clips/Oneoff/Futbol.mp3'
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='MidiMania', help='The hit new game hosted by yours truly')
@commands.cooldown(1, 10, commands.BucketType.user)
async def MidiMania(ctx, *args):
    global cheaters
    cheaters.clear()
    global answer
    answer, printable = await voicememe.midimania(ctx, client)
    await asyncio.sleep(30)
    global winners
    await voicememe.winnerlist(ctx, client, winners, printable, 25)
    winners.clear()
    return


@client.command(pass_context=True, name='MidiManiaDX',
                help='You may have conquered regular midimania, but can you do midimania deluxe???')
@commands.cooldown(1, 10, commands.BucketType.user)
async def MidiManiaDX(ctx, *args):
    global cheaters
    cheaters.clear()
    global answer
    answer, printable = await voicememe.midimaniadx(ctx, client)
    await asyncio.sleep(30)
    global winners
    await voicememe.winnerlist(ctx, client, winners, printable, 35)
    winners.clear()
    return


@client.command(pass_context=True, name='bruh', help='For the bruh moments in our lives')
@commands.cooldown(1, 10, commands.BucketType.user)
async def bruh(ctx, *args):
    cliplocation = './Clips/Oneoff/bruh.mp3'
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='baba', help='Meaty Chairs and Baba Yetus')
@commands.cooldown(1, 10, commands.BucketType.user)
async def baba(ctx, *args):
    cliplocation = './Clips/Oneoff/babayeet.mp3'
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='thomas', help='Thomas coming through')
@commands.cooldown(1, 10, commands.BucketType.user)
async def thomas(ctx, *args):
    cliplocation = './Clips/Oneoff/thomas.mp3'
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='fridge', help='Classico Flumico')
@commands.cooldown(1, 10, commands.BucketType.user)
async def fridge(ctx, *args):
    cliplocation = './Clips/Oneoff/oof.mp3'
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='clap', help='clap')
@commands.cooldown(1, 10, commands.BucketType.user)
async def clap(ctx, *args):
    cliplocation = './Clips/Oneoff/clap.mp3'
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='keyboard', help='I hear a keyboard round here')
@commands.cooldown(1, 10, commands.BucketType.user)
async def keyboard(ctx, *args):
    cliplocation = './Clips/Oneoff/keyboard.mp3'
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='chum', help='Gnot for the weak of heart')
@commands.cooldown(1, 10, commands.BucketType.user)
async def chum(ctx, *args):
    msg = ":tired_face: You've been gnomed! :tired_face:"
    cliplocation = './Clips/Oneoff/gnome.mp3'
    await ctx.send(msg)
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='knock', help='Who is it? MonkaS')
@commands.cooldown(1, 10, commands.BucketType.user)
async def knock(ctx, *args):
    cliplocation = './Clips/Oneoff/knock.mp3'
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='cocaine', help='I am Impotent Rage')
@commands.cooldown(1, 10, commands.BucketType.user)
async def cocaine(ctx, *args):
    msg = "Okay Mr.Phillips"
    await ctx.send(msg)
    cliplocation = './Clips/Oneoff/trevor.mp3'
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='futbol', help='A modern spin on a classic clip')
@commands.cooldown(1, 10, commands.BucketType.user)
async def futbol(ctx, *args):
    msg = "HI EVERYONE AND WELCOME TO JOHN MADDEN FOOT!"
    await ctx.send(msg)
    cliplocation = './Clips/Oneoff/Fut.mp3'
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='gamble', help='House always wins')
@commands.cooldown(1, 10, commands.BucketType.user)
async def gamble(ctx, *args):
    mp3files = []
    for dirpath, subdirs, files in os.walk('./Clips'):
        for x in files:
            if x.endswith(".mp3"):
                mp3files.append(os.path.join(dirpath, x))
    cliplocation = random.choice(mp3files)
    print(cliplocation)
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='spongebob', help='You gotta lick the Marble')
@commands.cooldown(1, 10, commands.BucketType.user)
async def spongebob(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/spongebob/')))
    cliplocation = './Clips/spongebob/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='funny', help='listen to what other people think is funny')
@commands.cooldown(1, 10, commands.BucketType.user)
async def usersub(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/usersub/')))
    cliplocation = './Clips/usersub/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='alexjones', help='Alex Jones screams about walruses')
@commands.cooldown(1, 10, commands.BucketType.user)
async def alexjones(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/alexjones/')))
    cliplocation = './Clips/alexjones/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='ramsay', help='Gordon Ramsay enlightens the chat')
@commands.cooldown(1, 10, commands.BucketType.user)
async def ramsay(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/ramsay/')))
    cliplocation = './Clips/ramsay/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='gleib', help='This is your Idiotest')
@commands.cooldown(1, 10, commands.BucketType.user)
async def gleib(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/gleib/')))
    cliplocation = './Clips/gleib/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='bigsmoke', help='Big Smoke gets Philisophical')
@commands.cooldown(1, 10, commands.BucketType.user)
async def bigsmoke(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/bigsmoke/')))
    cliplocation = './Clips/bigsmoke/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='prequel', help='wut')
@commands.cooldown(1, 10, commands.BucketType.user)
async def prequel(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/prequel/')))
    cliplocation = './Clips/prequel/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='meme', help='The biggest collection of memes since gamble')
@commands.cooldown(1, 10, commands.BucketType.user)
async def meme(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/meme/')))
    cliplocation = './Clips/meme/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='agent', help='Agent 14 tells you what to do')
@commands.cooldown(1, 10, commands.BucketType.user)
async def agent(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/agent14/')))
    cliplocation = './Clips/agent14/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='trevor', help='Trevor...Phillips...Industries...')
@commands.cooldown(1, 10, commands.BucketType.user)
async def trevor(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/trevor/')))
    cliplocation = './Clips/trevor/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='lester', help='Because we do not hear Lester enough')
@commands.cooldown(1, 10, commands.BucketType.user)
async def lester(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/lester/')))
    cliplocation = './Clips/lester/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='joke', help='Biggest Laughs')
@commands.cooldown(1, 10, commands.BucketType.user)
async def joke(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/bonzi/')))
    cliplocation = './Clips/bonzi/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='IASIP', help='Trashman comes to eat garbage')
@commands.cooldown(1, 10, commands.BucketType.user)
async def IASIP(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/IASIP/')))
    cliplocation = './Clips/IASIP/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='trump', help='We gotta build the wall')
@commands.cooldown(1, 10, commands.BucketType.user)
async def trump(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/trump/')))
    cliplocation = './Clips/trump/' + person
    if await voicememe.playclip(cliplocation, ctx, client, 0) == False and len(args) > 0:
        msg = "Everybody enjoys your political opinion :)"
        await ctx.send(msg, tts = True)
        await asyncio.sleep(10)
        msg = "Oh wait..."
        await ctx.send(msg, tts = True)
        await asyncio.sleep(4)
        msg = "Nobody cares :("
        await ctx.send(msg, tts = True)


@client.command(pass_context=True, name='got', help='BOBBY B to our rescue')
@commands.cooldown(1, 10, commands.BucketType.user)
async def got(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/got/')))
    cliplocation = './Clips/got/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='fact', help='Bonzi knows so much')
@commands.cooldown(1, 10, commands.BucketType.user)
async def fact(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/facts/')))
    cliplocation = './Clips/fact/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='wwe', help='HULK HOGAN')
@commands.cooldown(1, 10, commands.BucketType.user)
async def wwe(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/wwe/')))
    cliplocation = './Clips/wwe/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True, name='sports', help='NICE ON!')
@commands.cooldown(1, 10, commands.BucketType.user)
async def sports(ctx, *args):
    person = str(random.choice(os.listdir('./Clips/sports/')))
    cliplocation = './Clips/sports/' + person
    await voicememe.playclip(cliplocation, ctx, client, 0)


@client.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def surprise(ctx, *args):
    msg = daystart.link()
    await ctx.send(msg)


@client.command(pass_context=True, name='autopilot', help='Let flumbot gamble his life away')
@commands.cooldown(1, 10, commands.BucketType.user)
async def autopilot(ctx, *args):
    global pilot
    pilot = 1
    timer = 0
    msg = 'AutoPilot engaged, to turn off type "off"'
    await ctx.send(msg)
    while (pilot == 1):
        if (timer > 800):
            timer = 0
            continue
        await asyncio.sleep(timer)
        if (pilot == 0):
            return
        mp3files = []
        for dirpath, subdirs, files in os.walk('./Clips'):
            for x in files:
                if x.endswith(".mp3"):
                    mp3files.append(os.path.join(dirpath, x))
        cliplocation = random.choice(mp3files)
        print(cliplocation)
        duration = librosa.get_duration(filename=cliplocation) + 1
        await voicememe.playclip(cliplocation, ctx, client, 0)
        timer = timer + random.randint(30, 100)
        print ("waiting " + str(timer) + " seconds, before next clip")
                


@client.command(pass_context=True, name='tts', help='For the blind or those without a second monitor')
@commands.cooldown(1, 10, commands.BucketType.user)
async def tts(ctx, *args):
    global pilot
    global username
    global dater
    filename = './bin/en_data/longtermdata.json'
    with open(filename, "r") as file:
        data = json.load(file)
    pilot = 1
    while pilot > 0:
        with open(filename, "r") as file:
            data = json.load(file)
        text = username + ' said...' + dater
        if dater == 'tts':
            continue
        data['dayvalues']['tts'].append(text)
        if len(data['dayvalues']['tts']) > 0:
            text = data['dayvalues']['tts'][0]
            speech = gTTS(text=text, lang='en-ca', slow=False)
            speech.save("text.mp3")
            await voicememe.playclip('text.mp3', ctx, client, 0)
            os.remove('text.mp3')
            data['dayvalues']['tts'].remove(data['dayvalues']['tts'][0])
        else:
            dater = 'tts'
            asyncio.sleep(2)
        with open(filename, "w") as file:
            json.dump(data, file)

@client.command(pass_context=True, name='restart', help='kill flumbot only to make him stronger')
@commands.cooldown(1, 10, commands.BucketType.user)
async def restart(ctx, *args):
    os.startfile('restart.py')
    exit()


@client.command(pass_context=True, name='8-ball', help='let flumbot make the decisions now')
@commands.cooldown(1, 10, commands.BucketType.user)
async def ball(ctx, *args):
    await basics.fortune(ctx, client)


@client.command(pass_context=True, name='music', help='lo-fi hiphop beats to relax/study to')
@commands.cooldown(1, 10, commands.BucketType.user)
async def music(ctx, *args):
    global pilot
    pilot = 1
    while (pilot == 1):
        midifiles = []
        for dirpath, subdirs, files in os.walk('./Music/MIDI'):
            for x in files:
                if x.endswith(".mid"):
                    midifiles.append(os.path.join(dirpath, x))
        cliplocation = random.choice(midifiles)
        miditoaudio.to_audio('./Music/OPL2.sf2', cliplocation, './', out_type='wav')
        person = os.path.split(cliplocation)
        person = person[1]
        place = str(person[:-4]) + '.wav'
        if await voicememe.playclip(place, ctx, client, 0) == False:
            print("they ain't in voice chat boss")
            os.remove(place)
            pilot = 0
            return
        await asyncio.sleep(2)
        os.remove(place)
        print('waited, playing next song')


@client.command(pass_context=True, name='inventory', help='checkout your cool stuff')
@commands.cooldown(1, 10, commands.BucketType.user)
async def inventory(ctx, *args):
    await basics.checkinv(ctx, client)


@client.command(pass_context=True, name='flum', help='type flum help for full list of commands')
async def flumstatus(ctx, *args):
    lister = list(args)
    await basics.check(ctx, client, lister)


@client.command(pass_context=True, name='shop', help='gotta spend those marcs somewhere')
@commands.cooldown(1, 10, commands.BucketType.user)
async def shop(ctx, *args):
    await basics.shopfront(ctx, client, args)


@client.command(pass_context=True, name='flip', help='flip a standard US coin')
@commands.cooldown(1, 10, commands.BucketType.user)
async def flip(ctx, *args):
    x = list(args)
    if ('coin' in x):
        if (random.randint(0, 1) == 1):
            result = 'Heads'
        else:
            result = 'Tails'
        msg = 'Flipping...'
        await ctx.send(msg, tts=True)
        await asyncio.sleep(4)
        msg = 'Coin is ' + result + ' side up.'
        await ctx.send(msg, tts=True)


@client.command(pass_context=True, name='roll', help='roll any dice flumbot has')
async def roll(ctx, *args):
    await basics.rollthedice(ctx, args)


@client.command(pass_context=True, name='check-in', help='check in for daily marcs, only avaliable at 7:00 EDT/EST')
@commands.cooldown(1, 10, commands.BucketType.user)
async def checkin(ctx, *args):
    await basics.daily(ctx)

@client.command(pass_context=True, name='revel', help='OK Gamers')
@commands.cooldown(1, 10, commands.BucketType.user)
async def revel(ctx, *args):
    await voicememe.youtubelink(ctx,client)

@client.command(pass_context=True, name='geddit', help="Let's GEDDIT")
@commands.cooldown(1, 10, commands.BucketType.user)
async def geddit(ctx, *args):
    global cheaters
    cheaters.clear()
    global answer
    answer, printable, link = await voicememe.geddit(ctx, client)
    await asyncio.sleep(30)
    global winners
    await voicememe.winnerlist(ctx, client, winners, printable, 25)
    msg = "The post was <" + link + ">"
    await ctx.send(msg)
    winners.clear()
    return

@client.command(pass_context=True, name='gedditdx', help="Let's GEDDITDX")
@commands.cooldown(1, 10, commands.BucketType.user)
async def gedditdx(ctx, *args):
    args = list(args)
    args = ''.join(args)
    if len(args) < 1:
        msg ="use the format 'gedditdx (subreddit)'"
        await ctx.send(msg)
        return
    global cheaters
    cheaters.clear()
    global answer
    answer, printable = await voicememe.gedditdx(ctx, client, args)
    await asyncio.sleep(30)
    global winners
    await voicememe.winnerlist(ctx, client, winners, printable, 35)
    winners.clear()
    return

@client.command(pass_context=True, name='off', help='Turn off autopilot :(')
@commands.cooldown(1, 10, commands.BucketType.user)
async def off(ctx, *args):
    global pilot
    pilot = 0
    server = ctx.message.guild.voice_client
    try:
        await server.disconnect()
    except AttributeError:
        return
    print('autopilot off')


@client.command(pass_context=True, name='cancel', help='null')
@commands.cooldown(1, 10, commands.BucketType.user)
async def cancel(ctx, *args):
    global x
    x = -999999999999999999999


@client.command(pass_context=True, name='start', help='startup the minecraft server')
@commands.cooldown(1, 10, commands.BucketType.user)
async def start(ctx, *args):
    processName = 'cmd'
    count = []
    if ('minecraft' in args or 'server' in args or 'modded' in args): 
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if processName.lower() in proc.name().lower():
                    count.append(proc.name().lower())
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        if len(count) > 1:
            msg = "Server is currently starting, or running\nYou better go catch it!"
            await ctx.send(msg)
            return
        else:
            msg = "Starting the server now...\nShould be about 1 minute to start!"
            await ctx.send(msg)
            if 'modded' in args:
                await ctx.send("try to remember to type 'stop server' when done playing!")
                try:
                    path = str(os.environ['USERPROFILE'] + "\Desktop\MMCSERVER\go.bat")
                    print(path)
                    os.startfile(path)
                    def checkm(m):
                        return (m.content.lower() == 'stop server' or m.content.lower() == 'keep playing')

                    while 1:
                        try:
                            message = await client.wait_for('message', check=checkm, timeout=7200)
                            if str(message.content.lower()) == "stop server":
                                os.system("TASKKILL /F /IM java.exe")
                                await ctx.send("Server killed, type start modded server to restart")
                                return
                        except asyncio.TimeoutError:
                            await ctx.send("@"+str(ctx.message.author)+" I'm stopping the server in 2 minutes, please wait for the server to die, before typing start modded server again")
                            await asyncio.sleep(180)
                            os.system("TASKKILL /F /IM java.exe")
                            await ctx.send("Server killed, type start modded server to restart")
                            return
                except OSError:
                    msg = "This feature isn't working right now @me"
                    await ctx.send(msg)
                    return
            try:
                os.startfile("start.bat")
            except OSError:
                msg = "This feature isn't working right now @me"
                await ctx.send(msg)
                return
        return
   

    


    
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


client.run(token)
