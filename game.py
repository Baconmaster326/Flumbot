import asyncio
import discord
import librosa
import random
import json
import art
from discord import FFmpegPCMAudio
from discord.utils import get

async def playsong(ctx,channel,client,cliplocation):
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio(cliplocation)
    source = discord.PCMVolumeTransformer(source)
    source.volume = 10.0
    player = voice.play(source)

async def start(ctx,client):
    filename = './bin/en_data/userdata.json'
    with open(filename, "r") as file:
        data = json.load(file)
    await ctx.message.delete()
    gameplayer = ctx.message.author
    x = str(gameplayer)
    try:
        # retrieve player level
        level = data[x]["inventory"]["level"][0]
    except KeyError:
        # new to game, give level
        try:
            # do they have a formatted inventory?
            data[x]["inventory"]["level"] = []
        except (KeyError, TypeError):
            # no inventory or old format
            try:
                # old inventory case
                data[x]["inventory"] = {}
            except KeyError:
                # no information case
                data[x] = {}
                data[x]["inventory"] = {}
        # safely assume new to game and create blank weapon and set to first level
        data[x]["inventory"]["level"] = []
        data[x]["inventory"]["weapon"] = []
        data[x]["inventory"]["level"].append(1)
        data[x]["inventory"]["level"].append("0/100")

    with open(filename, "w") as file:
        json.dump(data, file)

    try:
        channel = gameplayer.voice.channel
    except AttributeError:
        msg = "You'll need to be in a voicechannel to play this game"
        await ctx.send(msg)
        return
    print(str(gameplayer) + ' has started playing Flum Game')
    cliplocation = './Music/flumgame/opening.mp3'
    await playsong(ctx, channel, client, cliplocation)
    msg1 = """
        ```
        
                ███████╗██╗     ██╗   ██╗███╗   ███╗
                ██╔════╝██║     ██║   ██║████╗ ████║
                █████╗  ██║     ██║   ██║██╔████╔██║
                ██╔══╝  ██║     ██║   ██║██║╚██╔╝██║
                ██║     ███████╗╚██████╔╝██║ ╚═╝ ██║
                ╚═╝     ╚══════╝ ╚═════╝ ╚═╝     ╚═╝
                
                            TYPE READY!
        ```
        """
    msg2 = """
        ```      
                 ██████╗  █████╗ ███╗   ███╗███████╗
                ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
                ██║  ███╗███████║██╔████╔██║█████╗  
                ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
                ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
                 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                 
                            TYPE READY!
        ```
        """
    screen = await ctx.send(msg1)
    count = 100

    async def check(m):
        if (m.content.lower() == 'ready!' or m.content.lower() == 'ready') and (ctx.message.author == gameplayer):
            return True
        else:
            print('something aint right')
            return False


    while(count != 0):
        if count % 2 != 0:
            try:
                message = await client.wait_for('message', check=check, timeout=3)
                await message.delete()
            except asyncio.TimeoutError:
                await screen.edit(content=msg1)
                count -= 1
                continue
            break
        else:
            try:
                message = await client.wait_for('message', check=check, timeout=3)
                await message.delete()
            except asyncio.TimeoutError:
                await screen.edit(content=msg2)
                count -= 1
                continue
            break

    voice = get(client.voice_clients, guild=ctx.guild)
    player = voice.stop()
    await asyncio.sleep(2)

    if (count == 0):
        msg = 'You appear to be jamming to the title screen music, but not starting the game, sorry I must stop :('
        await ctx.send(msg)
        await ctx.voice_client.disconnect()
        await screen.delete()
        return

    # INSERT LOAD PROGRESS, FOR NOW IS JUST BLANK

    #if (progress == 0):
    cliplocation = './Music/flumgame/dialog.mp3'
    await playsong(ctx, channel, client, cliplocation)

    peter = """
                   ⡠⠔⠒⠉⢉⣉⣙⣒⣠⣀
            ⠀⠀⠀⢠⠊⠐⡞⢩⣭⣭⣭⣀⡔⣒⡚⠇
            ⠀⠀⠠⠁⠀⠀⠉⢿⡘⠃⣸⠃⠓⠒⢦⠌⢦⡀
            ⠀⢀⠇⠀⠀⠀⠀⠠⢍⡉⠁⠐⠦⠤⠞⡀⠀⠀⢣
            ⠀⠘⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠉⠉⢳⠄⠀⠸⡆
            ⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⠁⠀⠀⠀⠀⡇
            ⠀⡇⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⡇
            ⡠⡇⠀⠀⠀⠀⠀⠀⠀⢷⣄⣀⡴⣤⣀⠴⠁⠀⠀⡇
            ⢣⠘⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏
            ⠀⠑⣄⠈⠢⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⡰
            ⠀⠀⠈⠑⢄⡀⠁⠢⢄⡀⠀⠀⠀⠀⠀⢀⡠⠒⢁⠔
            ⠀⠀⠀⠀⠀⠈⠒⠤⣀⠀⠉⠒⡂⢤⡰⠫⣄⡰⠃
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠼⠀⠠⡷⡀⠈
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱
                
                
    """
    dialog = """``` {c}\n{txt} ```"""
    msg1 = dialog.format(c=peter, txt="I see you're finally awake")
    await screen.edit(content=msg1)
    await asyncio.sleep(5)
    msg1 = dialog.format(c=peter, txt="Time for you to see what the world has become.")
    await screen.edit(content=msg1)
    await asyncio.sleep(5)
    msg1 = dialog.format(c=peter, txt="Nothing but pain and misery if you ask me; you'll see soon enough.")
    await screen.edit(content=msg1)
    await asyncio.sleep(5)
    msg1 = dialog.format(c=peter, txt="Here you go kid, something to remember me by before you go.")
    await screen.edit(content=msg1)
    await asyncio.sleep(10)
    c = """         />_________________________________
[########[]__________________________________>
          \>"""
    msg1 = dialog.format(c=c, txt="\n\nYou recieved a <placeholder>") #+ nameofweapon + statblock)
    await screen.edit(content=msg1)
    await asyncio.sleep(10)
    cliplocation = './Music/flumgame/forest.mp3'
    voice = get(client.voice_clients, guild=ctx.guild)
    player = voice.stop()
    await asyncio.sleep(2)
    await playsong(ctx,channel,client,cliplocation)
    world = """```Forests of Flum\n\n{c}\n\n\n\nWhich way should I go?\n\n{e}\n{f}\n{g}```"""
    victories = 0
    trees = ["""               ,@@@@@@@,
                       ,,,.   ,@@@@@@/@@,  .oo8888o.
                    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
                   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
                   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
                   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
                   `&%\ ` /%&'    |.|        \ '|8'
                       |o|        | |         | |
                       |.|        | |         | |
                    \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_

""",
"""
         # #### ####
      ### \/#|### |/####
     ##\/#/ \||/##/_/##/_#
   ###  \/###|/ \/ # ###
 ##_\_#\_\## | #/###_/_####
## #### # \ #| /  #### ##/##
 __#_--###`  |{,###---###-~
           \ }{
            }}{
            }}{
            {{}
      , -=-~{ .-^- _
            `}
             {
"""]
    while victories != 10:
        desc = [0, 1, 2]
        for each in range(0, 3):
            i = random.choices(population=['neutral', 'bad', 'good'], weights=[.6, .3, .1])
            desc[each] = i[0]
        print(desc)
        neu = ["I'm not sure what lies in this direction.", "I can't tell if I should go this direction.", "I think I should go this way, but I'm not sure."]
        bad = ["I'm getting bad vibes from this direction", "I should prepare before heading this direction", "I do not think it would be wise to head here", "Evil is coming from that direction"]
        good = ["I can't help but be pulled in this direction", "This way beckons to me", "I got a good feeling about this direction", "It would be wise to go this way", "My map says to go this way"]

        for each in range(0, 3):
            if desc[each] == 'neutral':
                desc[each] = random.choice(neu)
            if desc[each] == 'good':
                desc[each] = random.choice(good)
            if desc[each] == 'bad':
                desc[each] = random.choice(bad)

        while desc[0] == desc[1] or desc[0] == desc[2] or desc[1] == desc[2]:
            for each in range(0, 3):
                if desc in neu:
                    desc[each] = random.choice(neu)
                if desc in good:
                    desc[each] = random.choice(good)
                if desc in bad:
                    desc[each] = random.choice(bad)
        msg1 = world.format(c=random.choice(trees), e=str('Straight: ' + desc[0]), f=str('Right: ' + desc[1]), g=str('Left: ' + desc[2]))
        await screen.edit(content=msg1)

    voice = get(client.voice_clients, guild=ctx.guild)
    player = voice.stop()
    await ctx.voice_client.disconnect()
    await screen.delete()



#async def end(ctx,client):