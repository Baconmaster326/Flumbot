import discord
import ffmpeg
import asyncio
import random
import time
import os
import pickle
import string
import librosa
import urllib.request
from itertools import cycle
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
from sys import argv
from os import system
from urllib.error import HTTPError
from random import choice
#import big_smoke#
#import mad marc#

token = 'NTQ5OTk2NDI0NDIzNTM4Njg4.XaoWXw.n3ogBoE-kuyuOhxvRahKreL72ig'
client = commands.Bot(command_prefix = '', case_insensitive = True, )

thankin = open("thank.pickle" , "rb")
thank = int(pickle.load(thankin))
thankin.close()

#Things flumbot does on startup
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    flavorlist = ['Memeing since 1985', 'ok marc', 'Johnathan Cena', 'Watchmojo.com Top 10 Anime Bot Battles', 'https://www.youtube.com/watch?v=0gj-RYNhP8Y', \
                  'tinyurl.com/godisaliveandicanproveit', ':crab: Fortnite is Gone :crab:' , 'Windows 98 startup sound', 'LESTER CREST YOU ASSHOLE', \
                  'Pepperidge Farms remembers', 'We are praying for Puerto Rico, Puerto Rico', 'Shaq has The General Insurance', 'Kanye 2020', 'Marco Polo','Jesus Christ',\
                  'Chidlers guitar ;)', 'SmartShart', 'Belgium, which is basically a non-country', 'Buying a car today', 'High wuality midis', 'Spreadsheet simulator', 'Onion Knight',\
                  'Game of Thrones Season 8', 'HentaiHaven.org', 'http://nooooooooooooooo.com', 'dad', 'Slapchat' , 'https://tinyurl.com/Godisheretoday' ,'https://tinyurl.com/goodideasinhumanhistory (NSFW)',\
                  'https://tinyurl.com/hyperintelligentAI', 'marc cannot mute this']
    flavortown = str(random.choice(flavorlist))
    rando= int(random.randint(0,3))
    await client.change_presence(activity=discord.Game(name=flavortown, type=rando))

    awakelist = ["I'm Alive!!!", 'The boys are back in town', 'Go to bed now Marc', 'Oh hi Marc', 'Another day in the life of a British Chatbot', 'Good Morning Krusty Crew!',\
                 ':smiling_imp: Time to annoy :smiling_imp:', "You're going down WaifuBot", 'RIP AIRHORN SOLUTIONS', "Press F for Marc's sanity", 'Buzz Buzz', 'Loser, Loser, Loser, Looooooser',
                 'A nice video to start your day :) https://www.youtube.com/watch?v=pGzrL8J0t-c', '"I would never go to far when making this bot" - Sean', 'Marc said Jita', 'Give it up for Day 15, Day 15!',
                 '"I like flumbot he is so funny" - Nobody', 'Have I gone too far?', 'Fill out this survey to help us better understand how this bot could be improved \n https://www.strawpoll.me/18423333','Guess who',
                 'Marc has me muted :(','Riot','*naruto run*','OwO wuts twis', 'Uwu awake from a long slumber', 'Good morning Donald Trump, United States President number 44', 'Shoutouts to SimpleFlips',
                 'Throwback to LOLwut Pear','Checkout my obby course https://tinyurl.com/niceoneniche', 'This one is for the boys https://www.youtube.com/watch?v=26nnZSjtSqg', 'God was here','this makes marc mad', 'nice one marc'\
                 'shoutout to marc','marc turn on text commands','take these functions rat','bout to throw hands']          
    msg = str(random.choice(awakelist))
    
    channel = client.get_channel(137921870010777600)
    #await channel.send(msg)


    if len(argv) > 1:
            open = True

    opener = urllib.request.build_opener()
    opener.add_headers = [("User-agent", "Mozilla/5.0")]

    chars = string.ascii_letters + string.digits

    while True:

            imgPart = ''
            for i in range(5):
                    imgPart += choice(chars)
            url = "http://i.imgur.com/" + imgPart

            try:
                    opener.open(url)
                    print(url)
                    msg = "||" + url + "||"
                    #await channel.send(msg)
                    return
                    if open:
                            system("open " + url)
            except HTTPError:
                    print("found one that don't work")

