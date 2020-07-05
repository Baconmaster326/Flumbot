from __future__ import unicode_literals
import discord
import asyncio
import random
import os
import librosa
import json
from discord import FFmpegPCMAudio
from discord.utils import get

async def playclip(cliplocation,ctx,client,overide):
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
    source = FFmpegPCMAudio(cliplocation)
    source = discord.PCMVolumeTransformer(source)
    source.volume = 1.5
    player = voice.play(source)
    await asyncio.sleep(duration)
    player = voice.stop()
    await ctx.voice_client.disconnect()
    print('done playing clip')
    return

async def midimania(ctx,client):
    msg = "It's time to guess that Midi!\nYou'll have 30 seconds to pick the correct song from 4 choices\nPICK ONLY ONE TIME"
    await ctx.send(msg, tts = True)
    await asyncio.sleep(10)
    person = str(random.choice(os.listdir('./Music/MIDI/')))
    cliplocation = './Music/MIDI/' + person
    await playclip(cliplocation,ctx,client,30)
    select = random.randint(1,4)
    A,B,C,D = ' ' , ' ' , ' ' , ' '
    samples = random.sample(os.listdir('./Music/MIDI/'), 4)
    A,B,C,D = samples[0], samples[1], samples[2], samples[3]
    while(A == person or B == person or C == person or D == person):
        print("repetition detected")
        samples = random.sample(os.listdir('./Music/MIDI/'), 4)
        A,B,C,D = samples[0], samples[1], samples[2], samples[3]
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
        
    msg = "Was it\n:regional_indicator_a:\t\u21e6\t" + A[:-4] + "\n:regional_indicator_b:\t\u21e6\t" + B[:-4] + "\n:regional_indicator_c:\t\u21e6\t" + C[:-4] + "\n:regional_indicator_d:\t\u21e6\t" + D[:-4]
    message = await ctx.send(msg)
    await message.add_reaction('\U0001F1E6')
    await message.add_reaction('\U0001F1E7')
    await message.add_reaction('\U0001F1E8')
    await message.add_reaction('\U0001F1E9')
    return answer,printable

async def midimaniadx(ctx,client):
    msg = "It's time to for MidimaniaDX \nP \nO \nG\n You'll have 30 seconds to pick the correct song from 4 questionable choices, pick only one time"
    await ctx.send(msg, tts = True)
    await asyncio.sleep(20)
    person = str(random.choice(os.listdir('./Music/MIDIDX/')))
    cliplocation = './Music/MIDIDX/' + person
    await playclip(cliplocation,ctx,client,30)
    select = random.randint(1,4)
    A,B,C,D = ' ' , ' ' , ' ' , ' '
    samples = random.sample(os.listdir('./Music/MIDIDX/'), 4)
    A,B,C,D = samples[0], samples[1], samples[2], samples[3]
    while(A == person or B == person or C == person or D == person):
        print("repetition detected")
        samples = random.sample(os.listdir('./Music/MIDIDX/'), 4)
        A,B,C,D = samples[0], samples[1], samples[2], samples[3]
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
        
    msg = "Was it\n:regional_indicator_a:\t\u21e6\t" + A[:-4] + "\n:regional_indicator_b:\t\u21e6\t" + B[:-4] + "\n:regional_indicator_c:\t\u21e6\t" + C[:-4] + "\n:regional_indicator_d:\t\u21e6\t" + D[:-4]
    message = await ctx.send(msg)
    await message.add_reaction('\U0001F1E6')
    await message.add_reaction('\U0001F1E7')
    await message.add_reaction('\U0001F1E8')
    await message.add_reaction('\U0001F1E9')
    return answer,printable

async def winnerlist(ctx,client,winners,printable,mod):
    winnermsg = ''
    with open("userdata.json", "r") as file:
        data = json.load(file)
    msg = "The correct answer was " + printable + "\n\nCongratulations to:\n"
    await ctx.send(msg , tts = True)
    if len(winners) == 0:
        data['Flumbot#1927']['score'] = data['Flumbot#1927']['score'] + mod
        await ctx.channel.send(file=discord.File('./Pics/flumbus.png'))
        msg = "Better luck next time folks! Flumbot has won, he has " + str(data['Flumbot#1927']['score']) + " marcs!"
        await ctx.send(msg)
        with open("userdata.json", "w") as file:
            json.dump(data, file)
        return
    for x in winners:
        print(x)
        try:
            data[x]['score'] = data[x]['score'] + mod
        except KeyError:
            try:
                data[x] = data[x]
                data[x]['score'] = mod
            except KeyError:
                data[x] = {}
                data[x]['score'] = mod
        if x == 'Baconmaster#3725':
            await ctx.channel.send(file=discord.File('./Pics/bacon.png'))
            msg = "Sean has " + str(data[x]['score']) + ' marcs!'
            await ctx.send(msg)
        if x == 'BOOF#4284':
            await ctx.channel.send(file=discord.File('./Pics/beef.png'))
            msg = "Niche has " + str(data[x]['score']) + " marcs!"
            await ctx.send(msg)
        if x == 'ShadowXII#7240':
            await ctx.channel.send(file=discord.File('./Pics/horse.png'))
            msg = "Marc has " + str(data[x]['score']) + " marcs!"
            await ctx.send(msg)
        if x == 'ratbuddy#9913':
            await ctx.channel.send(file=discord.File('./Pics/ratto.png'))
            msg = "Rat has " + str(data[x]['score']) + " marcs!"
            await ctx.send(msg)
        winnermsg = " ".join(x)
    with open("userdata.json", "w") as file:
        json.dump(data, file)
    msg = "Text lineup of winners are:"
    await ctx.send(msg)
    await ctx.send(winnermsg)
    msg = "\n:clap::clap::clap::clap::clap::clap:\n"
    await ctx.send(msg, tts = True)

