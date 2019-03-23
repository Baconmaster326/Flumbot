import discord
import ffmpeg
import asyncio
import random
import time
import eyed3
#import big_smoke#

client = discord.Client()
thank = 0
forbidden = ['football','spongebob','big smoke', 'good bot', 'bet']

@client.event
async def on_message(message):
    messagetobot = str(message.content)
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

    if ('bet') in messagetobot.lower():
        wager = ['1 million doll hairs.', 'my diabetic cat photo collection.', 'my love for Jesus Christ.', 'my Kuruma.', 'Marc dying on the next Act 3.', \
                 'ratbuddy hating my code.', 'listening to Bonzi Buddy Jokes for 10 years.', 'Ratbuddy wanting more functions', 'Ratbuddy saying somthing about JSON',\
                 'water being the #1 cause of cancer', 'DJ Khaled is the messiah', 'Rhinehart knows', 'Emoji Movie 2 gets confirmed for 2020']
        wagerslt = str(random.choice(wager))
        msg = "I'll bet " + wagerslt
        await client.send_message(message.channel, msg, tts=True)

    if ('is your refrigerator running') in messagetobot.lower():
        msg = 'Yes'
        await client.send_message(message.channel, msg, tts=True)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/oof.mp3', after=lambda: print('played it'))
        player.start()
        await asyncio.sleep(15)
        player.stop()
        await voice_channel.disconnect()

    if ('good bot') in messagetobot.lower():
        thank = 0
        thanker = thank + 1
        thank += 1
        msg = 'Thank you are the ' + str(thanker) + 'th person to thank me. :feelsgoodman:'
        await client.send_message(message.channel, msg, tts=True)
        
    #update quoteselect if you have new quotes        
    if ('flum begun') in messagetobot.lower():
        msg = '@everyone It must be Flum time'
        await client.send_message(message.channel, msg, tts=True)
        timer = int(random.randint(600,3600))
        print ('waiting ' + str(timer) + ' seconds before surprise')
        asyncio.sleep(timer)
        surprise = int(timer % 2)
        
        if  surprise == 0:
            quoteselect = random.randint(0,4)
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('./Clips/trevor'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
            duration = eyed3.load('./Clips/trevor'+str(quoteselect)+'.mp3').info.time_secs
            duration += 1
            player.start()
            await asyncio.sleep(duration)
            player.stop()
            await voice_channel.disconnect()
            
        else:
            quoteselect = random.randint(0,12)
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('./Clips/lester'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
            duration = eyed3.load('./Clips/lester'+str(quoteselect)+'.mp3').info.time_secs
            duration += 1
            player.start()
            await asyncio.sleep(duration)
            player.stop()
            await voice_channel.disconnect()
        
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

    if ('clap') in messagetobot.lower():
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/clap.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/clap.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()

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
        
    if ('spongebob') in messagetobot.lower():
        quoteselect = random.randint(0,25)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/spongebob'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/spongebob'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()

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
                                  
    if ('big smoke') in messagetobot.lower():
        quoteselect = random.randint(0,3)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/smoke'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/smoke'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        
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

    if ('thomas') in messagetobot.lower():
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/thomas.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/thomas.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()

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

    if ('trump') in messagetobot.lower():
        quoteselect = random.randint(0,0)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/trump'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/trump'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        
    if ('ok marc') in messagetobot.lower():
        msg = 'ok marc'
        await client.send_message(message.channel,msg,tts=True)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/ok.mp3', after=lambda: print('played it'))
        player.start()
        await asyncio.sleep(1)
        player.stop()
        await voice_channel.disconnect()

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
        '"barrus benson"'+line+'"trump"'+line+'"thomas"'+line+'"alex jones"'+line+'"clap"'+line+\
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
                  'Pepperidge Farms remembers', 'We are praying for Puerto Rico, Puerto Rico', 'Shaq has The General Insurance', 'Kanye 2020', 'Marco Polo','Jesus Christ'\
                  'Chidlers guitar ;)', 'SmartShart', 'Belgium, which is basically a non-country', 'Buying a car today', 'High wuality midis']
    flavortown = str(random.choice(flavorlist))
    rando= int(random.randint(0,3))
    await client.change_presence(game=discord.Game(name=flavortown, type=rando))

client.run('NTQ5OTk2NDI0NDIzNTM4Njg4.D1cDvA.OzgmwGXBMe8HpkhUPt1kbT3DtuA')