#if anyone deletes a message do this I'll have no hidden messages from me
@client.event
async def on_message_delete(message):
    author = str(message.author)
    content = str(message.content)
    msg = 'Ladies and gentlemen, ' + '@' + author + " said, " + \
               content + ", which they promptly deleted. Making them tonight's biggest loser"
    await message.channel.send(msg)

@client.event
async def on_message(message):
    print("reading message")
    
    if message.author == client.user:
        return

    global thank
    messagetobot = str(message.content)
    splitme = str(messagetobot.lower())
    betcheck = splitme.split()

    if 'ok marc' in message.content.lower():
        msg = 'ok marc'
        await message.channel.send(msg)

    #dad-joke iniator boo-hoo marc got mega sad, re enable at some point
    if "i'm" in betcheck:
        dad = messagetobot.replace("I'm",'')
        msg = "Hi," + dad + ", I'm Flumbot, nice to meet you :)"
        await message.channel.send(msg)
        time.sleep (10)

    # DOnut ReMoVE NIChe!!!!
    # >:[ way to remove it niche >:[
    #better not remove my text or anything else
    if ('bet') in betcheck:
        wager = ['1 million doll hairs.', 'my diabetic cat photo collection.', 'my love for Jesus Christ.', 'my Kuruma.', 'Marc dying on the next Act 3.', \
                 'ratbuddy hating my code.', 'listening to Bonzi Buddy Jokes for 10 years.', 'Ratbuddy wanting more functions', 'Ratbuddy saying somthing about JSON',\
                 'water being the #1 cause of cancer', 'DJ Khaled is the messiah', 'Rhinehart knows', 'Emoji Movie 2 gets confirmed for 2020', 'Marc hates the bet command',\
                 'Marc has me muted right now', 'Jesus was a Jew', 'MP5 thats 2 more than 3 5', 'spreadsheet simulator is still boring', 'Marc is too smart to spend money' ,\
                 'Trump will build the wall', 'Flumbot is self-aware', 'Star Wars will be bought by me :)', 'Thanos will collect all the infinity stones and snap half the universe out of existence',\
                 'Sean will be at work, college, or not flumcapable', 'Sean will laugh at literally anything', 'Marc said Jita', 'Marc said Perimeter', 'Spreadsheet simulator makes everyone insane',\
                 'Nick will do something related to a video he saw but, no one else did and post it with no context', 'someone will make fun of what someone said', 'God is watching',\
                 'Marc will get mad', 'Toyota nation is a ethnicity', 'Marc stole a tree', 'Jesus was really a Roman, who was one of the first people to commit tax fraud', 'Taco Bell brings that dog back',\
                 'flumbot remastered will make ratbuddy slightly happy', 'flumbot remastered contains at least one function', 'there is nothing wrong with a little flumbot in your day',\
                 'a quote a day keeps the doctor away.', 'buttz is the password']
        wagerslt = str(random.choice(wager))
        msg = "I'll bet " + wagerslt
        await message.channel.send(msg)# tts=True)
        time.sleep(10)

    #thank flumbot for all the hard work he does (now persistent after resets PogChamp)
    if ('good bot') in messagetobot.lower():
        #get thank counter
        #increment by 1
        thank += 1
        #create and send message
        msg = 'Thank :clap: you :clap: are :clap: the :clap:' + str(thank) + 'th :clap: person :clap: to :clap: thank :clap: me. :clap:'
        await message.channel.send(msg)# tts=True)
        #save and dump the new thank counter
        thankout = open("thank.pickle", "wb")
        #lol pickle.dump
        pickle.dump(thank, thankout)
        thankout.close()
        time.sleep (10)

    if ('bad bot') in messagetobot.lower():
        #decrement by 1
        thank -= 1
        #create and send message
        msg = ':rage: You :rage: brought :rage: my :rage: thanks :rage: to :rage: ' + str(thank) + ' :rage: hope :rage: you :rage: feel :rage: good :rage:'
        await message.channel.send(msg)# tts=True)
        #save and dump the new thank counter
        thankout = open("thank.pickle", "wb")
        #lol pickle.dump
        pickle.dump(thank, thankout)
        thankout.close()
        time.sleep (10)

    #F's in chat for those we lost in the Area 51 raids
    if ('f') in betcheck:
        msg = 'F'
        await message.channel.send(msg)# tts=True)

    #alert chat of incoming flum
    if ('flum begun') in messagetobot.lower():
        msg = '@everyone It must be Flum time'
        await message.channel.send(msg)# tts=True)

    #nice way to tell if someone has posted a link in chat, also, nice.
    if ('http') in messagetobot.lower():
        msg = 'nice'
        await message.channel.send(msg)# tts=True)

    #Flumbot gets smarter everyday
    if ('flumbot') in messagetobot.lower():
        wager = ['thou shall not take the lords name in vain', 'you called', 'its your friend Simeon', 'who?', 'bow down to the king of Los Santos',\
                 'bet you cannot pickle these plums', ':crab:', 'Jesus Christ its Jason Bourne', 'knock knock', 'FBI OPEN UP', 'this is the Krusty Krab, may I take your order',\
                 'then to Mustafar we must go', 'Coruscant the Capital of the Rebuplic, the entire planet is one big city', 'A quote a day keeps the doctor away',\
                 'Hi Marc', 'Nice shoes', 'Jita', 'Perimeter', 'We are blessed and cursed', "I'm going to buy a car today", 'I will not get naked', "I'm Jonny on the Spot",\
                 "I'll hook you up", ':rage:', ':sweat_drops: :sweat_drops: :sweat_drops: :sweat_drops: :sweat_drops: :sweat_drops: :sweat_drops: :sweat_drops: :sweat_drops: :sweat_drops:',\
                 ':100: :poop: :100: :poop: :100: :poop: :100: :poop: :100: :poop: :100: :poop:',':a: :b: :a: :b: :a: :b: :a: :b: :a: :b: :a: :b: :a: :b: :a: :b:', 'Last Mistake, First Mistake', 'BRUH', 'Lets all order the Fortnite Burger the look on the workers faces will be EPIC', 'Pizza Time', 'Welcome to the Calzone Zone', \
                 'Hammer Down', 'Doctor', 'Excuse me', 'ok marc', 'nice functions', 'Pen Pinapple Apple', 'SAMMY G!', 'Kanye 2020', 'Puerto Rico, we are praying for Puerto Rico', 'Marc cannot die.',\
                 'But how will they feed Winterfell', 'FETCH THE BREASTPLATE STRETCHER', 'I am sorry for making this', 'Marc said Jita', ':crab: Cooldown is powerless :crab:', 'ping me bong', 'toke up', 'broke boy',\
                 ]
        wagerslt = str(random.choice(wager))
        msg = wagerslt
        await message.channel.send(msg)# tts=True)
        time.sleep (10)

    #enlighten the chat with a bible quote
    if ('bible') in messagetobot.lower():
        wager = ['Proverbs 18:10 The name of the Lord is a strong tower; the righteous run into it and are safe.', 'Psalm 34:10b Those who seek the Lord lack no good thing.', \
                 'Deuteronomy 31:8 It is the Lord who goes before you. He will be with you; he will not fail you or forsake you. Do not fear or be dismayed.', 'Psalm 34:17 When the righteous cry for help, the Lord hears, and rescues them from all their troubles.' \
                 'Isaiah 30:15 In repentance and rest is your salvation, in quietness and trust is your strength.', '2 Thessalonians 3:3 But the Lord is faithful, and he will strengthen and protect you from the evil one.',\
                 'To glorify God by being a faithful steward of all that is entrusted to us and to have a positive influence on all who come in contact with Chick-fil-A.', '“For with God nothing will be impossible” Luke 1:37.',\
                 'Philippians 4:13 I can do all things through him who strengthens me.', 'Isaiah 41:10 Fear not, for I am with you; be not dismayed, for I am your God; I will strengthen you, I will help you, I will uphold you with my righteous right hand.',\
                 'Habakkuk 3:19 God, the Lord, is my strength; he makes my feet like the deers; he makes me tread on my high places. To the choirmaster: with stringed instruments.'\
                 ]
        wagerslt = str(random.choice(wager))
        msg = wagerslt
        await message.channel.send(msg)# tts=True)
        time.sleep (10)

    #nice
    #if ('nice') in betcheck:
        #msg = 'nice'
        #await message.channel.send(msg) #tts=True)

    #Do you have a clear vision?
    if ('i see') in messagetobot.lower():
        channel = client.get_channel(137921870010777600)
        file = discord.File('./Pics/doyou.png' , filename="doyou.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://doyou.png")
        await channel.send(file = file, embed = embed)
        file = discord.File('./Pics/hedo.png' , filename="hedo.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://hedo.png")
        time.sleep(5)
        await channel.send(file = file, embed = embed)
        time.sleep(10)

    #never forget when :b: was standard
    if ('b-time') in messagetobot.lower():
        msg = 'Its :b:o time'
        frythis = 'b'
        await message.channel.send(msg)# tts=True)
        if frythis in messagetobot:
            msg = messagetobot
            msg2 = msg.replace('b',':b:')
            await message.channel.send(msg2)# tts=True)

    #roll a standard dice
    if ('roll dice') in messagetobot.lower():
        rand = random.randint(1,6)
        msg = 'Rolling...'
        await message.channel.send(msg, tts=True)
        time.sleep(2)
        msg = 'You rolled a ' + str(rand)
        await message.channel.send(msg, tts=True)
        
    #flip a standard US standard coin
    if ('flip coin') in messagetobot.lower():
        rand = random.randint(0,1)
        msg = 'Flipping...'
        await message.channel.send(msg, tts=True)
        time.sleep(2)
        
        if rand == 0:
            msg = 'Coin lands on heads'
        else:
            msg = 'Coin lands on tails'
            
        await message.channel.send(msg, tts=True)

    print("No specific phrases said, proceed to read commands")
    await client.process_commands(message)


        

    ###################################
    #End Text commands                #
    #Proceed to complex voice commands#
    ###################################

    
