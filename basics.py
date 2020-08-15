from __future__ import unicode_literals
import datetime
from datetime import date
import discord
import youtube_dl
import os
import random
import asyncio
import time
import dateparser
import json
import shutil
import daystart

gamestart = ''

async def check(ctx,client,lister):
    filename = './bin/en_data/userdata.json'
    with open(filename, "r") as file:
        userdata = json.load(file)
    altfilename = './bin/en_data/longtermdata.json'
    with open(altfilename, "r") as file:
        data = json.load(file)
    quips = './bin/en_data/quips.json'
    with open(quips, "r") as file:
        line = json.load(file)
    author = str(ctx.message.author)
    y = lister

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.remove(file)

    if 'game' in lister:
        x = lister.index('game')
        data['dayvalues']['game'] = ' '.join(lister[x+1:])
        with open(altfilename, "w") as file:
            json.dump(data, file)
        return

    if 'begun' in lister or 'begun?' in lister:
        msg = '@everyone it must be flum time'
        await ctx.send(msg, tts=True)

    if 'nay' in lister or 'yea' in lister:
        if 'nay' in lister:
            mod = -1
        else:
            mod = 0
        try:
            userdata[author]['status'] = mod
        except KeyError:
            userdata[author] = userdata[author]
            userdata[author]['status'] = mod
        with open(filename, "w") as file:
            json.dump(userdata, file)
        return

    if 'flavortext' in lister:
        y.remove('flavortext')
        y = ' '.join(y)
        line['gamemsg'].append(y)
        with open(quips, "w") as file:
            json.dump(line, file)
        msg = 'succesfully added ' + "'" + y + "'" + ' to flavortext list'
        await ctx.send(msg)
        return

    if 'awake' in lister:
        y.remove('awake')
        y = ' '.join(y)
        line['startmsg'].append(y)
        with open(quips, "w") as file:
            json.dump(line, file)
        msg = 'succesfully added ' + "'" + y + "'" + ' to the startup message list'
        await ctx.send(msg)
        return

    if 'name' in lister:
        y.remove('name')
        y = ' '.join(y)
        line['namemsg'].append(y)
        with open(quips, "w") as file:
            json.dump(line, file)
        msg = 'succesfully added ' + "'" + y + "'" + ' to flumbot response list'
        await ctx.send(msg)

    if 'bet' in lister:
        y.remove('bet')
        y = ' '.join(y)
        line['betmsg'].append(y)
        with open(quips, "w") as file:
            json.dump(line, file)
        msg = 'succesfully added ' + "'" + y + "'" + ' to bet list'
        await ctx.send(msg)
        return

    if 'ad' in lister:
        y.remove('ad')
        y = ' '.join(y)
        line['adlinks'].append(y)
        with open(quips, "w") as file:
            json.dump(line, file)
        msg = 'succesfully added ' + "'<" + y + ">'" + ' to list of ads'
        await ctx.send(msg)
        return

    if 'video' in lister:
        y.remove('video')
        y = ' '.join(y)
        line['ytlinks'].append(y)
        with open(quips, "w") as file:
            json.dump(line, file)
        msg = 'succesfully added ' + "'<" + y + ">'" + ' to list of flumbot streams'
        await ctx.send(msg)

    if 'channel' in lister:
        y.remove('channel')
        if len(y) == 1:
            for channel in ctx.guild.text_channels:
                if channel.name in y:
                    for h in ctx.guild.text_channels:
                        if h.id in data['dayvalues']['channels']:
                            data['dayvalues']['channels'].remove(h.id)
                    data['dayvalues']['channels'].append(channel.id)
                    with open(altfilename, "w") as file:
                        json.dump(data, file)
                    msg = "New default channel is now '" + channel.name + "'"
                    await ctx.send(msg)
                    return
                else:
                    continue
            else:
                msg = "channel not found, try checking the name, this command is case sensitive"
                await ctx.send(msg)
        else:
            msg = "use the form 'flum channel (name)' this command is case sensitive"
            await ctx.send(msg)

    if 'color' in lister:
        if len(y) != 4:
            msg = "please type in the format 'flum color r g b'"
            await ctx.send(msg)
            return
        try:
            userdata[author]['color'] = (int(y[1]), int(y[2]), int(y[3]))
        except KeyError:
            msg = 'type inventory first before doing this'
            await ctx.send(msg)
            return
        msg = 'Successfully changed your color!'
        await ctx.send(msg)
        with open(filename, "w") as file:
            json.dump(userdata, file)
        return

    if 'mp3' in lister:
        y.remove('mp3')
        y = str(y)
        char_list = ["'", "[", "]", ","]
        for i in char_list:
            y = y.replace(i, '')
        link = str(y)
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
        for file in os.listdir('./'):
            if file.endswith(".mp3"):
                location = os.path.join("./", file)
        shutil.move(location, './Clips/usersub')
        msg = "Successfully added <" + link + "> to user submissions folder"
        await ctx.send(msg)

    if 'help' in lister:
        embed = discord.Embed(title="list of important flum commands", colour=discord.Colour.from_rgb(0, 144, 0))
        embed.add_field(name='game', value='sets flum game of tonight')
        embed.add_field(name='begun', value='lets everyone know its time to flum')
        embed.add_field(name='nay and yea', value='confirms the flum status you currently have')
        embed.add_field(name='flavortext', value='adds a new flavortext under the bot name in discord')
        embed.add_field(name='awake', value='let flumbot say whatever you want when he wakes up tomorrow')
        embed.add_field(name='name', value='what flumbot does when you say his name in a message')
        embed.add_field(name= 'bet', value= 'what will flumbot bet when asked?')
        embed.add_field(name='ad', value='what ads display in flumbot brand embeds, use only direct links gifs/images')
        embed.add_field(name='video', value='what game flumbot is streaming or playing, use only youtube/twitch links')
        embed.add_field(name='mp3', value='add some content to flumbot, please no 10 hour videos, only do youtube links')
        embed.add_field(name='status', value='what is the flum status for tonight?')
        embed.add_field(name='channel', value='format is "flum channel (name)" this sets where default bot '
                                              'communication is')
        embed.set_thumbnail(url=daystart.getad())
        await ctx.send(embed=embed)


    if 'status' in lister:
        embed = discord.Embed(title="Flumcababilty of Compatriots", colour=discord.Colour.from_rgb(0, 144, 0))
        embed.add_field(name='Game of Tonight', value=data['dayvalues']['game'], inline=False)
        for x in userdata:
            if userdata[x]['status'] < 0:
                status = ':x:'
            else:
                status = ':+1:'
            embed.add_field(name = x[:-5], value = status)

        embed.set_thumbnail(url=daystart.getad())
        await ctx.send(embed=embed)


