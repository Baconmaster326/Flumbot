import asyncio
import threading
import datetime
import discord
import requests
import logging
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from datetime import date
import check_raw_text
import check_count
import generativeai
import voiceplay
import os
import json
import random
import games
import daystart
import shutil
import psutil
import yt_dlp
import platform

# start Discord client
client = commands.Bot(command_prefix='', intents=discord.Intents.all(), case_insensitive=True)

# setup logging
logging.basicConfig(handlers=[logging.FileHandler('debug.log')], level=logging.DEBUG)
logger = logging.getLogger()
logger.debug(f"Logger Initialized for {datetime.time()}")

# globals for autopilot
pilot = 0
dev = 0

# Grab discord api token
with open('token.json', "r") as file:
    data = json.load(file)
token = data['token'][0]

if platform.system() == 'Windows':
    print("You're in the testing environment")
    dev = 1

@client.event
async def on_ready():
    print('---------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------')
    await client.tree.sync()
    print("Synced commands list")

    if dev:
        return

    altfilename = './data/longtermdata.json'

    with open(altfilename, "r") as file:
        data = json.load(file)
    # flavortext change
    await client.change_presence(activity=await daystart.activity())
    # we started today already?
    if daystart.datecheck() == 0:
        print('\n-----already spammed chat today do not send wake message-----\n')
        return

    #  change profile picture
    await daystart.profile(client)

    # for each channel we a part of
    for channel in data['dayvalues']['channels']:
        channel = client.get_channel(channel)
        deltaday = daystart.days()
        # flum new year process
        if (deltaday % 365) == 0:
            msg = "HAPPY FLUM YEAR\nGIVE IT UP FOR " + str(deltaday / 365) + " YEAR(s) OF FLUMBOT!!!\n"
            await channel.send(msg, tts=True)

        # send random awake message
        msg = daystart.awake()
        await channel.send(msg)
        msg = f"Give it up for Day {deltaday}! Day {deltaday}!"
        await channel.send(msg)
        #send random reddit, 4chin, or pixiv link
        link = await daystart.makelink()
        await channel.send(file=discord.File(link))
        await daystart.quip_image(channel, link)
        os.remove(link)
     


@client.event
async def on_message(message):
    messagetobot = str(message.content)
    user = str(message.author)
    channel = message.channel.name
    guild = message.channel.guild.name

    if message.author == client.user:
        if "hey flumbot" in messagetobot.lower():
            print("new awake rule to add")
        else:
            return

    if message.type.name == "reply" and message.reference.resolved.author == client.user:        #are we being @'d?
        message.content = "hey flumbot, " + message.content


    print(f"=========\n{user} said {messagetobot} in {channel} || {guild}\nchecking for commands...")

    print("\n=====Nothing else found, proceed to read commands=====\n")

    await check_raw_text.parse(message)

    if len(str(message.content).split()) == 1:
        await check_count.parse(message)


    await client.process_commands(message)

@client.hybrid_command(name = "midimania", description= "The hit new game hosted by yours truly", pass_context= True)
async def Midimania(ctx):
    await games.midimania(ctx, client)

@client.hybrid_command(name = "midimaniadx", description= "The spin on the hit new game hosted by yours truly",
                       pass_context= True)
async def MidimaniaDX(ctx):
    await games.midimania(ctx, client, True)

@client.hybrid_command(name = "geddit", description= "Let's GEDDIT", pass_context= True)
async def Geddit(ctx):
    await games.geddit(ctx, client)

@client.hybrid_command(name = "gedditdx", description= "Let's GEDDITDX", pass_context= True)
async def GedditDX(ctx, subreddit):
    if len(subreddit) == 0:
        subreddit = 'all'
    await games.gedditdx(ctx, client, subreddit)

