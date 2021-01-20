from __future__ import unicode_literals
import discord
import asyncio
import random
import os
import librosa
import json
import urllib.request
import string
import praw
import miditoaudio
import requests
from PIL import Image, ImageFont, ImageDraw
from discord import FFmpegPCMAudio
from discord.utils import get


async def playclip(cliplocation, ctx, client, overide):

    def check(m):
        return m.content.lower() == 'stop' or m.content.lower() == 'skip'

    
    try:
        channel = ctx.message.author.voice.channel
    except AttributeError:
        #msg = "Can't Fool me :triumph: you aren't even in the voice chat :triumph:"
        #await ctx.send(msg)
        return False
    print('starting to play clip')
    duration = librosa.get_duration(filename=cliplocation) + 1
    if (overide != 0):
        duration = overide
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    if duration > 60:
        source = FFmpegPCMAudio("./Clips/Oneoff/alert.wav")
        source = discord.PCMVolumeTransformer(source)
        source.volume = 10.0
        player = voice.play(source)
        await asyncio.sleep(5)
        player = voice.stop()
        await asyncio.sleep(1)
    source = FFmpegPCMAudio(cliplocation)
    source = discord.PCMVolumeTransformer(source)
    source.volume = 10.0
    player = voice.play(source)
    try:
        await client.wait_for('message', check=check, timeout=duration)
        player = voice.stop()
        print('done playing clip')
        await ctx.voice_client.disconnect()
    except asyncio.TimeoutError:
        player = voice.stop()
        await ctx.voice_client.disconnect()
        print('done playing clip')
        return


async def midimania(ctx, client):
    for file in os.listdir("./"):
        if file.endswith(".wav"):
            os.remove(file)
    msg = await ctx.send("Please wait while I prepare your midi :)", tts=True)
    midifiles = []
    filenames = []
    for dirpath, subdirs, files in os.walk('./Music/MIDI'):
        for x in files:
            if x.endswith(".mid"):
                filenames.append(x)
                midifiles.append(os.path.join(dirpath, x))
    cliplocation = random.choice(midifiles)
    miditoaudio.to_audio('./Music/OPL2.sf2', cliplocation, './', out_type='wav')
    person = os.path.split(cliplocation)
    person = person[1]
    print(person)
    place = str(person[:-4]) + '.wav'
    await msg.delete()
    msg = "It's time to guess that Midi!\nYou'll have 30 seconds to pick the correct song from 4 choices\nPICK ONLY ONE TIME"
    await ctx.send(msg, tts=True)
    await asyncio.sleep(10)
    await playclip(place, ctx, client, 30)
    await asyncio.sleep(3)
    os.remove(place)
    select = random.randint(1, 4)
    A, B, C, D = ' ', ' ', ' ', ' '
    samples = random.sample(os.listdir('./Music/MIDI/'), 4)
    A, B, C, D = samples[0], samples[1], samples[2], samples[3]
    while (A == person or B == person or C == person or D == person):
        print("repetition detected")
        samples = random.sample(os.listdir('./Music/MIDI/'), 4)
        A, B, C, D = samples[0], samples[1], samples[2], samples[3]
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

    msg = "Was it\n:regional_indicator_a:\t\u21e6\t" + A[:-4] + "\n:regional_indicator_b:\t\u21e6\t" + B[
                                                                                                       :-4] + "\n:regional_indicator_c:\t\u21e6\t" + C[
                                                                                                                                                     :-4] + "\n:regional_indicator_d:\t\u21e6\t" + D[
                                                                                                                                                                                                   :-4]
    message = await ctx.send(msg)
    await message.add_reaction('\U0001F1E6')
    await message.add_reaction('\U0001F1E7')
    await message.add_reaction('\U0001F1E8')
    await message.add_reaction('\U0001F1E9')
    return answer, printable


