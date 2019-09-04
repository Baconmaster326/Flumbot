import discord
import ffmpeg
import asyncio
import random
import time
import eyed3
import os
import pickle
from discord.ext import commands
#import big_smoke#
#import mad marc#

token = 'NTQ5OTk2NDI0NDIzNTM4Njg4.XUcYeQ.GMk9ZPQ3Hmw6Ze-cJU9bUnDy2MA'
client = commands.Bot(command_prefix = '', case_insensitive = True, )

#load variables from previous bot run
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
    #Set flavortown text
    flavorlist = ['Memeing since 1985', 'ok marc', 'Johnathan Cena', 'Watchmojo.com Top 10 Anime Bot Battles', 'https://www.youtube.com/watch?v=0gj-RYNhP8Y', \
                  'tinyurl.com/godisaliveandicanproveit', ':crab: Fortnite is Gone :crab:' , 'Windows 98 startup sound', 'LESTER CREST YOU ASSHOLE', \
                  'Pepperidge Farms remembers', 'We are praying for Puerto Rico, Puerto Rico', 'Shaq has The General Insurance', 'Kanye 2020', 'Marco Polo','Jesus Christ',\
                  'Chidlers guitar ;)', 'SmartShart', 'Belgium, which is basically a non-country', 'Buying a car today', 'High wuality midis', 'Spreadsheet simulator', 'Onion Knight',\
                  'Game of Thrones Season 8', 'HentaiHaven.org', 'http://nooooooooooooooo.com', 'dad', 'Slapchat' , 'https://tinyurl.com/Godisheretoday' ,'https://tinyurl.com/goodideasinhumanhistory (NSFW)',\
                  'https://tinyurl.com/hyperintelligentAI', 'marc cannot mute this']
    flavortown = str(random.choice(flavorlist))
    rando= int(random.randint(0,3))
    await client.change_presence(game=discord.Game(name=flavortown, type=rando))
    #Set greeting for marc so he doesn't feel so lonely during his Austrailia time
    awakelist = ["I'm Alive!!!", 'The boys are back in town', 'Go to bed now Marc', 'Oh hi Marc', 'Another day in the life of a British Chatbot', 'Good Morning Krusty Crew!',\
                 ':smiling_imp: Time to annoy :smiling_imp:', "You're going down WaifuBot", 'RIP AIRHORN SOLUTIONS', "Press F for Marc's sanity", 'Buzz Buzz', 'Loser, Loser, Loser, Looooooser',
                 'A nice video to start your day :) https://www.youtube.com/watch?v=pGzrL8J0t-c', '"I would never go to far when making this bot" - Sean', 'Marc said Jita', 'Give it up for Day 15, Day 15!',
                 '"I like flumbot he is so funny" - Nobody', 'Have I gone too far?', 'Fill out this survey to help us better understand how this bot could be improved \n https://www.strawpoll.me/18423333','Guess who',
                 'Marc has me muted :(','Riot','*naruto run*','OwO wuts twis', 'Uwu awake from a long slumber', 'Good morning Donald Trump, United States President number 44', 'Shoutouts to SimpleFlips',
                 'Throwback to LOLwut Pear','Checkout my obby course https://tinyurl.com/niceoneniche', 'This one is for the boys https://www.youtube.com/watch?v=26nnZSjtSqg', 'God was here','this makes marc mad', 'nice one marc'\
                 'shoutout to marc','marc turn on text commands','take these functions rat','bout to throw hands']          
    msg = str(random.choice(awakelist))

    await client.send_message(discord.Object(id='137921870010777600'), msg, tts=True)
    