@client.hybrid_command(name = "gamble", description= "House always wins", pass_context= True)
async def gamble(ctx):
    mp3files = []
    for dirpath, subdirs, files in os.walk('./Clips'):
        for x in files:
            if x.endswith(".mp3") or x.endswith(".wav"):
                mp3files.append(os.path.join(dirpath, x))
    cliplocation = random.choice(mp3files)
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name = "autopilot", description= "Let flumbot gamble his life away", pass_context= True)
async def autopilot(ctx):
    global pilot
    pilot = 1
    timer = 0
    await ctx.send("Autopilot engaged, to turn off type 'off'", ephemeral=True, delete_after=3)
    mp3files = []
    for dirpath, subdirs, files in os.walk('./Clips'):
        for x in files:
            if x.endswith(".mp3") or x.endswith(".wav"):
                mp3files.append(os.path.join(dirpath, x))
    while pilot == 1:
        if timer > 800:
            timer = 0
            continue
        await asyncio.sleep(timer)
        if pilot == 0:
            return
        cliplocation = random.choice(mp3files)
        await voiceplay.playclip(cliplocation, ctx, client, 0)
        timer = timer + random.randint(30, 100)
        print(f"waiting {timer} seconds before next clip :)")

@client.hybrid_command(name = "8-ball", description= "let flumbot make the decisions now", pass_context= True)
async def ball(ctx):
    await check_raw_text.fortune(ctx)

@client.hybrid_command(name = "off", description= "Turn off autopilot :(", pass_context= True)
async def off(ctx):
    global pilot
    pilot = 0
    server = ctx.guild.voice_client
    try:
        await server.disconnect()
    except AttributeError:
        print("he wasn't in a voice channel")
    await ctx.send("I'm going to <@100562084894371840> on you", ephemeral=True, delete_after=3)
    print('autopilot off')

