from __future__ import unicode_literals
import discord
import asyncio
import random
import os
import datetime
import basics
import daystart
import messager
import voicememe
from gtts import gTTS
from discord.ext import commands
from datetime import date

# import big_smoke#
# import mad marc#

today = date.today()
now = datetime.datetime.now()
token = 'notforyou'
client = commands.Bot(command_prefix='', case_insensitive=True, )
x = 0
pilot = 0
username = 'urmum'
data = []
winners = []
cheaters = []
answer = ':a:'


# Things flumbot does on startup
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=daystart.activity())
    channel = client.get_channel(137921870010777600)
    deltaday = daystart.days()

    if daystart.datecheck() == 0:
        print('already spammed chat today do not send wake message')
        return
    if (deltaday % 365) == 0:
        x = deltaday
        while x != 0:
            await asyncio.sleep(2)
            msg = "HAPPY FLUM YEAR\nGIVE IT UP FOR " + str(deltaday / 365) + " YEAR(s) OF FLUMBOT!!!\n"
            await channel.send(msg, tts=True)
            print('wrong')
            x -= 1

    msg = daystart.awake()
    await channel.send(msg)

    msg = "Give it up for Day " + str(deltaday) + "! Day " + str(deltaday) + "!"
    await channel.send(msg)

    await channel.send(daystart.link())


# if anyone deletes a message do this I'll have no hidden messages from me
@client.event
async def on_message_delete(message):
    author = str(message.author)
    content = str(message.content)
    msg = 'Ladies and gentlemen, ' + '@' + author + " said, " + \
          content + ", which they promptly deleted. Making them tonight's biggest loser"
    await message.channel.send(msg)


@client.event
async def on_typing(channel, user, when):
    name = str(user)
    name = name[:-5]

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
    print(user)
    if str(user) in winners or str(user) in cheaters:
        print(str(user) + ' already answered')
        return
    if str(user) == 'Flumbot#1927':
        return
    if answer == reaction.emoji:
        if str(user) == 'BOOF#4284':
            winners.append(str(user))
        if str(user) == 'ratbuddy#9913':
            winners.append(str(user))
        if str(user) == 'ShadowXII#7240':
            winners.append(str(user))
        if str(user) == 'Baconmaster#3725':
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
    messagetobot = str(message.content)
    splitme = str(messagetobot.lower())
    global username
    global data
    data = messagetobot
    username = str(message.author)
    username = username[:-5]
    print(username)

    msg, flag = messager.check(splitme)
    if msg != 'oop':
        await message.channel.send(msg, tts=flag)

    # Do you have a clear vision?
    if 'i see' in messagetobot.lower():
        await message.channel.send(file=discord.File('./Pics/doyou.png'))
        await asyncio.sleep(5)
        await message.channel.send(file=discord.File('./Pics/hedo.png'))

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

    print("No specific phrases said, proceed to read commands")
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
    await voicememe.playclip(cliplocation, ctx, client, 0)


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
        if (timer > 1500):
            timer = 0
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
        await voicememe.playclip(cliplocation, ctx, client, 0)
        timer = timer + random.randint(30, 100)
        print('waiting ' + str(timer) + ' seconds before next clip')


@client.command(pass_context=True, name='tts', help='For the blind or those without a second monitor')
@commands.cooldown(1, 10, commands.BucketType.user)
async def tts(ctx, *args):
    global pilot
    global data
    global username
    pilot = 1
    if 'text.mp3' in os.listdir('./'):
        os.remove('text.mp3')
    while (pilot != 0):
        if (data == 'null' or data == 'tts'):
            await asyncio.sleep(1)
            continue
        text = username + ' said... ' + str(data)
        langlist = ['en-ca']
        language = random.choice(langlist)
        speech = gTTS(text=text, lang=language, slow=False)
        speech.save("text.mp3")
        cliplocation = 'text.mp3'
        await voicememe.playclip(cliplocation, ctx, client, 0)
        os.remove('text.mp3')
        data = 'null'


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
        person = str(random.choice(os.listdir('./Music/MIDI/')))
        cliplocation = './Music/MIDI/' + person
        await voicememe.playclip(cliplocation, ctx, client, 0)
        await asyncio.sleep(2)
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


@client.command(pass_context=True, name='stop', help='Ruin the fun for everyone')
@commands.cooldown(1, 10, commands.BucketType.user)
async def stop(ctx, *args):
    global pilot
    pilot = 0
    server = ctx.message.guild.voice_client
    await server.disconnect()


client.run(token)