@client.command(pass_context=True, name = 'football', help ='The new John Madden game sounds pretty good.')
@commands.cooldown(1,10,commands.BucketType.user)
async def football(ctx):
    msg = "HI EVERYONE AND WELCOME TO JOHN MADDEN FOOTBALL!!!"
    await ctx.send(msg)
    cliplocation = './Clips/Futbol.mp3'
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'bruh', help ='For the bruh moments in our lives')
@commands.cooldown(1,10,commands.BucketType.user)
async def bruh(ctx):
    cliplocation = './Clips/bruh.mp3'
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'thomas', help ='Thomas coming through')
@commands.cooldown(1,10,commands.BucketType.user)
async def thomas(ctx):
    cliplocation = './Clips/thomas.mp3'
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'fridge', help ='Classico Flumico')
@commands.cooldown(1,10,commands.BucketType.user)
async def fridge(ctx):
    cliplocation = './Clips/oof.mp3'
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'clap', help ='clap')
@commands.cooldown(1,10,commands.BucketType.user)
async def clap(ctx):
    cliplocation = './Clips/clap.mp3'
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'chum', help ='Gnot for the weak of heart')
@commands.cooldown(1,10,commands.BucketType.user)
async def chum(ctx):
    msg = ":tired_face: You've been gnomed! :tired_face:"
    await ctx.send(msg)
    cliplocation = './Clips/gnome.mp3'
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'knock', help ='Who is it? MonkaS')
@commands.cooldown(1,10,commands.BucketType.user)
async def knock(ctx):
    cliplocation = './Clips/knock.mp3'
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'cocaine', help ='I am Impotent Rage')
@commands.cooldown(1,10,commands.BucketType.user)
async def cocaine(ctx):
    msg = "Okay Mr.Phillips"
    await ctx.send(msg)
    cliplocation = './Clips/trevor.mp3'
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'futbol', help ='A modern spin on a classic clip')
@commands.cooldown(1,10,commands.BucketType.user)
async def futbol(ctx):
    msg = "HI EVERYONE AND WELCOME TO JOHN MADDEN FOOT!"
    await ctx.send(msg)
    cliplocation = './Clips/fut.mp3'
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'gamble', help ='House always wins')
@commands.cooldown(1,10,commands.BucketType.user)
async def gamble(ctx):
    person = str(random.choice(os.listdir('./Clips/!gamble/')))
    cliplocation = './Clips/!gamble/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'spongebob', help ='You gotta lick the Marble')
