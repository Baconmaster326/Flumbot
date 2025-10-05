import os
import discord
import requests
import miditoaudio
import random
import asyncio
import voiceplay
import json
import asyncpraw
from asyncprawcore import NotFound
from PIL import Image, ImageFont, ImageDraw

winners = []
cheaters = []
answer = 0


class answer_choices(discord.ui.View):
    global winners
    global cheaters
    @discord.ui.button(label="Answer A", style=discord.ButtonStyle.primary)
    async def A_button_callback(self, interaction, button):
        if interaction.user in cheaters:
            return
        button.disabled = True
        if answer == 1:
            winners.append(interaction.user)
        cheaters.append(interaction.user)
        await interaction.response.edit_message(view=self)  # edit the message's view
    @discord.ui.button(label="Answer B", style=discord.ButtonStyle.secondary)
    async def B_button_callback(self, interaction, button):
        if interaction.user in cheaters:
            return
        button.disabled = True
        if answer == 2:
            winners.append(interaction.user)
        cheaters.append(interaction.user)
        await interaction.response.edit_message(view=self)  # edit the message's view
    @discord.ui.button(label="Answer C", style=discord.ButtonStyle.success)
    async def C_button_callback(self, interaction, button):
        if interaction.user in cheaters:
            return
        button.disabled = True
        if answer == 3:
            winners.append(interaction.user)
        cheaters.append(interaction.user)
        await interaction.response.edit_message(view=self)  # edit the message's view
    @discord.ui.button(label="Answer D", style=discord.ButtonStyle.danger)
    async def D_button_callback(self, interaction, button):
        if interaction.user in cheaters:
            return
        button.disabled = True
        if answer == 4:
            winners.append(interaction.user)
        cheaters.append(interaction.user)
        await interaction.response.edit_message(view=self)  # edit the message's view

async def midimania(ctx, client, dx=False):
    global winners
    global answer
    global cheaters

    channel = ctx.channel

    if dx:
        midilocation = './Music/MIDIDX'
    else:
        midilocation = './Music/MIDI'

    # clear winner and cheater list
    winners.clear()
    cheaters.clear()
    answer = 0
    printable = ":sad:"

    for file in os.listdir("./"):  # clear previous midis justincase
        if file.endswith(".wav"):
            os.remove(file)
    await ctx.send("Launching midimania!", ephemeral=True, delete_after=float(1))
    msg = await channel.send("Please wait while I prepare your midi :)", tts=True)
    midifiles = []
    filenames = []
    soundfonts = []
    # gather list of possible midis
    for dirpath, subdirs, files in os.walk(midilocation):
        for x in files:
            if x.endswith(".mid"):
                filenames.append(x)
                midifiles.append(os.path.join(dirpath, x))
    # gather list of possible soundfonts
    for dirpath, subdirs, files in os.walk('./Music/'):
        for x in files:
            if x.endswith(".sf2"):
                soundfonts.append(os.path.join(dirpath, x))
    # pick a soundfont
    soundfont = random.choice(soundfonts)
    # format soundfont for printing
    printsound = soundfont.split('/')[-1]
    # pick random midi
    cliplocation = random.choice(midifiles)
    # convert to midi to wav
    miditoaudio.to_audio(soundfont, cliplocation, './', out_type='wav')
    person = os.path.split(cliplocation)
    person = person[1]
    place = str(person[:-4]) + '.wav'
    await msg.delete()
    msg = f"It's time to guess that Midi!\nYou'll have 30 seconds to pick the correct song from 4 " \
          f"choices\nPICK ONLY ONE TIME\nI'll play it to you with {printsound}"
    msg = await channel.send(msg, tts=True)
    await asyncio.sleep(14)
    await msg.delete()
    await voiceplay.playclip(place, ctx, client, 30)
    await asyncio.sleep(3)

    # delete converted midi
    os.remove(place)
    select = random.randint(1, 4)
    answer = select
    A, B, C, D = ' ', ' ', ' ', ' '
    test = os.listdir(midilocation)
    samples = random.sample(midifiles, 4)
    for index, each in enumerate(samples):
        samples[index] = os.path.split(each)[1]
    A, B, C, D = str(samples[0])[:-4], str(samples[1])[:-4], str(samples[2])[:-4], str(samples[3])[:-4]
    while A == person or B == person or C == person or D == person:
        print("repetition detected")
        samples = random.sample(midifiles, 4)
        A, B, C, D = str(samples[0])[:-4], str(samples[1])[:-4], str(samples[2])[:-4], str(samples[3])[:-4]

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
        color=discord.Colour.blurple(),
    )
    embed3 = discord.Embed(
        title=f"B - {B}",
        color=discord.Colour.greyple(),
    )
    embed4 = discord.Embed(
        title=f"C - {C}",
        color=discord.Colour.green(),
    )
    embed5 = discord.Embed(
        title=f"D - {D}",
        color=discord.Colour.red(),
    )

    msg1 = await channel.send(embed=embed1)
    msg2 = await channel.send(embed=embed2)
    msg3 = await channel.send(embed=embed3)
    msg4 = await channel.send(embed=embed4)
    msg5 = await channel.send(embed=embed5, view=answer_choices())

    await asyncio.sleep(30)

    await msg1.delete()
    await msg2.delete()
    await msg3.delete()
    await msg4.delete()
    await msg5.delete()


    await winnerlist(ctx, printable, 50)