async def midimaniadx(ctx, client):
    for file in os.listdir("./"):
        if file.endswith(".wav"):
            os.remove(file)
    msg = await ctx.send("Please wait while I prepare your midi :)")
    midifiles = []
    filenames = []
    for dirpath, subdirs, files in os.walk('./Music/MIDIDX'):
        for x in files:
            if x.endswith(".mid"):
                filenames.append(x)
                midifiles.append(os.path.join(dirpath, x))
    cliplocation = random.choice(midifiles)
    miditoaudio.to_audio('./Music/OPL2.sf2', cliplocation, './', out_type='wav')
    person = os.path.split(cliplocation)
    person = person[1]
    print(person)
    place = str(person[:-4]) + '.wav'
    await msg.delete()
    msg = "It's time to for MidimaniaDX \nP \nO \nG\nYou'll have 30 seconds to pick the correct song from 4 questionable choices, pick only one time"
    await ctx.send(msg, tts=True)
    await asyncio.sleep(20)
    await playclip(place, ctx, client, 30)
    await asyncio.sleep(3)
    os.remove(place)
    select = random.randint(1, 4)
    A, B, C, D = ' ', ' ', ' ', ' '
    samples = random.sample(filenames, 4)
    A, B, C, D = samples[0], samples[1], samples[2], samples[3]
    while (A == person or B == person or C == person or D == person):
        print("repetition detected")
        samples = random.sample(filenames, 4)
        A, B, C, D = samples[0], samples[1], samples[2], samples[3]
    if select == 1:
        A = str(person)
        answer = '\U0001F1E6'
        printable = ':regional_indicator_a:'
    if select == 2:
        B = str(person)
        answer = '\U0001F1E7'
        printable = ':regional_indicator_b:'
    if select == 3:
        C = str(person)
        answer = '\U0001F1E8'
        printable = ':regional_indicator_c:'
    if select == 4:
        D = str(person)
        answer = '\U0001F1E9'
        printable = ':regional_indicator_d:'

    msg = "Was it\n:regional_indicator_a:\t\u21e6\t" + A[:-4] + "\n:regional_indicator_b:\t\u21e6\t" + B[
                                                                                                       :-4] + "\n:regional_indicator_c:\t\u21e6\t" + C[
                                                                                                                                                     :-4] + "\n:regional_indicator_d:\t\u21e6\t" + D[
                                                                                                                                                                                                   :-4]
    message = await ctx.send(msg)
    await message.add_reaction('\U0001F1E6')
    await message.add_reaction('\U0001F1E7')
    await message.add_reaction('\U0001F1E8')
    await message.add_reaction('\U0001F1E9')
    return answer, printable


async def winnerlist(ctx, client, winners, printable, mod):
    filename = './bin/en_data/userdata.json'
    with open(filename, "r") as file:
        data = json.load(file)
    msg = "The correct answer was " + printable + "\n\nCongratulations to:\n"
    await ctx.send(msg, tts=True)
    if len(winners) == 0:
        data['Flumbot#1927']['score'] = data['Flumbot#1927']['score'] + mod
        await ctx.channel.send(file=discord.File('./Pics/flumbus.png'))
        msg = "Better luck next time folks! Flumbot has won, he has " + str(data['Flumbot#1927']['score']) + " marcs!"
        await ctx.send(msg)
        with open(filename, "w") as file:
            json.dump(data, file)
        return
    for x in winners:
        try:
            # add normally
            data[x]['score'] = data[x]['score'] + mod
        except KeyError:
            # no wallet found
            try:
                data[x]['score'] = mod
            except KeyError:
                # no entry found
                data[x] = {}
                data[x]['score'] = mod

        im = Image.open("./Pics/blank.png")
        d = ImageDraw.Draw(im)
        location = (0, 10)
        text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        d.text(location, x[:-5], font=ImageFont.truetype(font='./Pics/sponge.ttf', size=56), fill=text_color)
        im.save("person.png")
        await ctx.channel.send(file=discord.File('person.png'))
        os.remove('person.png')
        msg = x[:-5] + " has " + str(data[x]["score"]) + " marcs!"
        await ctx.send(msg)
    with open(filename, "w") as file:
        json.dump(data, file)
    msg = "\n:clap::clap::clap::clap::clap::clap:\n"
    await ctx.send(msg, tts=True)