@commands.cooldown(1,10,commands.BucketType.user)
async def spongebob(ctx):
    person = str(random.choice(os.listdir('./Clips/spongebob/')))
    cliplocation = './Clips/spongebob/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'alexjones', help ='Alex Jones screams about walruses')
@commands.cooldown(1,10,commands.BucketType.user)
async def alexjones(ctx):
    person = str(random.choice(os.listdir('./Clips/alexjones/')))
    cliplocation = './Clips/alexjones/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'ramsay', help ='Gordon Ramsay enlightens the chat')
@commands.cooldown(1,10,commands.BucketType.user)
async def ramsay(ctx):
    person = str(random.choice(os.listdir('./Clips/ramsay/')))
    cliplocation = './Clips/ramsay/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'bigsmoke', help ='Big Smoke gets Philisophical')
@commands.cooldown(1,10,commands.BucketType.user)
async def bigsmoke(ctx):
    person = str(random.choice(os.listdir('./Clips/bigsmoke/')))
    cliplocation = './Clips/bigsmoke/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'prequel', help ='wut')
@commands.cooldown(1,10,commands.BucketType.user)
async def bigsmoke(ctx):
    person = str(random.choice(os.listdir('./Clips/prequel/')))
    cliplocation = './Clips/prequel/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'meme', help ='The biggest collection of memes since gamble')