@client.event
#The following commands work regardless of where there are or how many conditions you set, please note some commands are legacy and should not be copied
#Copy commands at your own risk
#For commands relying on more than one word, do not use 'in betcheck', that is to prevent it from thinking better is 'bet' command, 'betcheck' should be used for all single word commands.BadArgument
async def on_message(message):
    global thank
    #create case insensitive conditions
    messagetobot = str(message.content)
    #seperate all the words for easy parsing
    splitme = str(messagetobot.lower())
    betcheck = splitme.split()
    
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    #dad-joke iniator boo-hoo marc got mega sad, re enable at some point
    #if "i'm" in betcheck:
        #dad = messagetobot.replace("I'm",'')
        #msg = "Hi," + dad + ", I'm Flumbot, nice to meet you :)"
        #await client.send_message(message.channel, msg, tts=True)
        #time.sleep (10)
        
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
        await client.send_message(message.channel, msg, tts=True)
        time.sleep(10)

    #thank flumbot for all the hard work he does (now persistent after resets PogChamp)
    if ('good bot') in messagetobot.lower():
        #get thank counter
        #increment by 1
        thank += 1
        #create and send message
        msg = 'Thank :clap: you :clap: are :clap: the :clap:' + str(thank) + 'th :clap: person :clap: to :clap: thank :clap: me. :clap:'
        await client.send_message(message.channel, msg, tts=True)
        #save and dump the new thank counter
        thankout = open("thank.pickle", "wb")
        #lol pickle.dump
        pickle.dump(thank, thankout)
        thankout.close()
        time.sleep (10)

    if ('bad bot') in messagetobot.lower():
        #increment by 1
        thank -= 1
        #create and send message
        msg = ':rage: You :rage: brought :rage: my :rage: thanks :rage: to :rage' + str(thank) + ':rage: hope :rage: you :rage: feel :rage: good :rage:'
        await client.send_message(message.channel, msg, tts=True)
        #save and dump the new thank counter
        thankout = open("thank.pickle", "wb")
        #lol pickle.dump
        pickle.dump(thank, thankout)
        thankout.close()
        time.sleep (10)

    #classic flum
    if ('is your refrigerator running') in messagetobot.lower():
        msg = 'Yes'
        await client.send_message(message.channel, msg, tts=True)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/oof.mp3', after=lambda: print('played it'))
        player.start()
        await asyncio.sleep(15)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    #F's in chat for those we lost in the Area 51 raids
    if ('f') in betcheck:
        msg = 'F'
        await client.send_message(message.channel, msg, tts=True)

    #alert chat of incoming flum
    if ('flum begun') in messagetobot.lower():
        msg = '@everyone It must be Flum time'
        await client.send_message(message.channel, msg, tts=True)

    #nice way to tell if someone has posted a link in chat, also, nice.
    if ('http') in messagetobot.lower():
        msg = 'nice'
        await client.send_message(message.channel,msg,tts=True)

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
        await client.send_message(message.channel, msg, tts=True)
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
        await client.send_message(message.channel, msg, tts=True)
        time.sleep (10)

    #nice
    if ('nice') in betcheck:
        msg = 'nice'
        await client.send_message(message.channel, msg, tts=True)

    #Do you have a clear vision?
    if ('i see') in messagetobot.lower():
        await client.send_file(message.channel, './Pics/doyou.png')
        time.sleep(3)
        await client.send_file(message.channel, './Pics/hedo.png')
        time.sleep(10)

    #never forget when :b: was standard
    if ('b-time') in messagetobot.lower():
        msg = 'Its :b:o time'
        frythis = 'b'
        await client.send_message(message.channel, msg, tts=True)
        if frythis in messagetobot:
            msg = messagetobot
            msg2 = msg.replace('b',':b:')
            await client.send_message(message.channel, msg2, tts=True)

    #roll a standard dice
    if ('roll dice') in messagetobot.lower():
        rand = random.randint(1,6)
        msg = 'Rolling...'
        await client.send_message(message.channel, msg, tts=True)
        time.sleep(2)
        msg = 'You rolled a ' + str(rand)
        await client.send_message(message.channel, msg, tts=True)
        
    #flip a standard US standard coin
    if ('flip coin') in messagetobot.lower():
        rand = random.randint(0,1)
        msg = 'Flipping...'
        await client.send_message(message.channel, msg, tts=True)
        time.sleep(2)
        
        if rand == 0:
            msg = 'Coin lands on heads'
        else:
            msg = 'Coin lands on tails'
            
        await client.send_message(message.channel, msg, tts=True)


        

    ###################################
    #End Text commands                #
    #Proceed to complex voice commands#
    ###################################



        

    if ('ok marc') in messagetobot.lower():
        msg = 'ok marc'
        await client.send_message(message.channel,msg,tts=True)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/ok.mp3', after=lambda: print('played it'))
        player.start()
        await asyncio.sleep(1)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

        
    else:
        print('proceed to read commands')
        
    await client.process_commands(message)

    

