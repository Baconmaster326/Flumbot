import asyncio
import discord
from discord.ext import bridge
from discord.ext.commands import CommandNotFound
import check_raw_text
import check_count
import voiceplay
import os
import random
import games

pilot = 0

client = bridge.Bot(command_prefix='', intents=discord.Intents.all(), case_insensitive=True)

@client.event
async def on_ready():
    print('---------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------')



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    messagetobot = str(message.content)
    user = str(message.author)[:-5]
    channel = message.channel.name
    guild = message.channel.guild.name
    print(f"=========\n{user} said {messagetobot} in {channel} || {guild}\nchecking for commands...")

    print("\n=====Nothing else found, proceed to read commands=====\n")
    await check_raw_text.parse(message)

    if len(str(message.content).split()) == 1:
        await check_count.parse(message)


    await client.process_commands(message)

@client.bridge_command(name = "midimania", description= "The hit new game hosted by yours truly", pass_context= True)
async def Midimania(ctx):
    await games.midimania(ctx, client)

@client.bridge_command(name = "gamble", description= "House always wins", pass_context= True)
async def gamble(ctx):
    mp3files = []
    for dirpath, subdirs, files in os.walk('./Clips'):
        for x in files:
            if x.endswith(".mp3") or x.endswith(".wav"):
                mp3files.append(os.path.join(dirpath, x))
    cliplocation = random.choice(mp3files)
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name = "autopilot", description= "Let flumbot gamble his life away", pass_context= True)
async def autopilot(ctx):
    global pilot
    pilot = 1
    timer = 0
    await ctx.respond("Autopilot engaged, to turn off type 'off'", ephemeral=True, delete_after=3)
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

@client.bridge_command(name = "off", description= "Turn off autopilot :(", pass_context= True)
async def off(ctx):
    global pilot
    pilot = 0
    server = ctx.guild.voice_client
    try:
        await server.disconnect()
    except AttributeError:
        print("he wasn't in a voice channel")
    await ctx.respond("I'm going to <@100562084894371840> on you", ephemeral=True, delete_after=3)
    print('autopilot off')