async def fortune(ctx, client):
    chance = int(random.randrange(0, 1000))
    msg = "Let me think on what you have told me"
    await ctx.send(msg, tts=True)
    await asyncio.sleep(4)
    msg = ":thinking:"

    if (chance == 69):
        msg = "give me a couple hours to contemplate the results"
        await ctx.send(msg, tts=True)
        time.sleep(10800)
        guess = ['yes', 'no', 'poop', 'penile fracture']
        msg = random.choice(guess)
        await ctx.send(msg, tts=True)

    else:
        await ctx.send(msg, tts=True)
        await asyncio.sleep(6)
        wager = ['It would be wise to pursue other ventures', 'History does not side with you', 'no lol',
                 'I recommend you dab', 'You do you', "Just don't steal a tree",
                 "The future looks bright", "It is unlikely", "Pray on it", "Ask marc", "Ask rat", "Ask niche",
                 "Ask yourself", "best @everyone with your question",
                 "yes", "the future you seek has already happened", "marc said he will do it for you",
                 "only t-dubs will know the answer to your question", "Ask again", "It is certain",
                 "It is decidedly so", "Most likely", "Meh", "Signs point to yes", "Without a doubt", "Outlook good",
                 "Outlook not so good", "You may rely on it", "Cannot predict now",
                 "Just die", "I prescribe a midimania to heal", "Maybe think on it a few days",
                 "Rome wasn't built in a day", "The day of reckoning is approaching", "help me",
                 "Fo Sure", "Nah", "I don't feel like it", "behind you is the answer you seek", "yes", "no",
                 "yeah I think so", "Doesn't sounds right", "I think you are wrong", "Is that gamer?", "oh yeah",
                 "Think for yourself next time", "Uhhhhhhhhhhhhhhhhhhhhhhhh", "yuh", "nah"]
        msg = random.choice(wager)
        await ctx.send(msg, tts=True)