#if anyone deletes a message do this I'll have no hidden messages from me
@client.event
async def on_message_delete(message):
    author = str(message.author)
    content = str(message.content)
    channel = message.channel
    message = 'Ladies and gentlemen, ' + '@' + author + " said, " + \
               content + ", which they promptly deleted. Making them tonight's biggest loser"
    await client.send_message(channel,message)

    

#WARNING these can only parse 1 word phrases at the begining of a discord message. Subject to change.
@client.command(pass_context=True)
async def football(ctx):
        #set message to be sent to discord chat
        msg = "HI EVERYONE AND WELCOME TO JOHN MADDEN FOOTBALL!!!"
        #send message to chat, TTS on
        await client.say(msg, tts=True)
        #set channel to join as author's channel
        channel = ctx.message.author.voice.voice_channel
        await client.join_voice_channel(channel)
        #create variables
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        #create player
        player = voice_client.create_ffmpeg_player('./Clips/Futbol.mp3', after=lambda: print('played it'))
        #get duration of song
        duration = eyed3.load('./Clips/Futbol.mp3').info.time_secs
        duration += 1
        #start player
        player.start()
        #wait x secs before auto leaving
        await asyncio.sleep(duration)
        #play song for duration + 1 secs and stop
        player.stop()
        #leave voice channel
        await voice_client.disconnect()
        time.sleep(10)
        return
    
