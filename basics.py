from __future__ import unicode_literals
import datetime
from datetime import date
import discord
import youtube_dl
import os
import random
import asyncio
import time
import game
import xlrd
import json
import shutil
import daystart
from PIL import Image
from shutil import copyfile
import numpy as np
import colorsys

gamestart = ''


async def colorweap(filename, player):
    rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
    hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

    def shift_hue(arr, hout):
        r, g, b, a = np.rollaxis(arr, axis=-1)
        h, s, v = rgb_to_hsv(r, g, b)
        h = hout
        r, g, b = hsv_to_rgb(h, s, v)
        arr = np.dstack((r, g, b, a))
        return arr

    def colorize(image, hue):
        """
        Colorize PIL image `original` with the given
        `hue` (hue within 0-360); returns another PIL image.
        """
        img = image.convert('RGBA')
        arr = np.array(np.asarray(img).astype('float'))
        new_img = Image.fromarray(shift_hue(arr, hue / 360.).astype('uint8'), 'RGBA')

        return new_img

    im = Image.open(filename)
    im1 = colorize(im, random.randint(1, 360))
    im1.save("./Pics/" + player[:-5] + "_weap_temp.png")


async def genweapon(level, player, ctx, client, type=-1, rarity=0):
    genlist = []
    k = 0
    loc = './bin/en_data/statsheet.xlsx'
    wb = xlrd.open_workbook(loc, on_demand=True)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    for i in range(1, sheet.nrows - 2):
        genlist.append(sheet.row_values(i))
        k += 1
    wb.release_resources()
    print(genlist)

    if (rarity <= 0):
        rarity = random.choices(population=[1, 2, 3, 4], weights=[1000, 100, 50, 1])
        rarity = rarity[0]
    if (rarity == 1):
        rmod = 25
        rarity = "Common"
    if (rarity == 2):
        rmod = 18
        rarity = "Rare"
    if (rarity == 3):
        rmod = 5
        rarity = "Strange"
    if (rarity == 4):
        rmod = 1
        rarity = "Legendary"

    if type == -1:
        print("no type request, selecting random one...")
        type = random.choice(genlist)
        attmod = (level / rmod) * (1 + type[3])
        spdmod = (level / rmod) * (1 + type[2])
        type = type[1]
    else:
        attmod = (level / rmod) * (1 + genlist[type][3])
        spdmod = (level / rmod) * (1 + genlist[type][2])
        type = genlist[type][1]
    shutil.copyfile("./Pics/" + type + ".png", "./Pics/" + player[:-5] + "_weap_temp.png")
    if rmod == 25:
        # common or rare, do not color or name
        msg = """```{} found a {} {}\nAttack Modifier: {:.3f}\nSpeed Modifier: {:.3f}\nType 'keep' to replace your current weapon
        with this one...```""".format(str(player[:-5]), rarity, type, attmod, spdmod)
        message1 = await ctx.send(msg)
    else:
        # strange or legendary, color and name the weapon
        act = []
        adj = []
        with open("./bin/en_data/act.txt") as fp:
            Lines = fp.readlines()
        for line in Lines:
            line = line.rstrip()
            act.append(line)
        with open("./bin/en_data/adj.txt") as fp:
            Lines = fp.readlines()
        for line in Lines:
            line = line.rstrip()
            adj.append(line)
        if rmod != 18:
            await colorweap("./Pics/" + type + ".png", player)
        adj = random.choice(adj).capitalize()
        act = random.choice(act).capitalize()
        msg = """```{} found a {} {} {} of {}\nAttack Modifier: {:.3f}\nSpeed Modifier: {:.3f}\nType 'keep' to replace your current weapon
                with this one...```""".format(str(player[:-5]), rarity, adj, type, act, attmod, spdmod)
        message1 = await ctx.send(msg)
    message2 = await ctx.send(file=discord.File("./Pics/" + player[:-5] + "_weap_temp.png"))

    def check(m):
        return (m.content.lower() == 'keep' or m.content.lower() == 'pass') and player == str(m.author)

    try:
        message = await client.wait_for('message', check=check, timeout=90)
    except asyncio.TimeoutError:
        msg = "I'll just be throwing this away then..."
        message = await ctx.send(msg)
        await message1.delete()
        await message2.delete()
        await asyncio.sleep(20)
        await message.delete()
        os.remove("./Pics/" + player[:-5] + "_weap_temp.png")
        return
    await message.delete()
    if message.content.lower() == "pass":
        msg = "I'll just be throwing this away then..."
        message = await ctx.send(msg)
        await message1.delete()
        await message2.delete()
        await asyncio.sleep(20)
        await message.delete()
        os.remove("./Pics/" + player[:-5] + "_weap_temp.png")
        return

    os.rename("./Pics/" + player[:-5] + "_weap_temp.png", "./Pics/" + player[:-5] + "_weap.png")
    if rmod in [1, 5, 18]:
        await saveweapon(level, rarity, attmod, spdmod, type, player, "{} {} of {}".format(adj, type, act))
    else:
        await saveweapon(level, rarity, attmod, spdmod, type, player)
    await message1.edit(content="""```{} equips {} {}```""".format(player[:-5], rarity, type))
    await asyncio.sleep(20)
    await message1.delete()
    await message2.delete()

    return