async def checkinv(ctx, client):
    filename = './bin/en_data/userdata.json'
    with open(filename, "r") as file:
        userdata = json.load(file)
    user = str(ctx.message.author)
    try:
        a = int(userdata[user]['inventory'])
    except KeyError:
        try:
            userdata[user] = userdata[user]
            userdata[user]['inventory'] = 0
            a = 0
        except KeyError:
            userdata[user] = {}
            userdata[user]['inventory'] = 0
            a = 0
    try:
        color = userdata[user]['color']
    except KeyError:
        color = [0, 144, 0]
        userdata[user]['color'] = color
    embed = discord.Embed(title=user[:-5], colour=discord.Colour.from_rgb(color[0], color[1], color[2]))
    try:
        money = userdata[user]['score']
    except KeyError:
        money = 0
    embed.add_field(name = 'Marcs',
                    value = "You have " + str(money) + " marcs!",
                    inline = False)
    if (a == 0):
        embed.add_field(name='Empty',
                        value='Maybe spend some marcs')
        await ctx.send(embed=embed)
    b = 2
    if (a & b == b):
        embed.add_field(name='Big Daddy Rhinehart',
                        value='World Renowned Doctor, and Football Coach, now in your pocket!')
        embed.set_image(url='https://cdn.discordapp.com/attachments/137921870010777600/695021109891825754/a_god.jpeg')
        await ctx.send(embed=embed)
    b = b * 2
    if (a & b == b):
        embed.add_field(name='Pop-tart Gang',
                        value='Gang shit, thats why and who made this blessed image')
        embed.set_image(url='https://cdn.discordapp.com/attachments/402876560165830657/693255972508139630/gang.png')
        await ctx.send(embed=embed)
    b = b * 2
    if (a & b == b):
        embed.add_field(name='Taco Bell Dog',
                        value='The long forgotten mascot of ol Taco Bell, too racist to ever return')
        embed.set_image(
            url='https://cdn.discordapp.com/attachments/549996148643856389/696824107169218620/897414028-banner_33.png')
        await ctx.send(embed=embed)
    b = b * 2
    if (a & b == b):
        embed.add_field(name="Twitch IRL Streamer",
                        value="Twitch sure has changed, maybe for the better, don't worry maybe one day I will make this something better")
        embed.set_image(url='https://i.imgur.com/86wH1kX.mp4')
        await ctx.send(embed=embed)
    b = b * 2
    if (a & b == b):
        embed.add_field(name="Marc",
                        value="ok marc, here is your cheap item, before you even ask for it")
        embed.set_image(
            url='https://www.bgt.nz/tmp/testimonialstalent/marco-fletcher/images/medium/Screen_Shot_2016-04-29_at_11.49.43_AM.png')
        await ctx.send(embed=embed)
    b = b * 2
    if (a & b == b):
        embed.add_field(name="John F. Kennedy",
                        value="He did stuff in Cuba, and got shot in the head")
        embed.set_image(url='https://thumbs.gfycat.com/AdorableDifferentArmednylonshrimp-small.gif')
        await ctx.send(embed=embed)
    b = b * 2
    if (a & b == b):
        embed.add_field(name="Donald Trump", value="45th President of the United States. Says China, and Mexico a lot")
        embed.set_image(url='https://media3.giphy.com/media/sUrqLJoLNpFa8/source.gif')
        await ctx.send(embed=embed)
    b = b * 2
    if (a & b == b):
        embed.add_field(name="A Math Book",
                        value="Ran out of Ideas lol, but here is a math book")
        embed.set_image(url='https://images-na.ssl-images-amazon.com/images/I/41bv5SmS6NL._SX368_BO1,204,203,200_.jpg')
        await ctx.send(embed=embed)
    with open(filename, "w") as file:
        json.dump(userdata, file)
    return