#command forces flumbot to disconnect   
@client.command(pass_context=True)
async def stop(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

#plays bruh sound effect 2
@client.command(pass_context=True)
async def bruh(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/bruh.mp3', after=lambda: print('played it'))
    duration = eyed3.load('./Clips/bruh.mp3').info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#plays thomas the thank engine
@client.command(pass_context=True)
async def thomas(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/thomas.mp3', after=lambda: print('played it'))
    duration = eyed3.load('./Clips/thomas.mp3').info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#plays bonzi buddy clap
@client.command(pass_context=True)
async def clap(ctx):
    discord.ext.commands.cooldown(1,10, commands.BucketType.user)
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/clap.mp3', after=lambda: print('played it'))
    duration = eyed3.load('./Clips/clap.mp3').info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#plays gnomed
@client.command(pass_context=True)
async def chum(ctx):
    msg = ":tired_face: You've been gnomed! :tired_face:"
    await client.say(msg, tts=True)
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/gnome.mp3', after=lambda: print('played it'))
    duration = eyed3.load('./Clips/gnome.mp3').info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#spook your friends
@client.command(pass_context=True)
async def knock(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/knock.mp3', after=lambda: print('played it'))
    duration = eyed3.load('./Clips/knock.mp3').info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#plays entire Series A ending
@client.command(pass_context=True)
async def cocaine(ctx):
    msg = "Okay Mr.Phillips"
    await client.say(msg, tts=True)
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/trevor.mp3', after=lambda: print('played it'))
    duration = eyed3.load('./Clips/trevor.mp3').info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#plays foot
@client.command(pass_context=True)
async def futbol(ctx):
    msg = "HI EVERYONE AND WELCOME TO JOHN MADDEN FOOT!"
    await client.say(msg, tts=True)
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/fut.mp3', after=lambda: print('played it'))
    duration = eyed3.load('./Clips/fut.mp3').info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#Plays a random clip !!!BEFORE UPDATING QUOTES MAKE SURE YOU COPY MP3 FILES INTO !GAMBLE!!!
@client.command(pass_context=True)
async def gamble(ctx):
    msg = 'House always wins'
    await client.say(msg, tts=True)
    person = str(random.choice(os.listdir('./Clips/!gamble/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/!gamble/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/!gamble/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#Plays random quote from spongebob
@client.command(pass_context=True)
async def spongebob(ctx):
    person = str(random.choice(os.listdir('./Clips/spongebob/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/spongebob/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/spongebob/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#Plays random quote from Gordon Ramsay
@client.command(pass_context=True)
async def ramsay(ctx):
    person = str(random.choice(os.listdir('./Clips/ramsay/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/ramsay/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/ramsay/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#BIG SMOKE QUOTES
@client.command(pass_context=True)
async def bigsmoke(ctx):
    person = str(random.choice(os.listdir('./Clips/bigsmoke/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/bigsmoke/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/bigsmoke/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#Prequel QUOTES
@client.command(pass_context=True)
async def prequel(ctx):
    person = str(random.choice(os.listdir('./Clips/prequel/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/prequel/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/prequel/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#MEEMEE
@client.command(pass_context=True)
async def meme(ctx):
    person = str(random.choice(os.listdir('./Clips/meme/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/meme/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/meme/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#Agent 14 WHAT ARE THESE CLOWNS DOING HERE
@client.command(pass_context=True)
async def agent(ctx):
    person = str(random.choice(os.listdir('./Clips/agent14/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/agent14/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/agent14/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#TREVAHHH
@client.command(pass_context=True)
async def trevor(ctx):
    person = str(random.choice(os.listdir('./Clips/trevor/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/trevor/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/trevor/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#LESTER CREST YOU AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
@client.command(pass_context=True)
async def lester(ctx):
    person = str(random.choice(os.listdir('./Clips/lester/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/lester/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/lester/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#Bonzi ASMR
@client.command(pass_context=True)
async def joke(ctx):
    person = str(random.choice(os.listdir('./Clips/bonzi/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/bonzi/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/bonzi/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#THESE ARE PEOPLE, THESE ARE PEOPLE 
@client.command(pass_context=True)
async def alexjones(ctx):
    person = str(random.choice(os.listdir('./Clips/alexjones/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/alexjones/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/alexjones/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#We gotta build the wall
@client.command(pass_context=True)
async def trump(ctx):
    person = str(random.choice(os.listdir('./Clips/trump/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/trump/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/trump/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#FETCH THE BREASTPLATE STRECTCHER
@client.command(pass_context=True)
async def got(ctx):
    person = str(random.choice(os.listdir('./Clips/got/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/got/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/got/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

@client.command(pass_context=True)
async def fact(ctx):
    person = str(random.choice(os.listdir('./Clips/fact/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/fact/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/fact/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#Hulk Hogan here for HULKAMANIA 
@client.command(pass_context=True)
async def wwe(ctx):
    person = str(random.choice(os.listdir('./Clips/wwe/')))
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = voice_client.create_ffmpeg_player('./Clips/wwe/' + person, after=lambda: print('played it'))
    duration = eyed3.load('./Clips/wwe/' + person).info.time_secs
    duration += 1
    player.start()
    await asyncio.sleep(duration)
    player.stop()
    await voice_client.disconnect()
    time.sleep(10)
    return

#help command (who cares about formatting)
@client.command(pass_context=True)
async def helping(ctx):
    line = u'\u2551'
    msg = 'My current commands are: \n \n \
    ' + line + '"flum begun"' + line + '"football"' + line + '"help"' + line + '"gamble"' + line +\
    '"lester"' + line + '"flip coin"' + line + '"roll dice"' + line + '"ok marc"' + line + '"cocaine"' + line +'\n'+ line +\
    '"is your refrigerator running?"' + line + '"trevor"' + line + '"joke"' + line + '"bigsmoke"' + line +\
    '"fact"' + line + '"chum"' + line + '"alexjones"' + line + '"spongebob"' + line + '"trump"' + line + '"bible"'+ line +\
    '"clap"' + line + '"bruh"' + line + '"futbol"' + line + '"meme"' + line + '"got"' + line + '"thomas"' + line +\
    '"agent"' + line + '"good bot"' + line + '"bet"' + line + \
    '"\n \n I am always watching stay :regional_indicator_w: :regional_indicator_o: :regional_indicator_k: :regional_indicator_e: :eye:'
    
    await client.say(msg, tts=True)
    time.sleep(10)
    return

#@client.command(pass_context=True)
#async def "I'm"(ctx):
    #msg = 'House always wins'
    #author = str(message.author)
    #content = str(message.content)
    #channel = message.channel
    #await client.say(msg, tts=True)
    #person = str(random.choice(os.listdir('./Clips/!gamble/')))

    return

client.run(token)