async def geddit(ctx, client):
    global winners
    global answer
    global cheaters

    channel = ctx.channel

    winners.clear()
    cheaters.clear()
    answer = 0
    printable = ":sad:"

    with open('token.json', "r") as file:
        data = json.load(file)
    rtoken = data['token'][2]
    reddit = asyncpraw.Reddit(client_id='zQodI26PnfVmAhgdZogiLA',
                              client_secret=rtoken,
                              user_agent='FlumbotAPRAW')
    await ctx.send("Launching geddit!", ephemeral=True, delete_after=float(3))
    id = []
    subreddit = []
    tempreddit = await reddit.subreddit("all")
    async for submission in tempreddit.hot(limit=250):
        id.append(submission.id)
        subreddit.append(submission.subreddit.display_name)
    post = await reddit.submission(id=random.choice(id))
    person = post.subreddit.display_name
    link = "https://reddit.com" + post.permalink
    msg = "It's time for GEDDIT!\nYou'll have 30 seconds to determine what subreddit the following r/all post came " \
          "from.\nPICK ONLY ONE TIME!!!"
    msg = await channel.send(msg, tts=True)
    await asyncio.sleep(12)
    await msg.delete()

    samples = random.sample(subreddit, 4)
    select = random.randint(1, 4)
    answer = select
    A, B, C, D = samples[0], samples[1], samples[2], samples[3]
    while A == person or B == person or C == person or D == person:
        print("repetition detected")
        samples = random.sample(subreddit, 4)
        A, B, C, D = samples[0], samples[1], samples[2], samples[3]
    if select == 1:
        A = str(person)
        printable = ':regional_indicator_a:'
    if select == 2:
        B = str(person)
        printable = ':regional_indicator_b:'
    if select == 3:
        C = str(person)
        printable = ':regional_indicator_c:'
    if select == 4:
        D = str(person)
        printable = ':regional_indicator_d:'

    embed1 = discord.Embed(
        title=f"'{post.title}'",
        description="What is the subreddit that this title came from?",
        color=discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    )
    embed2 = discord.Embed(
        title=f"A - {A}",
        color=discord.Colour.blurple(),
    )
    embed3 = discord.Embed(
        title=f"B - {B}",
        color=discord.Colour.greyple(),
    )
    embed4 = discord.Embed(
        title=f"C - {C}",
        color=discord.Colour.green(),
    )
    embed5 = discord.Embed(
        title=f"D - {D}",
        color=discord.Colour.red(),
    )

    msg1 = await channel.send(embed=embed1)
    msg2 = await channel.send(embed=embed2)
    msg3 = await channel.send(embed=embed3)
    msg4 = await channel.send(embed=embed4)
    msg5 = await channel.send(embed=embed5, view=answer_choices())

    await asyncio.sleep(30)

    await msg1.delete()
    await msg2.delete()
    await msg3.delete()
    await msg4.delete()
    await msg5.delete()

    msg = f"The post was {link} from r/{post.subreddit}"
    await channel.send(msg, delete_after=15)

    await winnerlist(ctx, printable, 50)