async def shopfront(ctx,client,args):
    filename = './bin/en_data/userdata.json'
    with open(filename, "r") as file:
        userdata = json.load(file)
    author = ctx.message.author

    if (len(args) == 0):
        msg = "here is what we gots to sell"
        await ctx.send(msg)
        embed = discord.Embed(title="Welcome to the WarStone!", colour=discord.Colour.from_rgb(0, 144, 0))
        embed.add_field(name='Item 1', value='Big Daddy Rhinehart - \n5000 marcs', inline=True)
        embed.add_field(name='Item 2', value='Pop-tart Gang - \n2500 marcs', inline=True)
        embed.add_field(name='Item 3', value='Taco Bell Dog - \n1500 marcs', inline=True)
        embed.add_field(name='Item 4', value='Twitch IRL Streamer - 10000 marcs', inline=False)
        embed.add_field(name='Item 5', value='Marc - \n10 marcs', inline=True)
        embed.add_field(name='Item 6', value='John F. Kennedy - \n1969 marcs', inline=True)
        embed.add_field(name='Item 7', value='Donald Trump -\n 2020 marcs', inline=True)
        embed.add_field(name='Item 8', value='A Math Book -\n 200 marcs', inline=True)
        embed.set_footer(text='all sales are final, refunds will not be taken')
        embed.set_thumbnail(url=daystart.getad())
        await ctx.send(embed=embed)
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
        await client.wait_for('message', check=check, timeout=20)
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
    if (args == 8):
        price = 200

    item = pow(2, args)
    try:
        userdata[user]['score'] = userdata[user]['score']
    except KeyError:
        try:
            userdata[user] = userdata[user]
            userdata[user]['score'] = 0
        except KeyError:
            userdata[user] = {}
            userdata[user]['score'] = 0
    if userdata[user]['score'] - price < 0:
        msg = "broke boy"
        await ctx.send(msg)
        return
    try:
        userdata[user]['inventory'] = userdata[user]['inventory']
    except KeyError:
        try:
            userdata[user] = userdata[user]
            userdata[user]['inventory'] = 0
        except KeyError:
            userdata[user] = {}
            userdata[user]['inventory'] = 0
    a = userdata[user]['inventory']
    b = item
    if ((a & b) == b):
        msg = "you already own this"
        await ctx.send(msg)
        return

    userdata[user]['score'] = userdata[user]['score'] - price
    userdata[user]['inventory'] = userdata[user]['inventory'] + item
    msg = "You now have " + str(userdata[user]['score']) + " marcs!\nThank you for shopping Flumbot!"
    with open(filename, "w") as file:
        json.dump(userdata, file)
    await ctx.send(msg)
    return

async def rollthedice(ctx,args):
    x = list(args)
    dicerol = 1
    if ('dice' and 'sided' and ('times' or 'time') in x):
        sides = x[x.index('sided') - 1]
        times = x[x.index('times') - 1]
        while (times != 0):
            msg = 'Dice ' + str(dicerol) + ' rolled a ' + str(random.randint(1, int(sides)))
            await asyncio.sleep(2)
            await ctx.send(msg)
            times = int(times) - 1
            dicerol = dicerol + 1
        return
    elif ('dice' and 'sided') in x:
        sides = x[x.index('sided') - 1]
        print(sides)
        roll = str(random.randint(1, int(sides)))
        if (int(sides) == 20):
            if (int(roll) == 20):
                await asyncio.sleep(2)
                msg = '<:PogChamp:583814253484441601>'
                await ctx.send(msg)
                msg = 'You rolled a ' + roll + '!'
                await ctx.send(msg)
                return
            if (int(roll) == 1):
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
    elif ('d20' in x or 'd10' in x or 'd4' in x or 'd6' in x or 'd8' in x or 'd12' in x or 'd100' in x):
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
        if ('x' in x):
            if ('+' in x):
                mod = x[x.index('+') + 1]
                extra = ' + '
            else:
                mod = ''
                extra = ''
            times = x[x.index('x') + 1]
            while (times != 0):
                msg = 'Dice ' + str(dicerol) + ' rolled a ' + str(random.randint(1, sides)) + extra + mod + '!'
                await asyncio.sleep(2)
                await ctx.send(msg)
                times = int(times) - 1
                dicerol = dicerol + 1
            return
        roll = str(random.randint(1, sides))
        if ((int(roll) == 20) and (sides == 20)):
            await asyncio.sleep(2)
            msg = '<:PogChamp:583814253484441601>'
            await ctx.send(msg)
            if ('+' in x):
                mod = x[x.index('+') + 1]
                extra = ' + '
            else:
                mod = ''
                extra = ''
            msg = 'You rolled a ' + roll + extra + mod + '!'
            await ctx.send(msg)
            return
        if ((int(roll) == 1) and (sides == 20)):
            await asyncio.sleep(2)
            msg = '<:monkaS:583814789298651154>'
            await ctx.send(msg)
            if ('+' in x):
                mod = x[x.index('+') + 1]
                extra = ' + '
            else:
                mod = ''
                extra = ''
            msg = 'You rolled a ' + roll + extra + mod + '!'
            await ctx.send(msg)
            return
        if ('+' in x):
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