async def getpicture(links):
    x = 0
    for image in links:
        print(image)
        img_data = requests.get(image).content
        with open('image'+str(x)+'.jpg', 'wb') as handler:
            handler.write(img_data)
        x += 1
    im1 = Image.open('./image0.jpg')
    im2 = Image.open('./image1.jpg')
    im3 = Image.open('./image2.jpg')
    im4 = Image.open('./image3.jpg')


    def get_concat_h_multi_resize(im_list, resample=Image.BICUBIC):
        min_height = min(im.height for im in im_list)
        im_list_resize = [im.resize((int(im.width * min_height / im.height), min_height), resample=resample)
                          for im in im_list]
        total_width = sum(im.width for im in im_list_resize)
        dst = Image.new('RGB', (total_width, min_height))
        pos_x = 0
        for im in im_list_resize:
            dst.paste(im, (pos_x, 0))
            pos_x += im.width
        return dst

    def get_concat_v_multi_resize(im_list, resample=Image.BICUBIC):
        min_width = min(im.width for im in im_list)
        im_list_resize = [im.resize((min_width, int(im.height * min_width / im.width)), resample=resample)
                          for im in im_list]
        total_height = sum(im.height for im in im_list_resize)
        dst = Image.new('RGB', (min_width, total_height))
        pos_y = 0
        for im in im_list_resize:
            dst.paste(im, (0, pos_y))
            pos_y += im.height
        return dst

    def get_concat_tile_resize(im_list_2d, resample=Image.BICUBIC):
        im_list_v = [get_concat_h_multi_resize(im_list_h, resample=resample) for im_list_h in im_list_2d]
        return get_concat_v_multi_resize(im_list_v, resample=resample)

    get_concat_tile_resize([[im1, im2],
                            [im3, im4]]).save('./image4.jpg')

    im = Image.open("./image4.jpg")
    d = ImageDraw.Draw(im)
    letters = ['A', 'B', 'C', 'D']
    fontsize = int(.05*im.width)
    fontwidth = int(im.width*.0075)
    for letter in letters:
        text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if letter == 'A':
            location = (int(im.width*.02), int(im.height*.02))
        if letter == 'B':
            location = (int(im.width*.92), int(im.height*.02))
        if letter == 'C':
            location = (int(im.width*.02), int(im.height*.92))
        if letter == 'D':
            location = (int(im.width*.92), int(im.height*.92))
        d.text(location, letter, font=ImageFont.truetype(font='./Pics/sponge.ttf', size=fontsize), fill=text_color,
               stroke_width=fontwidth, stroke_fill="#000000")
    im.save("person.jpg")
    return True


async def geddit(ctx, client):
    reddit = praw.Reddit(client_id='kyPylZpqbbNzdg',
                         client_secret='3xCZsd2Ib5GHwM_lkV8F5MzEUYI',
                         username='FlumbotPRAW',
                         password='somebodyring?',
                         user_agent='flumbot')
    id = []
    subreddit = []
    for submission in reddit.subreddit("all").hot(limit=100):
        id.append(submission.id)
        subreddit.append(submission.subreddit.display_name)
    post = reddit.submission(id=random.choice(id))
    person = post.subreddit.display_name
    link = "https://reddit.com" + post.permalink
    msg = "It's time for GEDDIT!\nYou'll have 30 seconds to determine what subreddit the following r/all post came " \
          "from.\nPICK ONLY ONE TIME!!!"
    await ctx.send(msg, tts=True)
    await asyncio.sleep(12)
    embed = discord.Embed(title=post.title,
                          colour=discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255),
                                                         random.randint(0, 255)))
    await ctx.send(embed=embed)
    samples = random.sample(subreddit, 4)
    select = random.randint(1, 4)
    A, B, C, D = samples[0], samples[1], samples[2], samples[3]
    while (A == person or B == person or C == person or D == person):
        print("repetition detected")
        samples = random.sample(subreddit, 4)
        A, B, C, D = samples[0], samples[1], samples[2], samples[3]
    if select == 1:
        A = str(person)
        answer = '\U0001F1E6'
        printable = ':regional_indicator_a:'
    if select == 2:
        B = str(person)
        answer = '\U0001F1E7'
        printable = ':regional_indicator_b:'
    if select == 3:
        C = str(person)
        answer = '\U0001F1E8'
        printable = ':regional_indicator_c:'
    if select == 4:
        D = str(person)
        answer = '\U0001F1E9'
        printable = ':regional_indicator_d:'

    msg = "Was it\n:regional_indicator_a:\t\u21e6\tr/" + A + "\n:regional_indicator_b:\t\u21e6\tr/" + B + "\n:regional_indicator_c:\t\u21e6\tr/" + C + "\n:regional_indicator_d:\t\u21e6\tr/" + D
    message = await ctx.send(msg)
    await message.add_reaction('\U0001F1E6')
    await message.add_reaction('\U0001F1E7')
    await message.add_reaction('\U0001F1E8')
    await message.add_reaction('\U0001F1E9')
    return answer, printable, link


