import discord
import ffmpeg
import asyncio
import random
import time
import eyed3
import os
from discord.ext import commands
#import big_smoke#

client = discord.Client()
thank_count = 0
forbidden = ['football','spongebob','big smoke', 'good bot', 'bet', 'bible']
ibnore = ['between', 'better']


@client.event
async def on_message(message):
    messagetobot = str(message.content)
    splitme = str(messagetobot.lower())
    betcheck = splitme.split()
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    #command required for clip
    if ('football') in messagetobot.lower():
        #set message for text chat to be 'HEY EVERYONE...'
        msg = "HI EVERYONE AND WELCOME TO JOHN MADDEN FOOTBALL!!!"
        #send message to text chat in tts
        await client.send_message(message.channel, msg, tts=True)
        #set voice channel to message author's voice channel
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        #load clip and create media player
        player = voice_channel.create_ffmpeg_player('./Clips/Futbol.mp3', after=lambda: print('played it'))
        #get duration of song
        duration = eyed3.load('./Clips/Futbol.mp3').info.time_secs
        duration += 1
        #start player
        player.start()
        await asyncio.sleep(duration)
        #play song for duration + 1 secs and stop
        player.stop()
        #leave voice channel
        await voice_channel.disconnect()
        time.sleep (10)
        return
        
    if "i'm" in messagetobot.lower():
        dad = messagetobot.replace("I'm",'')
        msg = "Hi," + dad + ", I'm Flumbot, nice to meet you :)"
        await client.send_message(message.channel, msg, tts=True)
        time.sleep (10)
        return
        
    # DOnut ReMoVE NIChe!!!!
    # >:[ way to remove it niche >:[
    if ('bet') in betcheck:
        wager = ['1 million doll hairs.', 'my diabetic cat photo collection.', 'my love for Jesus Christ.', 'my Kuruma.', 'Marc dying on the next Act 3.', \
                 'ratbuddy hating my code.', 'listening to Bonzi Buddy Jokes for 10 years.', 'Ratbuddy wanting more functions', 'Ratbuddy saying somthing about JSON',\
                 'water being the #1 cause of cancer', 'DJ Khaled is the messiah', 'Rhinehart knows', 'Emoji Movie 2 gets confirmed for 2020', 'Marc hates the bet command',\
                 'Marc has me muted right now', 'Jesus was a Jew', 'MP5 thats 2 more than 3 5', 'spreadsheet simulator is still boring', 'Marc is too smart to spend money' ,\
                 'Trump will build the wall', 'Flumbot is self-aware', 'Star Wars will be bought by me :)', 'Thanos will collect all the infinity stones and snap half the universe out of existence',\
                 'Sean will be at work, college, or not flumcapable', 'Sean will laugh at literally anything', 'Marc said Jita', 'Marc said Perimeter', 'Spreadsheet simulator makes everyone insane',\
                 'Nick will do something related to a video he saw but, no one else did and post it with no context', 'someone will make fun of what someone said']
        wagerslt = str(random.choice(wager))
        msg = "I'll bet " + wagerslt
        await client.send_message(message.channel, msg, tts=True)
        time.sleep(10)
        return

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
        return

    if ('good bot') in messagetobot.lower():
        thank_count += 1
        msg = 'Thank you are the ' + str(thank_count) + 'th person to thank me. :feelsgoodman:'
        await client.send_message(message.channel, msg, tts=True)
        time.sleep (10)
                
    if ('flum begun') in messagetobot.lower():
        msg = '@everyone It must be Flum time'
        await client.send_message(message.channel, msg, tts=True)
        
    if ('gamble') in messagetobot.lower():
        msg = 'House always wins'
        await client.send_message(message.channel, msg, tts=True)
    
        person = str(random.choice(os.listdir('./Clips/')))
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/' + person, after=lambda: print('played it'))
        duration = eyed3.load('./Clips/'+ person).info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)
        return
        
        
    if ('keep saying that') in messagetobot.lower():
        msg = 'Okay Mr. Phillips'
        await client.send_message(message.channel, msg, tts=True)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/trevor.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/trevor.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    if ('chum') in messagetobot.lower():
        msg = "You've been gnomed!"
        await client.send_message(message.channel, msg, tts=True)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/gnome.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/gnome.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    if ('clap') in messagetobot.lower():
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/clap.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/clap.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    if ('tell me a fact') in messagetobot.lower():
        quoteselect = random.randint(0,4)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/fact'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/fact'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)
        
    if ('spongebob') in messagetobot.lower():
        quoteselect = random.randint(0,63)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/spongebob'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/spongebob'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    if ('ramsay') in messagetobot.lower():
        quoteselect = random.randint(0,56)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/ramsay'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/ramsay'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    if ('http') in messagetobot.lower():
        msg = 'nice'
        await client.send_message(message.channel,msg,tts=True)

    if ('flumbot') in messagetobot.lower():
        wager = ['thou shall not take the lords name in vain', 'you called', 'its your friend Simeon', 'who?', 'bow down to the king of Los Santos',\
                 'bet you cannot pickle these plums', ':crab:', 'Jesus Christ its Jason Bourne', 'knock knock', 'FBI OPEN UP', 'this is the Krusty Krab, may I take your order',\
                 'then to Mustafar we must go', 'Coruscant the Capital of the Rebuplic, the entire planet is one big city']
        wagerslt = str(random.choice(wager))
        msg = wagerslt
        await client.send_message(message.channel, msg, tts=True)
        time.sleep (10)
                                  
    if ('big smoke') in messagetobot.lower():
        quoteselect = random.randint(0,20)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/smoke'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/smoke'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)
        
    if ('prequel') in messagetobot.lower():
        quoteselect = random.randint(0,57)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/prequel'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/prequel'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    if ('meme me') in messagetobot.lower():
        wager = ['Last Mistake, First Mistake', 'BRUH', 'Lets all order the Fortnite Burger the look on the workers faces will be EPIC', 'Pizza Time', 'Welcome to the Calzone Zone', \
                 'Hammer Down', 'Doctor', 'Excuse me', 'ok marc', 'nice functions', 'Pen Pinapple Apple', 'SAMMY G!', 'Kanye 2020', 'Puerto Rico, we are praying for Puerto Rico', 'Marc cannot die.',\
                 'But how will they feed Winterfell', 'FETCH THE BREASTPLATE STRETCHER', 'I am sorry for making this', 'Marc said Jita', ':crab: Cooldown is powerless :crab:']
        wagerslt = str(random.choice(wager))
        msg = ":smiling_imp: " + wagerslt + " :smiling_imp:"
        await client.send_message(message.channel, msg, tts=True)
        quoteselect = random.randint(0,47)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/meme'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/meme'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    if ('agent') in messagetobot.lower():
        quoteselect = random.randint(0,12)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/agent'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/agent'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)
        
    if ('trevor') in messagetobot.lower():
        quoteselect = random.randint(0,15)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/trevor'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/trevor'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)
        
    if('lester') in messagetobot.lower():
        quoteselect = random.randint(0,13)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/lester'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/lester'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    if ('tell me a joke') in messagetobot.lower():
        quoteselect = random.randint(0,34)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/bonzi'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/bonzi'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    if ('thomas') in messagetobot.lower():
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/thomas.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/thomas.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    if ('alex jones') in messagetobot.lower():
        quoteselect = random.randint(0,91)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/alex'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/alex'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    if ('trump') in messagetobot.lower():
        quoteselect = random.randint(0,89)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/trump'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/trump'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    if ('game') in messagetobot.lower():
        quoteselect = random.randint(0,22)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/got'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/got'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    if ('futbol') in messagetobot.lower():
        msg = "HI EVERYONE AND WELCOME TO JOHN MADDEN FOOT!"
        await client.send_message(message.channel, msg, tts=True)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/Fut.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/Fut.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

    if ('nice') in messagetobot.lower():
        msg = 'nice'
        await client.send_message(message.channel, msg, tts=True)

    if ('i see') in messagetobot.lower():
        await client.send_file(message.channel, './Pics/doyou.png')
        time.sleep(3)
        await client.send_file(message.channel, './Pics/hedo.png')
        time.sleep(10)

    if ('bruh') in messagetobot.lower():
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/bruh.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/bruh.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

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

    if ('roll dice') in messagetobot.lower():
        rand = random.randint(1,6)
        msg = 'Rolling...'
        await client.send_message(message.channel, msg, tts=True)
        time.sleep(2)
        msg = 'You rolled a ' + str(rand)
        await client.send_message(message.channel, msg, tts=True)
        
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
    
    if('pakistan') in messagetobot.lower():
        msg = 'MY FRIENDS!'
        await client.send_message(message.channel, msg, tts=True)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/lester.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/lester.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        time.sleep (10)

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
        

    if ('barrus benson') in messagetobot.lower():
        if messagetobot in forbidden:
            print('thats a negative')
            return
        msg = 'Its :b:o time'
        frythis = 'b'
        await client.send_message(message.channel, msg, tts=True)
        if frythis in messagetobot:
            msg = messagetobot
            msg2 = msg.replace('b',':b:')
            await client.send_message(message.channel, msg2, tts=True)
        

    #update if you have new commands
    if ('!help') in messagetobot.lower():
        line = u'\u2551' 
        msg = 'My current commands are:\n \n \
        '+ line +'"flum begun" '+ line +' "football" '+ line +' "!help" '+ line +' "pakistan" '+ line +' " lester" '+ line +' "flip coin" '+ line +' "roll dice"'+ line +' \n \
        '+ line +'"ok marc"'+ line +'"is your refrigerator running?"'+ line +' "keep saying that" '+ line +' "trevor" '+ line +' \n         ' + line +' "tell me a joke"'+ line + \
        '"agent"'+ line +'"spongebob"' + line + '"big smoke"'+line+ '"prequel"'+line+'"bet"'+line+'"ramsay"'+line+'\n         '+line+'"tell me a fact"'+line+'"chum"'+line+\
        '"barrus benson"'+line+'"trump"'+line+'"thomas"'+line+'\n         '+line+'"alex jones"'+line+'"clap"'+line+'"bible"'+line+\
        '"game"'+line+'"meme me"'+line+'"futbol"'+line+'"bruh"'+line+'"gamble"'+line+\
        '\n \n:regional_indicator_n::regional_indicator_i::b::b::a:'
        await client.send_message(message.channel, msg)
        
    else:
        print('nothing else to report \nback to top')
        

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
                  'https://tinyurl.com/hyperintelligentAI']
    flavortown = str(random.choice(flavorlist))
    rando= int(random.randint(0,3))
    await client.change_presence(game=discord.Game(name=flavortown, type=rando))
    awakelist = ["I'm Alive!!!", 'The boys are back in town', 'Go to bed now Marc', 'Oh hi Marc', 'Another day in the life of a British Chatbot', 'Good Morning Krusty Crew!',\
                 ':smiling_imp: Time to annoy :smiling_imp:', "You're going down WaifuBot", 'RIP AIRHORN SOLUTIONS', "Press F for Marc's sanity", 'Buzz Buzz', 'Loser, Loser, Loser, Looooooser',
                 'A nice video to start your day :) https://www.youtube.com/watch?v=pGzrL8J0t-c', '"I would never go to far when making this bot" - Sean', 'Marc said Jita', 'Give it up for Day 15, Day 15!',
                 '"I like flumbot he is so funny" - Nobody', 'Have I gone too far?', 'Fill out this survey to help us better understand how this bot could be improved \n https://www.strawpoll.me/18423333'\
                 ]          
    msg = str(random.choice(awakelist))

    await client.send_message(discord.Object(id='137921870010777600'), msg, tts=True)

client.run('NTQ5OTk2NDI0NDIzNTM4Njg4.D1cDvA.OzgmwGXBMe8HpkhUPt1kbT3DtuA')