@client.hybrid_command(name = "football", description= "The new John Madden game sounds pretty good.", pass_context= True)
async def football(ctx):
    await ctx.send("HI EVERYONE AND WELCOME TO JOHN MADDEN FOOTBALL!!!", delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/Futbol.mp3', ctx, client, 0)

@client.hybrid_command(name='bruh', description='For the bruh moments in our lives', pass_context=True)
async def bruh(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/bruh.mp3', ctx, client, 0)

@client.hybrid_command(name='baba', description='Meaty Chairs and Baba Yetus', pass_context=True)
async def baba(ctx):
    await ctx.send("you got it boss", delete_after=float(10), ephemeral=True)
    await voiceplay.playclip('./Clips/Oneoff/babayeet.mp3', ctx, client, 0)

@client.hybrid_command(name='thomas', description='Thomas coming through', pass_context=True)
async def thomas(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/thomas.mp3', ctx, client, 0)

@client.hybrid_command(name='fridge', description='Classico Flumico', pass_context=True)
async def fridge(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/oof.mp3', ctx, client, 0)

@client.hybrid_command(name='clap', description='clap', pass_context=True)
async def clap(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/clap.mp3', ctx, client, 0)

@client.hybrid_command(name='keyboard', description='I hear a keyboard round here', pass_context=True)
async def keyboard(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/keyboard.mp3', ctx, client, 0)

@client.hybrid_command(name='chum', description='Gnot for the weak of heart', pass_context=True)
async def chum(ctx):
    await ctx.send(":tired_face: You've been gnomed! :tired_face:", delete_after=float(10), tts=True)
    await voiceplay.playclip('./Clips/Oneoff/chum.mp3', ctx, client, 0)

@client.hybrid_command(name='knock', description='Who is it? MonkaS', pass_context=True)
async def knock(ctx):
    await ctx.send("monster", ephemeral=True, delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/knock.mp3', ctx, client, 0)

@client.hybrid_command(name='cocaine', description='I am Impotent Rage', pass_context=True)
async def cocaine(ctx):
    await ctx.send("Okay Mr. Phillips", ephemeral=True, delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/trevor.mp3', ctx, client, 0)

@client.hybrid_command(name='futbol', description='A modern spin on a classic clip', pass_context=True)
async def futbol(ctx):
    await ctx.send("HI EVERYONE AND WELCOME TO JOHN MADDEN FOOT!", delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/Fut.mp3', ctx, client, 0)

@client.hybrid_command(name='spongebob', description='You gotta lick the Marble', pass_context=True)
async def spongebob(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/spongebob/')))
    cliplocation = './Clips/spongebob/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='funny', description='listen to what other people think is funny', pass_context=True)
async def usersub(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/usersub/')))
    cliplocation = './Clips/usersub/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='alexjones', description='Alex Jones screams about walruses', pass_context=True)
async def alexjones(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/alexjones/')))
    cliplocation = './Clips/alexjones/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='ramsay', description='Gordon Ramsay enlightens the chat', pass_context=True)
async def ramsay(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/ramsay/')))
    cliplocation = './Clips/ramsay/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='gleib', description='This is your Idiotest', pass_context=True)
async def gleib(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/gleib/')))
    cliplocation = './Clips/gleib/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='bigsmoke', description='Big Smoke gets Philisophical', pass_context=True)
async def bigsmoke(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/bigsmoke/')))
    cliplocation = './Clips/bigsmoke/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='prequel', description='wut', pass_context=True)
async def prequel(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/prequel/')))
    cliplocation = './Clips/prequel/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='meme', description='The biggest collection of memes since gamble', pass_context=True)
async def meme(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/meme/')))
    cliplocation = './Clips/meme/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='agent', description='Agent 14 tells you what to do', pass_context=True)
async def agent(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/agent14/')))
    cliplocation = './Clips/agent14/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='trevor', description='Trevor...Phillips...Industries...', pass_context=True)
async def trevor(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/trevor/')))
    cliplocation = './Clips/trevor/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='lester', description='Because we do not hear Lester enough', pass_context=True)
async def lester(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/lester/')))
    cliplocation = './Clips/lester/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='joke', description='Biggest Laughs', pass_context=True)
async def joke(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/joke/')))
    cliplocation = './Clips/joke/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='iasip', description='Trashman comes to eat garbage', pass_context=True)
async def IASIP(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/IASIP/')))
    cliplocation = './Clips/IASIP/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='trump', description='We gotta build the wall', pass_context=True)
async def trump(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/trump/')))
    cliplocation = './Clips/trump/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='gameof', description='Booby B to our rescue', pass_context=True)
async def gameof(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/got/')))
    cliplocation = './Clips/got/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='fact', description='Bonzi knows so much', pass_context=True)
async def fact(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/facts/')))
    cliplocation = './Clips/facts/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='wwe', description='Hulk Hogan', pass_context=True)
async def wwe(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/wwe/')))
    cliplocation = './Clips/wwe/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='sports', description='NICE ON!', pass_context=True)
async def sports(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/sports/')))
    cliplocation = './Clips/sports/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.hybrid_command(name='check-in', description='check in for daily marcs, only avaliable at 7:00 EDT/EST', pass_context=True)
async def checkin(ctx):
    filename = 'data/userdata.json'
    with open(filename, "r") as file:
        userdata = json.load(file)
    altfilename = './data/longtermdata.json'
    with open(altfilename, "r") as file:
        data = json.load(file)
    today = date.today()
    now = datetime.datetime.now()
    dt_string = now.strftime("%H%M")
    print(dt_string)

    user = str(ctx.message.author)

    if user in data['dayvalues']['check-in']:
        msg = "I already gave you credit for flum today baka:rage:! Try again tomorrow!"
        await ctx.send(msg, tts=True)
        return

    try:
        channel = ctx.message.author.voice.channel
    except AttributeError:
        msg = "Can't Fool me :triumph: you aren't even in the voice chat :triumph:"
        await ctx.send(msg, tts=True)
        return

    if int(dt_string) <= 2200 and int(dt_string) >= 1900:
        msg = "Thank you for your service kind stranger! Have some marcs to spend!"
        await ctx.send(msg, tts=True)
        if data['dayvalues']['check-in'] == 'empty':
            data['dayvalues']['check-in'] = str(user)
        else:
            data['dayvalues']['check-in'] = data['dayvalues']['check-in'] + ', ' + str(user)
        mod = 500
        x = user
        try:
            # adding marcs normally, do they have a wallet?
            userdata[x]['score'] = userdata[x]['score'] + mod
        except KeyError:
            # no wallet found, do they have an entry?
            try:
                userdata[x]['score'] = mod
            except KeyError:
                userdata[x] = {}
                userdata[x]['score'] = mod
        msg = str(user) + ' has ' + str(userdata[x]['score']) + ' marcs!'
        await ctx.send(msg)
        with open(altfilename, "w") as file:
            json.dump(data, file)
        with open(filename, "w") as file:
            json.dump(userdata, file)
    else:
        bet = int(dt_string) - 1900
        if bet > 0:
            msg = "Too late! Try tommorow at 7:00 p.m. like everyone else"
            await ctx.send(msg, tts=True)
        else:
            msg = "Appreciate the enthusiam but, wait till everyone else is awake and flumcabale"
            await ctx.send(msg, tts=True)

@client.hybrid_command(name='restart', description='kill flumbot only to make him stronger', pass_context=True)
async def restart(ctx):
    await ctx.send("cry :(", ephemeral=True, delete_after=float(10))
    os.startfile('restart.py')
    exit()

@client.hybrid_command(name='flip', description='flip a standard US coin', pass_context=True)
async def flip(ctx, args):
        x = list(args)
        if 'coin' in x:
            if random.randint(0, 1) == 1:
                result = 'Heads'
            else:
                result = 'Tails'
            msg = 'Flipping...'
            await ctx.send(msg, tts=True)
            await asyncio.sleep(4)
            msg = 'Coin is ' + result + ' side up.'
            await ctx.send(msg, tts=True)

@client.hybrid_command(name='roll', description='roll any dice flumbot has', pass_context=True)
async def roll(ctx, sidedness, times, modifier):
    rolls = []
    sum = 0
    i = 0
    for each in range(0, times):
        rolls.append(random.randint(1, sidedness))
    str = f"Rolling a {sidedness} sided dice {times} times, plus {modifier}\n"
    for each in rolls:
        i += 1
        sum = sum + each
        if (each == 20 or each == 1) and (sidedness == 20):
            each = f"**{each}**"
        str = f"{str}Dice {i} rolled a {each}!\n"
    str = f"{str}\nd{sidedness}x{times}+{modifier} = {sum} + {modifier} = {sum+modifier}"

    await ctx.send(content=str, ephemeral=True, delete_after=float(30))

@client.hybrid_command(name='flum', description='various flum editing commands, it is amazing!', pass_context=True)
async def flum(ctx, action, arg):
    quips = './data/quips.json'
    altfilename = './data/longtermdata.json'

    action = action.lower().split()
    if len(action) > 1:
        return

    with open(altfilename, "r") as file:
        data = json.load(file)
    with open(quips, "r") as file:
        line = json.load(file)

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.remove(file)

    if 'flavortext' in action:
        line['gamemsg'].append(arg)
        with open(quips, "w") as file:
            json.dump(line, file)
        msg = f"Succesfully added {arg} to flavortext list!"
        await ctx.send(msg)
        return

    if 'awake' in action:
        line['startmsg'].append(arg)
        with open(quips, "w") as file:
            json.dump(line, file)
        if "hey flumbot" in arg:
            await ctx.send("Successfully added your rule!")
        else:
            msg = f"Successfully added {arg} to the startup messages list!"
            await ctx.send(msg)
        return

    if 'name' in action:
        line['namemsg'].append(arg)
        with open(quips, "w") as file:
            json.dump(line, file)
        msg = f"Successfully added {arg} to the flumbot response list!"
        await ctx.send(msg)

    if 'bet' in action:
        line['betmsg'].append(arg)
        with open(quips, "w") as file:
            json.dump(line, file)
        msg = f"Successfully added {arg} to the bet list!"
        await ctx.send(msg)
        return

    if 'ad' in action:
        line['adlinks'].append(arg)
        with open(quips, "w") as file:
            json.dump(line, file)
        msg = f"Successfully added <{arg}> to the list of ads"
        await ctx.send(msg)
        return

    if 'purge' in action:
        newlist = []
        await ctx.send("Starting purge...")
        for each in line['ytlinks']:
            if ('user' in each) or ('twitch' in each) or ('youtu.be' in each):
                await ctx.send("Purged video... " + str(each))
                continue
            ydl_opts = {
                'cookiefile': 'cookies.txt'
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(each, download=False)
            except Exception as e:
                print(e)
                await ctx.send("Purged video..." + str(each))
                continue
            newlist.append(each)
        line['ytlinks'] = newlist
        with open(quips, "w") as file:
            json.dump(line, file)
        await ctx.send("COMPLETED PURGE")
        print("done")



    if 'video' in action:
        full_url = arg
        ydl_opts = {
            'cookiefile': 'cookies.txt'
        }

        if "youtu.be" in full_url:
            link = full_url.split("/")
            full_url = "https://www.youtube.com/watch?v=" + link[3]
        if "/shorts/" in full_url:
            link = full_url.split("/")
            full_url = "https://www.youtube.com/watch?v=" + link[4]
        if full_url in line['ytlinks']:
            await ctx.send("Already in the list boss...", ephemeral=True, delete_after=3)
            return

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(full_url, download=False)
        except Exception as e:
            print(e)
            await ctx.send("Sorry, I couldn't get that one boss", ephemeral=True, delete_after=3)
            return

        line['ytlinks'].append(full_url)
        with open(quips, "w") as file:
            json.dump(line, file)
        msg = f"Successfully added <{full_url}> to the flum stream"
        await ctx.send(msg)

    if 'mp3' in action:
        link = arg

        ydl_opts = {
            'cookiefile': 'cookies.txt'
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=False)
        except Exception as e:
            print(e)
            await ctx.send("Sorry, I couldn't get that one boss", ephemeral=True, delete_after=3)
            return

        await ctx.send(f"Adding <{link}> to the queue to download!")
        threading.Thread(target=entry, args=(link, ctx), daemon=True).start()

@client.hybrid_command(name='surprise', description='flumbot how scandelous of you!', pass_context=True)
async def surprise(ctx):
    await ctx.send("you got it boss", ephemeral=True, delete_after=float(10))
    if random.randint(0, 2) == 1:
        link = await daystart.get_random_image_from_reddit()
    elif random.randint(0, 2) == 1:
        link = await daystart.get_random_image_from_pixiv()
    else:
        link = await daystart.get_random_image_from_4chan()
    await ctx.channel.send(file=discord.File(link))
    await ctx.channel.send(await daystart.quip_image(link))
    os.remove(link)

async def download(link, ctx):
    ydl_opts = {
        'format': 'bestaudio/best',
        'cookiefile': 'cookies.txt',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     ydl.download([link])
    # for file in os.listdir('./'):
    #     if file.endswith(".mp3"):
    #         location = os.path.join("./", file)
    # try:
    #     shutil.move(location, './Clips/usersub')
    # except:
    #     print(f"Duplicate clip <{link}> not added")
    #     for file in os.listdir("./"):
    #         if file.endswith(".mp3"):
    #             os.remove(file)
    #     return
    print(f"Successfully added <{link}> to user submissions folder")

def entry(link, ctx):
    asyncio.run(download(link, ctx))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        print("\t\t=====Nothing else found=====\t\t")
        return
    raise error

client.run(token)