async def gedditdx(ctx, client, args):
    reddit = praw.Reddit(client_id='kyPylZpqbbNzdg',
                         client_secret='3xCZsd2Ib5GHwM_lkV8F5MzEUYI',
                         username='FlumbotPRAW',
                         password='somebodyring?',
                         user_agent='flumbot')
    id = []
    pics = []
    sr = reddit.subreddit(args).hot(limit=300)
    for submission in sr:
        if not submission.is_self:
            if submission.url.endswith('.jpg') or submission.url.endswith('.png'):
                id.append(submission.id)
                pics.append(submission.url)
    if len(pics) < 4:
        print('loser posted a text only subreddit, let him know the news')
        msg = "Your subreddit doesn't appear to have enough pictures I can use, please use a different one."
        await ctx.send(msg)
        return False
    post = reddit.submission(id=random.choice(id))
    while len(post.title) > 256:
        post = reddit.submission(id=random.choice(id))
    person = post.url
    msg = "It's time to for GEDDITDX!\nYou'll have 30 seconds to determine what picture matches the title that came " \
          "from r/" + post.subreddit.display_name + "\nPICK ONLY ONE TIME!!!"
    if args == 'all':
        msg = "It's time to for GEDDITDX!\nYou'll have 30 seconds to determine what picture matches the title that " \
              "came from r/all\nPICK ONLY ONE TIME!!!"
    await ctx.send(msg, tts=True)
    await asyncio.sleep(12)
    embed = discord.Embed(title=post.title,
                          colour=discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255),
                                                         random.randint(0, 255)))
    samples = random.sample(pics, 4)
    select = random.randint(1, 4)
    A, B, C, D = samples[0], samples[1], samples[2], samples[3]
    while A == person or B == person or C == person or D == person:
        print("repetition detected")
        samples = random.sample(pics, 4)
        A, B, C, D = samples[0], samples[1], samples[2], samples[3]
    if select == 1:
        A = str(person)
        answer = '\U0001F1E6'
        printable = ':regional_indicator_a:'
    if select == 2:
        B = str(person)
        answer = '\U0001F1E7'
        printable = ':regional_indicator_b:'
    if select == 3:
        C = str(person)
        answer = '\U0001F1E8'
        printable = ':regional_indicator_c:'
    if select == 4:
        D = str(person)
        answer = '\U0001F1E9'
        printable = ':regional_indicator_d:'
    answers = [A, B, C, D]
    await ctx.send(embed=embed)
    await getpicture(answers)
    message = await ctx.channel.send(file=discord.File('person.jpg'))
    for file in os.listdir("./"):
        if file.endswith(".jpg"):
            os.remove(file)
    await message.add_reaction('\U0001F1E6')
    await message.add_reaction('\U0001F1E7')
    await message.add_reaction('\U0001F1E8')
    await message.add_reaction('\U0001F1E9')
    return answer, printable