@client.bridge_command(name = "football", description= "The new John Madden game sounds pretty good.", pass_context= True)
async def football(ctx):
    await ctx.respond("HI EVERYONE AND WELCOME TO JOHN MADDEN FOOTBALL!!!", delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/Futbol.mp3', ctx, client, 0)

@client.bridge_command(name='bruh', description='For the bruh moments in our lives', pass_context=True)
async def bruh(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/bruh.mp3', ctx, client, 0)

@client.bridge_command(name='baba', description='Meaty Chairs and Baba Yetus', pass_context=True)
async def baba(ctx):
    await ctx.respond("you got it boss", delete_after=float(10), ephemeral=True)
    await voiceplay.playclip('./Clips/Oneoff/babayeet.mp3', ctx, client, 0)

@client.bridge_command(name='thomas', description='Thomas coming through', pass_context=True)
async def thomas(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/thomas.mp3', ctx, client, 0)

@client.bridge_command(name='fridge', description='Classico Flumico', pass_context=True)
async def fridge(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/oof.mp3', ctx, client, 0)

@client.bridge_command(name='clap', description='clap', pass_context=True)
async def clap(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/clap.mp3', ctx, client, 0)

@client.bridge_command(name='keyboard', description='I hear a keyboard round here', pass_context=True)
async def keyboard(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/keyboard.mp3', ctx, client, 0)

@client.bridge_command(name='chum', description='Gnot for the weak of heart', pass_context=True)
async def chum(ctx):
    await ctx.respond(":tired_face: You've been gnomed! :tired_face:", delete_after=float(10), tts=True)
    await voiceplay.playclip('./Clips/Oneoff/chum.mp3', ctx, client, 0)

@client.bridge_command(name='knock', description='Who is it? MonkaS', pass_context=True)
async def knock(ctx):
    await ctx.respond("monster", ephemeral=True, delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/knock.mp3', ctx, client, 0)

@client.bridge_command(name='cocaine', description='I am Impotent Rage', pass_context=True)
async def cocaine(ctx):
    await ctx.respond("Okay Mr. Phillips", ephemeral=True, delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/trevor.mp3', ctx, client, 0)

@client.bridge_command(name='futbol', description='A modern spin on a classic clip', pass_context=True)
async def futbol(ctx):
    await ctx.respond("HI EVERYONE AND WELCOME TO JOHN MADDEN FOOT!", delete_after=float(10))
    await voiceplay.playclip('./Clips/Oneoff/Fut.mp3', ctx, client, 0)

@client.bridge_command(name='spongebob', description='You gotta lick the Marble', pass_context=True)
async def spongebob(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/spongebob/')))
    cliplocation = './Clips/spongebob/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='funny', description='listen to what other people think is funny', pass_context=True)
async def usersub(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/usersub/')))
    cliplocation = './Clips/usersub/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='alexjones', description='Alex Jones screams about walruses', pass_context=True)
async def alexjones(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/alexjones/')))
    cliplocation = './Clips/alexjones/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='ramsay', description='Gordon Ramsay enlightens the chat', pass_context=True)
async def ramsay(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/ramsay/')))
    cliplocation = './Clips/ramsay/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='gleib', description='This is your Idiotest', pass_context=True)
async def gleib(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/gleib/')))
    cliplocation = './Clips/gleib/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='bigsmoke', description='Big Smoke gets Philisophical', pass_context=True)
async def bigsmoke(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/bigsmoke/')))
    cliplocation = './Clips/bigsmoke/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='prequel', description='wut', pass_context=True)
async def prequel(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/prequel/')))
    cliplocation = './Clips/prequel/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='meme', description='The biggest collection of memes since gamble', pass_context=True)
async def meme(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/meme/')))
    cliplocation = './Clips/meme/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='agent', description='Agent 14 tells you what to do', pass_context=True)
async def agent(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/agent14/')))
    cliplocation = './Clips/agent14/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='trevor', description='Trevor...Phillips...Industries...', pass_context=True)
async def trevor(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/trevor/')))
    cliplocation = './Clips/trevor/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='lester', description='Because we do not hear Lester enough', pass_context=True)
async def lester(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/lester/')))
    cliplocation = './Clips/lester/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='joke', description='Biggest Laughs', pass_context=True)
async def joke(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/joke/')))
    cliplocation = './Clips/joke/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='iasip', description='Trashman comes to eat garbage', pass_context=True)
async def IASIP(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/IASIP/')))
    cliplocation = './Clips/IASIP/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='trump', description='We gotta build the wall', pass_context=True)
async def trump(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/trump/')))
    cliplocation = './Clips/trump/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='gameof', description='Booby B to our rescue', pass_context=True)
async def gameof(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/got/')))
    cliplocation = './Clips/got/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='fact', description='Bonzi knows so much', pass_context=True)
async def fact(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/facts/')))
    cliplocation = './Clips/facts/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='wwe', description='Hulk Hogan', pass_context=True)
async def wwe(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/wwe/')))
    cliplocation = './Clips/wwe/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='sports', description='NICE ON!', pass_context=True)
async def sports(ctx):
    await ctx.respond("you got it boss", ephemeral=True, delete_after=float(10))
    person = str(random.choice(os.listdir('./Clips/sports/')))
    cliplocation = './Clips/sports/' + person
    await voiceplay.playclip(cliplocation, ctx, client, 0)

@client.bridge_command(name='restart', description='kill flumbot only to make him stronger', pass_context=True)
async def restart(ctx):
    await ctx.respond("cry :(", ephemeral=True, delete_after=float(10))
    os.startfile('restart.py')
    exit()

@client.bridge_command(name='flip', description='flip a standard US coin', pass_context=True)
async def flip(ctx, *args):
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

@client.bridge_command(name='roll', description='roll any dice flumbot has', pass_context=True)
async def roll(ctx, sidedness: discord.Option(int), times: discord.Option(int), modifier: discord.Option(int)):
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

    await ctx.respond(content=str, ephemeral=True, delete_after=float(30))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        print("\t\t=====Nothing else found=====\t\t")
        return
    raise error

client.run("OTk5NDg2Njg5Mjc1ODI2MjY2.GF5FTx.vYGFLAZdxvrF8iJB2MDrOzUa36jZ2NbmeQ5vDQ")