@commands.cooldown(1,10,commands.BucketType.user)
async def meme(ctx):
    person = str(random.choice(os.listdir('./Clips/meme/')))
    cliplocation = './Clips/meme/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'agent', help ='Agent 14 tells you what to do')
@commands.cooldown(1,10,commands.BucketType.user)
async def agent(ctx):
    person = str(random.choice(os.listdir('./Clips/agent14/')))
    cliplocation = './Clips/agent14/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'trevor', help ='Trevor...Phillips...Industries...')
@commands.cooldown(1,10,commands.BucketType.user)
async def trevor(ctx):
    person = str(random.choice(os.listdir('./Clips/trevor/')))
    cliplocation = './Clips/trevor/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'lester', help ='Because we do not hear Lester enough')
@commands.cooldown(1,10,commands.BucketType.user)
async def lester(ctx):
    person = str(random.choice(os.listdir('./Clips/lester/')))
    cliplocation = './Clips/lester/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'joke', help ='Biggest Laughs')
@commands.cooldown(1,10,commands.BucketType.user)
async def joke(ctx):
    person = str(random.choice(os.listdir('./Clips/bonzi/')))
    cliplocation = './Clips/bonzi/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'IASIP', help ='Trashman comes to eat garbage')
@commands.cooldown(1,10,commands.BucketType.user)
async def IASIP(ctx):
    person = str(random.choice(os.listdir('./Clips/IASIP/')))
    cliplocation = './Clips/IASIP/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'trump', help ='We gotta build the wall')
@commands.cooldown(1,10,commands.BucketType.user)
async def trump(ctx):
    person = str(random.choice(os.listdir('./Clips/trump/')))
    cliplocation = './Clips/trump/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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
    
@client.command(pass_context=True, name = 'got', help ='BOBBY B to our rescue')
@commands.cooldown(1,10,commands.BucketType.user)
async def got(ctx):
    person = str(random.choice(os.listdir('./Clips/got/')))
    cliplocation = './Clips/got/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'fact', help ='Bonzi knows so much')
@commands.cooldown(1,10,commands.BucketType.user)
async def fact(ctx):
    person = str(random.choice(os.listdir('./Clips/fact/')))
    cliplocation = './Clips/fact/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'wwe', help ='HULK HOGAN')
@commands.cooldown(1,10,commands.BucketType.user)
async def wwe(ctx):
    person = str(random.choice(os.listdir('./Clips/wwe/')))
    cliplocation = './Clips/wwe/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True, name = 'sports', help ='NICE ON!')
@commands.cooldown(1,10,commands.BucketType.user)
async def sports(ctx):
    person = str(random.choice(os.listdir('./Clips/sports/')))
    cliplocation = './Clips/sports/' + person
    duration = librosa.get_duration(filename=cliplocation)
    duration += 1
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

@client.command(pass_context=True)
@commands.cooldown(1,10,commands.BucketType.user)
async def surprise(ctx):
    if len(argv) > 1:
            open = True

    opener = urllib.request.build_opener()
    opener.add_headers = [("User-agent", "Mozilla/5.0")]

    chars = string.ascii_letters + string.digits

    while True:

            imgPart = ''
            for i in range(5):
                    imgPart += choice(chars)
            url = "http://i.imgur.com/" + imgPart

            try:
                    opener.open(url)
                    print(url)
                    msg = url
                    await ctx.send(url)
                    return
                    if open:
                            system("open " + url)
            except HTTPError:
                    print("found one that don't work")


@client.command(pass_context=True, name = 'stop' , help ='Ruin the fun for everyone')
@commands.cooldown(1,10,commands.BucketType.user)
async def stop(ctx):
    await ctx.voice_client.disconnect()


client.run(token)