async def gedditdx(ctx, client, args):
    global winners
    global answer
    global cheaters

    with open('token.json', "r") as file:
        data = json.load(file)
    rtoken = data['token'][2]
    reddit = asyncpraw.Reddit(client_id='zQodI26PnfVmAhgdZogiLA',
                              client_secret=rtoken,
                              user_agent='FlumbotAPRAW')

    channel= ctx.channel

    winners.clear()
    cheaters.clear()
    answer = 0
    await ctx.send("Launching GedditDX!", ephemeral=True, delete_after=float(3))
    msg = await channel.send("Please wait while I peruse your subreddit :D", tts=True)
    id = []
    pics = []
    tempreddit = await reddit.subreddit(args)
    sr = tempreddit.hot(limit=250)
    try:
        async for submission in sr:
            if not submission.is_self:
                if submission.url.endswith('.jpg') or submission.url.endswith('.png'):
                    id.append(submission.id)
                    pics.append(submission.url)
    except Exception as e:
        await msg.delete()
        msg1 = await ctx.send("I'm having trouble with this subreddit, please make sure it exists, or isn't banned!")
        await asyncio.sleep(15)
        await msg1.delete()
        return
    if len(pics) < 4:
        print('loser posted a text only subreddit, let him know the news')
        await msg.delete()
        msg = "Your subreddit doesn't appear to have enough pictures I can use, please use a different one."
        msg1 = await ctx.send(msg)
        await asyncio.sleep(13)
        await msg1.delete()
        return False
    post = await reddit.submission(id=random.choice(id))
    while len(post.title) > 256:
        post = await reddit.submission(id=random.choice(id))
    person = post.url
    await msg.delete()
    if args.lower() != "all":
        msg = f"It's time to for GEDDITDX!\nYou'll have 30 seconds to determine what picture matches the title that came " \
              f"from r/{post.subreddit.display_name}\nPICK ONLY ONE TIME!!!"
    else:
        msg = f"It's time to for GEDDITDX!\nYou'll have 30 seconds to determine what picture matches the title that came " \
              f"from r/all\nPICK ONLY ONE TIME!!!"
    msg1 = await channel.send(msg, tts=True)
    await asyncio.sleep(12)
    await msg1.delete()
    embed = discord.Embed(title=post.title,
                          colour=discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255),
                                                         random.randint(0, 255)))
    samples = random.sample(pics, 4)
    select = random.randint(1, 4)
    answer = select
    A, B, C, D = samples[0], samples[1], samples[2], samples[3]
    while A == person or B == person or C == person or D == person:
        print("repetition detected")
        samples = random.sample(pics, 4)
        A, B, C, D = samples[0], samples[1], samples[2], samples[3]
    if select == 1:
        A = str(person)
        printable = ':regional_indicator_a:'
    if select == 2:
        B = str(person)
        printable = ':regional_indicator_b:'
    if select == 3:
        C = str(person)
        printable = ':regional_indicator_c:'
    if select == 4:
        D = str(person)
        printable = ':regional_indicator_d:'
    answers = [A, B, C, D]

    embed = discord.Embed(
        title=f"'{post.title}'",
        description=f"What picture matches this title from r/{args}",
        color=discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
    )

    msg = await channel.send(embed=embed)
    await getpicture(answers)
    message = await channel.send(file=discord.File('person.jpg'), view=answer_choices())

    for file in os.listdir("./"):
        if file.endswith(".jpg"):
            os.remove(file)

    await asyncio.sleep(30)
    await msg.delete()
    await message.delete()

    await winnerlist(ctx, printable, 100)


async def winnerlist(ctx, printable, mod):
    global winners

    channel = ctx.channel

    filename = './bin/en_data/userdata.json'
    with open(filename, "r") as file:
        data = json.load(file)
    msg = await channel.send(f"The correct answer was {printable}\n\nCongratulations to:\n", tts=True)

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
            title=f"{str(person)} now has {data[str(person)]['score']} marcs!",
            color=discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        )
        embed.set_thumbnail(url=person.avatar.url)
        im = Image.open("./Pics/blank.png")
        d = ImageDraw.Draw(im)
        location = (0, 10)
        text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        d.text(location, str(person), font=ImageFont.truetype(font='./Pics/sponge.ttf', size=56), fill=text_color)
        im.save("person.png")
        im.close()
        file = discord.File("person.png", filename="person.png")
        embed.set_image(url="attachment://person.png")
        await channel.send(file=file, embed=embed)
    with open(filename, "w") as file:
        json.dump(data, file)
    msg = "\n:clap::clap::clap::clap::clap::clap:\n"
    await channel.send(msg, tts=True)
    os.remove('person.png')

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
        if letter == 'A':
            text_color = 0xe74c3c
            location = (int(im.width*.02), int(im.height*.02))
        if letter == 'B':
            text_color = 0x99aab5
            location = (int(im.width*.92), int(im.height*.02))
        if letter == 'C':
            text_color = 0x2ecc71
            location = (int(im.width*.02), int(im.height*.92))
        if letter == 'D':
            text_color = 0x5865F2
            location = (int(im.width*.92), int(im.height*.92))
        d.text(location, letter, font=ImageFont.truetype(font='./Pics/sponge.ttf', size=fontsize), fill=text_color,
               stroke_width=fontwidth, stroke_fill="#000000")
    im.save("person.jpg")
    return True
