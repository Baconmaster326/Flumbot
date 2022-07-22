import os
import discord
import miditoaudio
import random
import asyncio
import voiceplay
import json
from PIL import Image, ImageFont, ImageDraw

winners = []
cheaters = []
answer = 0


class answer_choices(discord.ui.View):
    global winners
    global cheaters
    @discord.ui.button(label="Answer A", style=discord.ButtonStyle.primary)
    async def A_button_callback(self, button, interaction):
        if interaction.user in cheaters:
            return
        if answer == 1:
            winners.append(interaction.user)
        cheaters.append(interaction.user)
        await interaction.response.edit_message(view=self)  # edit the message's view
    @discord.ui.button(label="Answer B", style=discord.ButtonStyle.secondary)
    async def B_button_callback(self, button, interaction):
        if interaction.user in cheaters:
            return
        if answer == 2:
            winners.append(interaction.user)
        cheaters.append(interaction.user)
        await interaction.response.edit_message(view=self)  # edit the message's view
    @discord.ui.button(label="Answer C", style=discord.ButtonStyle.success)
    async def C_button_callback(self, button, interaction):
        if interaction.user in cheaters:
            return
        if answer == 3:
            winners.append(interaction.user)
        cheaters.append(interaction.user)
        await interaction.response.edit_message(view=self)  # edit the message's view
    @discord.ui.button(label="Answer D", style=discord.ButtonStyle.danger)
    async def D_button_callback(self, button, interaction):
        if interaction.user in cheaters:
            return
        if answer == 4:
            winners.append(interaction.user)
        cheaters.append(interaction.user)
        await interaction.response.edit_message(view=self)  # edit the message's view

async def midimania(ctx, client):
    global winners
    global answer
    global cheaters

    winners.clear()
    cheaters.clear()
    answer = 0

    for file in os.listdir("./"):  # clear previous midis justincase
        if file.endswith(".wav"):
            os.remove(file)
    await ctx.respond("Launching midimania!", ephemeral=True, delete_after=float(1))
    msg = await ctx.send("Please wait while I prepare your midi :)", tts=True)
    midifiles = []
    filenames = []
    soundfonts = []
    for dirpath, subdirs, files in os.walk('./Music/MIDI'):
        for x in files:
            if x.endswith(".mid"):
                filenames.append(x)
                midifiles.append(os.path.join(dirpath, x))
    for dirpath, subdirs, files in os.walk('./Music/'):
        for x in files:
            if x.endswith(".sf2"):
                soundfonts.append(os.path.join(dirpath, x))
    soundfont = random.choice(soundfonts)
    printsound = soundfont.split('/')[-1]
    cliplocation = random.choice(midifiles)
    miditoaudio.to_audio(soundfont, cliplocation, './', out_type='wav')
    person = os.path.split(cliplocation)
    person = person[1]
    place = str(person[:-4]) + '.wav'
    await msg.delete()
    msg = f"It's time to guess that Midi!\nYou'll have 30 seconds to pick the correct song from 4 " \
          f"choices\nPICK ONLY ONE TIME\nI'll play it to you with {printsound}"
    msg = await ctx.send(msg, tts=True)
    await asyncio.sleep(14)
    await msg.delete()
    await voiceplay.playclip(place, ctx, client, 30)
    await asyncio.sleep(3)

    os.remove(place)
    select = random.randint(1, 4)
    answer = select
    A, B, C, D = ' ', ' ', ' ', ' '
    samples = random.sample(os.listdir('./Music/MIDI/'), 4)
    A, B, C, D = samples[0], samples[1], samples[2], samples[3]
    while A == person or B == person or C == person or D == person:
        print("repetition detected")
        samples = random.sample(os.listdir('./Music/MIDI/'), 4)
        A, B, C, D = samples[0], samples[1], samples[2], samples[3]

    if select == 1:
        A = str(person)[:-4]
        printable = ':regional_indicator_a:'
    if select == 2:
        B = str(person)[:-4]
        printable = ':regional_indicator_b:'
    if select == 3:
        C = str(person)[:-4]
        printable = ':regional_indicator_c:'
    if select == 4:
        D = str(person)[:-4]
        printable = ':regional_indicator_d:'

    embed1 = discord.Embed(
        title="Midimania",
        description="What song did you just hear?!",
        color=discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    )
    embed2 = discord.Embed(
        title=f"A - {A}",
        color=discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    )
    embed3 = discord.Embed(
        title=f"B - {B}",
        color=discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    )
    embed4 = discord.Embed(
        title=f"C - {C}",
        color=discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    )
    embed5 = discord.Embed(
        title=f"D - {D}",
        color=discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    )

    msg1 = await ctx.send(embed=embed1)
    msg2 = await ctx.send(embed=embed2)
    msg3 = await ctx.send(embed=embed3)
    msg4 = await ctx.send(embed=embed4)
    msg5 = await ctx.send(embed=embed5, view=answer_choices())

    await asyncio.sleep(30)

    await msg1.delete()
    await msg2.delete()
    await msg3.delete()
    await msg4.delete()
    await msg5.delete()


    await winnerlist(ctx, printable, 50)

async def winnerlist(ctx, printable, mod):
    global winners
    filename = './bin/en_data/userdata.json'
    with open(filename, "r") as file:
        data = json.load(file)
    msg = await ctx.send(f"The correct answer was {printable}\n\nCongratulations to:\n", tts=True)

    if len(winners) == 0:
        winners.append(ctx.me)

    for x in winners:
        x = str(x)
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

    for person in winners:
        embed = discord.Embed(
            title=f"{str(person)[:-5]} now has {data[str(person)]['score']} marcs!",
            color=discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        )
        embed.set_thumbnail(url=person.avatar.url)
        im = Image.open("./Pics/blank.png")
        d = ImageDraw.Draw(im)
        location = (0, 10)
        text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        d.text(location, str(person)[:-5], font=ImageFont.truetype(font='./Pics/sponge.ttf', size=56), fill=text_color)
        im.save("person.png")
        im.close()
        file = discord.File("person.png", filename="person.png")
        embed.set_image(url="attachment://person.png")
        await ctx.send(file=file, embed=embed)
    with open(filename, "w") as file:
        json.dump(data, file)
    msg = "\n:clap::clap::clap::clap::clap::clap:\n"
    await ctx.send(msg, tts=True)
    os.remove('person.png')