async def daily(ctx):
    filename = './bin/en_data/userdata.json'
    with open(filename, "r") as file:
        userdata = json.load(file)
    altfilename = './bin/en_data/longtermdata.json'
    with open(altfilename, "r") as file:
        data = json.load(file)
    today = date.today()
    now = datetime.datetime.now()
    dt_string = now.strftime("%H%M")
    print(dt_string)

    user = str(ctx.message.author)

    if (user in data['dayvalues']['check-in']):
        msg = "I already gave you credit for flum today baka:rage:! Try again tomorrow!"
        await ctx.send(msg)
        return

    try:
        channel = ctx.message.author.voice.channel
    except AttributeError:
        msg = "Can't Fool me :triumph: you aren't even in the voice chat :triumph:"
        await ctx.send(msg)
        return

    if int(dt_string) <= 2200 and int(dt_string) >= 1900:
        msg = "Thank you for your service kind stranger! Have some marcs to spend!"
        await ctx.send(msg, tts=True)
        if data['dayvalues']['check-in'] == 'empty':
            data['dayvalues']['check-in'] = str(user)
        else:
            data['dayvalues']['check-in'] = data['dayvalues']['check-in'] + ', ' + str(user)
        mod = 75
        for i in userdata:
            try:
                userdata[i]['score'] = userdata[i]['score'] + mod
            except KeyError:
                try:
                    userdata[i] = userdata[i]
                    userdata[i]['score'] = mod
                except KeyError:
                    userdata[i] = {}
                    userdata[i]['score'] = mod
        msg = str(user[:-5]) + ' has ' + str(userdata[user]['score']) + ' marcs!'
        await ctx.send(msg)
        with open(altfilename, "w") as file:
            json.dump(data, file)
        with open(filename, "w") as file:
            json.dump(userdata, file)
    else:
        bet = int(dt_string) - 1900
        if (bet > 0):
            msg = "Too late! Try tommorow at 7:00 p.m. like everyone else"
            await ctx.send(msg)
        else:
            msg = "Appreciate the enthusiam but, wait till everyone else is awake and flumcabale"
            await ctx.send(msg)

async def welcome(client,guild):
    channel = guild.text_channels[0]
    msg = "Welcome to Flumbot, the official bot of Flum. A bot where you create half the content this bot has! I " \
          "am going to ask you type the preferred text channel for me to spam chat in. The next message sent will be " \
          "the text channel I look for, note this is case sensitive. You can change this later with the command " \
          "'flum channel'. I recommend starting by typing 'flum help', simply 'help', or jump straight into things " \
          "and hop in a voice channel and type 'midimania'\nHave Fun! Enjoy the Bot :) "
    await channel.send(msg)
    altfilename = './bin/en_data/longtermdata.json'
    with open(altfilename, "r") as file:
        data = json.load(file)

    def checkit(m):
        message = m.content
        for channel in guild.text_channels:
            if channel.name == message:
                number = int(channel.id)
                data['dayvalues']['channels'].append(number)
                global gamestar
                gamestar = "Default Channel set to '" + message + "' use 'flum channel' to change it'"
                with open(altfilename, "w") as file:
                    json.dump(data, file)
                return True
            else:
                continue
        return

    try:
        await client.wait_for('message', check=checkit, timeout=900)
        await channel.send(gamestar)
        return

    except asyncio.TimeoutError:
        data['dayvalues']['channels'].append(int(guild.text_channels[0].id))
        with open(altfilename, "w") as file:
            json.dump(data, file)
        msg = "Default Channel set to " + guild.text_channels[0].name + " use 'flum channel' to change it'"
        guild.text_channels[0].send(msg)


async def killed(client, guild):
    altfilename = './bin/en_data/longtermdata.json'
    with open(altfilename, "r") as file:
        data = json.load(file)
    for x in guild.text_channels:
        if x.id in data['dayvalues']['channels']:
            data['dayvalues']['channels'].remove(x.id)
    with open(altfilename, "w") as file:
        json.dump(data, file)
    print('successfully removed the traitors')