async def saveweapon(level, rarity, attack, speed, type, player, name="null"):
    filename = './bin/en_data/userdata.json'
    with open(filename, "r") as file:
        data = json.load(file)
    try:
        data[player]["inventory"]
    except KeyError:
        print(player + " had no inventory, creating one...")
        data[player]["inventory"] = {}

    try:
        print(player + " upgrades \n" + str(data[player]["inventory"]["weapon"]) + " --> ", end="")
    except KeyError:
        print(player + " gets their first weapon...")

    data[player]["inventory"]["weapon"] = []
    data[player]["inventory"]["weapon"].append(attack)
    data[player]["inventory"]["weapon"].append(speed)
    data[player]["inventory"]["weapon"].append(type)
    data[player]["inventory"]["weapon"].append(rarity)
    data[player]["inventory"]["weapon"].append(name)
    data[player]["inventory"]["weapon"].append(level)

    print(str(data[player]["inventory"]["weapon"]))

    with open(filename, "w") as file:
        json.dump(data, file)
    return


async def check(ctx, client, lister):
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
        if 'start' in lister:
            await game.start(ctx, client)
            return
        if 'end' in lister:
            await game.end()
            return
        x = lister.index('game')
        data['dayvalues']['game'] = ' '.join(lister[x + 1:])
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
        embed.add_field(name='bet', value='what will flumbot bet when asked?')
        embed.add_field(name='ad', value='what ads display in flumbot brand embeds, use only direct links gifs/images')
        embed.add_field(name='video', value='what game flumbot is streaming or playing, use only youtube/twitch links')
        embed.add_field(name='mp3',
                        value='add some content to flumbot, please no 10 hour videos, only do youtube links')
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
            embed.add_field(name=x[:-5], value=status)

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
    await ctx.message.delete()
    filename = './bin/en_data/userdata.json'
    with open(filename, "r") as file:
        data = json.load(file)
    author = str(ctx.message.author)

    try:
        # see if custom color set
        color = data[author]["color"]
        color = discord.Colour.from_rgb(color[0], color[1], color[2])
    except KeyError:
        colorlist = []
        for role in ctx.guild.roles:
            if role in ctx.message.author.roles:
                color = role.colour
        # this will break if user has no role, seems impossible, as @everyone would have to be disabled for them
        if str(color) == "#000000":
            color = discord.Colour.from_rgb(0, 144, 0)

        # color = discord.Colour.from_rgb(0, 144, 0)
    embed = discord.Embed(title=author[:-5] + "'s inventory",
                          colour=color)

    try:
        # see if they have money
        money = data[author]["score"]
    except KeyError:
        try:
            # they have an entry, but no wallet
            data[author]["score"] = 0
        except KeyError:
            # they have no entry
            data[author] = {}
            data[author]["score"] = 0
        money = 0

    try:
        print(data[author]["inventory"]["level"][0])
        # do they have a level in flum game?
    except (KeyError, TypeError, IndexError):
        try:
            # do they have a proper inventory format?
            data[author]["inventory"]["level"] = []
        except (KeyError, TypeError):
            # old format, or no inventory
            data[author]["inventory"] = {}
            data[author]["inventory"]["level"] = []
        # set level to 1
        data[author]["inventory"]["level"].append(1)
        data[author]["inventory"]["level"].append("0/100")
        with open(filename, "w") as file:
            json.dump(data, file)
        with open(filename, "r") as file:
            data = json.load(file)

    level = data[author]["inventory"]["level"][0]
    exp = data[author]["inventory"]["level"][1]

    try:
        # do they have a weapon?
        print(data[author]["inventory"]["weapon"][0])
    except (KeyError, IndexError):
        # give starter weapon
        await saveweapon(1, "Starter", 0, 0, "Stick", author)
        shutil.copyfile("./Pics/Stick.png", "./Pics/"+author[:-5]+"_weap.png")
        with open(filename, "r") as file:
            data = json.load(file)

    attack = data[author]["inventory"]["weapon"][0]
    speed = data[author]["inventory"]["weapon"][1]
    name = data[author]["inventory"]["weapon"][2]
    rarity = data[author]["inventory"]["weapon"][3]
    strength = data[author]["inventory"]["weapon"][5]
    if data[author]["inventory"]["weapon"][4] != "null":
        custom = " named ***" + data[author]["inventory"]["weapon"][4] + "***"
    else:
        custom = ""

    weapimage = "./Pics/" + author[:-5] + "_weap.png"
    embed.add_field(name="Marcs", value=money, inline=False)
    embed.add_field(name="Level in Flum Game", value=level, inline=False)
    embed.add_field(name="Experience to Next Level", value=exp, inline=False)
    embed.add_field(name="Attack || Modifier", value="placeholder || {:.3f}".format(attack), inline=False)
    embed.add_field(name="Defense || Modifier", value=("placeholder" + " || " + "placeholder"), inline=False)
    embed.add_field(name="Speed || Modifier", value="placeholder || {:.3f}".format(speed), inline=False)
    embed.add_field(name="Current Weapon", value="Level " + str(strength) + ": **" + rarity + "** " + name + custom, inline=False)

    file = discord.File(weapimage, filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.send(file=file, embed=embed)
    with open(filename, "w") as file:
        json.dump(data, file)
    return

async def shopfront(ctx, client, args):
    await ctx.message.delete()
    filename = './bin/en_data/userdata.json'
    with open(filename, "r") as file:
        data = json.load(file)
    author = str(ctx.message.author)
    try:
        money = data[author]["score"]
        print(data[author]["inventory"]["weapon"][0])
    except (KeyError, TypeError):
        msg1 = await ctx.send("check your inventory before coming here tubby...")
        await asyncio.sleep(20)
        await msg1.delete()
        return
    embed = discord.Embed(title="Welcome to the Warstone!", colour=discord.Colour.from_rgb(0, 144, 0))
    embed.add_field(name=author[:-5]+ "'s Marcs", value=money, inline=False)
    embed.add_field(name="Roulette", value="type 'roulette' to gain new weapons")
    embed.add_field(name="Name", value="type 'name' to name your current weapon --- 5000 marcs")
    embed.add_field(name="Color", value="type 'color' to color your current weapon, at random --- 10000 marcs")
    message1 = await ctx.send(embed=embed)

    def checkm(m):
        return (m.content.lower() == 'roulette' or m.content.lower() == 'name' or m.content.lower() == 'color') and author == str(m.author)

    try:
        message = await client.wait_for('message', check=checkm, timeout=90)
    except asyncio.TimeoutError:
        await message1.delete()
        return
    await message.delete()
    if message.content.lower() == 'roulette':
        embed = discord.Embed(title="Welcome to the GambleZone!", colour=discord.Colour.from_rgb(0, 144, 0))
        embed.add_field(name=author[:-5] + "'s Marcs", value=money, inline=False)
        embed.add_field(name="Random Gamble", value="1000 marcs")
        embed.add_field(name="Common Gamble", value="500 marcs")
        embed.add_field(name="Rare Gamble", value="10000 marcs")
        embed.add_field(name="Strange Gamble", value="25000 marcs")
        embed.add_field(name="Legendary Gamble", value = "99999 marcs")
        embed.add_field(name="Flumbot Pot", value="1000 marcs")
        await message1.edit(embed=embed)

        def checkm(m):
            return (m.content.lower() in 'random common rare strange legendary flumbot pot') and author == str(m.author)

        try:
            message = await client.wait_for('message', check=checkm, timeout=90)
        except asyncio.TimeoutError:
            await message1.delete()
        await message.delete()

        if message.content.lower() == 'random':
            await message1.delete()
            money = money - 1000
            if money < 0:
                msg = await ctx.send("broke boy")
                await asyncio.sleep(20)
                await msg.delete()
                return
            else:
                data[author]["score"] = money
                with open(filename, "w") as file:
                    json.dump(data, file)
            await genweapon(data[author]["inventory"]["level"][0], author, ctx, client)
            return
        if message.content.lower() == 'common':
            await message1.delete()
            money = money - 500
            if money < 0:
                msg = await ctx.send("broke boy")
                await asyncio.sleep(20)
                await msg.delete()
                return
            else:
                data[author]["score"] = money
                with open(filename, "w") as file:
                    json.dump(data, file)
            await genweapon(data[author]["inventory"]["level"][0], author, ctx, client, -1, 1)
            return
        if message.content.lower() == 'rare':
            await message1.delete()
            money = money - 10000
            if money < 0:
                msg = await ctx.send("broke boy")
                await asyncio.sleep(20)
                await msg.delete()
                return
            else:
                data[author]["score"] = money
                with open(filename, "w") as file:
                    json.dump(data, file)
            await genweapon(data[author]["inventory"]["level"][0], author, ctx, client, -1, 2)
            return
        if message.content.lower() == 'strange':
            await message1.delete()
            money = money - 25000
            if (money - 25000) < 0:
                msg = await ctx.send("broke boy")
                await asyncio.sleep(20)
                await msg.delete()
                return
            else:
                data[author]["score"] = money
                with open(filename, "w") as file:
                    json.dump(data, file)
            await genweapon(data[author]["inventory"]["level"][0], author, ctx, client, -1, 3)
            return
        if message.content.lower() == 'legendary':
            await message1.delete()
            money = money - 99999
            if money < 0:
                msg = await ctx.send("broke boy")
                await asyncio.sleep(20)
                await msg.delete()
                return
            else:
                data[author]["score"] = money
                with open(filename, "w") as file:
                    json.dump(data, file)
            await genweapon(data[author]["inventory"]["level"][0], author, ctx, client, -1, 4)
            return
        if message.content.lower() in 'flumbot pot':
            await message1.delete()
            money = money - 1000
            if money < 0:
                message2 = await ctx.send("You don't have enough money to gamble :(")
                await asyncio.sleep(20)
                await message2.delete()
                return
            message1 = await ctx.send("...")
            await message1.edit(content="Time for a chance to win the pot!")
            await asyncio.sleep(5)
            await message1.edit(content="Checking the winning numbers.")
            await asyncio.sleep(2)
            await message1.edit(content="Checking the winning numbers..")
            await asyncio.sleep(2)
            await message1.edit(content="Checking the winning numbers...")
            await asyncio.sleep(2)
            if random.randint(0, 1000) < 5:
                await message1.edit(content="@EVERYONE " + author[:-5] + " WON THE POT!!! THEY GOT " + str(data["Flumbot#1927"]["score"]) + " MARCS!")
                data[author]["score"] = money + data["Flumbot#1927"]["score"]
                data["Flumbot#1927"]["score"] = 0
            else:
                await message1.edit(content=author[:-5] + " loses more to their gambling addiction. Flumbot Pot gains 1000 marcs, it is now " + str(data["Flumbot#1927"]["score"] + 1000) + " marcs!")
                data["Flumbot#1927"]["score"] = data["Flumbot#1927"]["score"] + 1000
                data[author]["score"] = money
            await asyncio.sleep(20)
            await message1.delete()



    elif message.content.lower() == 'name':
        money = data[author]["score"] - 5000
        if money < 0:
            await message.delete()
            await message1.edit(content="you broke boy")
            await asyncio.sleep(20)
            await message1.delete()
            return
        try:
            data[author]["inventory"]["weapon"][4]
        except (KeyError, IndexError):
            msg = "You don't appear to have a weapon to name bud..."
            message2 = await ctx.send(msg)
            await message.delete()
            await message1.delete()
            await asyncio.sleep(20)
            await message2.delete()
            return
        msg = "Type your new weapon's name, cannot be more than 3 words, and use less than 64 characters"
        message2 = await ctx.send(msg)
        await message1.delete()

        def checkm(m):
            return author == str(m.author)

        try:
            message = await client.wait_for('message', check=checkm, timeout=90)
        except asyncio.TimeoutError:
            await message2.edit(content="That's ok take your time")
            await asyncio.sleep(20)
            await message2.delete()
            return

        if len(str(message.content)) < 64 and len(message.content.split()) <= 3:
            data[author]["inventory"]["weapon"][4] = message.content
            data[author]["score"] = money
        else:
            await message2.edit(content="That is too long ;), try something smaller")
            await asyncio.sleep(20)
            await message2.delete()
            return
        await message2.edit(content="Weapon named ***" + data[author]["inventory"]["weapon"][4] + "*** successfully!")
        await asyncio.sleep(20)
        await message2.delete()

    elif message.content.lower() == 'color':
        await message1.delete()
        message1 = await ctx.send("...")
        money = data[author]["score"] - 10000
        if money < 0:
            await message1.edit(content="you broke boy")
            await asyncio.sleep(20)
            await message1.delete()
            return

        type = data[author]["inventory"]["weapon"][2]
        await colorweap("./Pics/" + type + ".png", author)
        message2 = await ctx.send(file=discord.File("./Pics/" + author[:-5] + "_weap_temp.png"))
        await message1.edit(content="I painted it, you want to keep it?")

        def checkm(m):
            return (m.content.lower() == 'keep' or m.content.lower() == 'pass') and author == str(m.author)

        try:
            message = await client.wait_for('message', check=checkm, timeout=90)
        except asyncio.TimeoutError:
            os.remove("./Pics/" + author[:-5] + "_weap_temp.png")
            data[author]["score"] = money
            await message1.delete()
            await message2.edit(content="Well I'm still charging, you...")
            await asyncio.sleep(20)
            await message2.delete()
            with open(filename, "w") as file:
                json.dump(data, file)
            return
        await message.delete()
        if message.content.lower() == 'keep':
            await message1.edit(content="It's all yours now :)")
            await message2.delete()
            os.rename("./Pics/" + author[:-5] + "_weap_temp.png", "./Pics/" + author[:-5] + "_weap.png")
            await asyncio.sleep(20)
            await message1.delete()
        else:
            os.remove("./Pics/" + author[:-5] + "_weap_temp.png")
            await message2.delete()
            await message1.edit(content="Well I'm still charging, you...")
            await asyncio.sleep(20)
            await message1.delete()
        data[author]["score"] = money

    with open(filename, "w") as file:
        json.dump(data, file)
    return

async def rollthedice(ctx, args):
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
        msg = str(user[:-5]) + ' has ' + str(userdata[x]['score']) + ' marcs!'
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


async def welcome(client, guild):
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
