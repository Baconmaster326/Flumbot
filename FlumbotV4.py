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
        #create reply back with 'ok marc'
        msg = 'HI EVERYONE AND WELCOME TO JOHN MADDEN FOOTBALL!!!'.format(message)
        #send msg and await result
        await client.send_message(message.channel, msg)
        #set voice channel to join (the message senders voice channel)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        #create a ffmpeg player to play 'Futbol.mp3' after creating, print played it in console
        player = voice_channel.create_ffmpeg_player('./Clips/Futbol.mp3', after=lambda: print('played it'))
        #start music in voice channel
        player.start()
        while not player.is_done():
            #timer before leaving (duration of clip)
            await asyncio.sleep(13)
            #stop player after leaving
            player.stop()
            #leave voice channel
            await voice_channel.disconnect()

    if ('bet') in messagetobot.lower():
        wager = ['1 million doll hairs.', 'my diabetic cat photo collection.', 'my love for Jesus Christ.', 'my Kuruma.', 'Marc dying on the next Act 3.', \
                 'Ratbuddy hating my code.', 'listening to Bonzi Buddy Jokes for 10 years.']
        wagerslt = random.randint(0,7)
        msg = "I'll wager " +str(wager[wagerslt])
        await client.send_message(message.channel, msg)

    if ('is your refrigerator running') in messagetobot.lower():
        msg = 'Yes'
        await client.send_message(message.channel, msg)
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
        await client.send_message(message.channel, msg)
        
    #update quoteselect if you have new quotes        
    if ('flum begun') in messagetobot.lower():
        msg = '@everyone It must be Flum time'
        await client.send_message(message.channel, msg)
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
        await client.send_message(message.channel, msg)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/trevor.mp3', after=lambda: print('played it'))
        player.start()
        await asyncio.sleep(124)
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
        quoteselect = random.randint(0,0)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/spongebob'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/spongebob'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()

    if ('ramsay') in messagetobot.lower():
        quoteselect = random.randint(0,50)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/ramsay'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/ramsay'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        
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
        
    if ('ok marc') in messagetobot.lower():
        msg = 'ok marc'
        await client.send_message(message.channel,msg)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/ok.mp3', after=lambda: print('played it'))
        player.start()
        await asyncio.sleep(1)
        player.stop()
        await voice_channel.disconnect()

    if ('roll dice') in messagetobot.lower():
        rand = random.randint(1,6)
        msg = 'Rolling...'
        await client.send_message(message.channel, msg)
        time.sleep(2)
        msg = 'You rolled a ' + str(rand)
        await client.send_message(message.channel, msg)
        
    if ('flip coin') in messagetobot.lower():
        rand = random.randint(0,1)
        msg = 'Flipping...'
        await client.send_message(message.channel, msg)
        time.sleep(2)
        
        if rand == 0:
            msg = 'Coin lands on heads'
        else:
            msg = 'Coin lands on tails'
            
        await client.send_message(message.channel, msg)
    
    if('pakistan') in messagetobot.lower():
        msg = 'MY FRIENDS!'
        await client.send_message(message.channel, msg)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/lester.mp3', after=lambda: print('played it'))
        player.start()
        await asyncio.sleep(122)
        player.stop()
        await voice_channel.disconnect()

    if ('b') in messagetobot.lower():
        if messagetobot in forbidden:
            print('thats a negative')
            return
        msg = 'Its :b:o time'
        frythis = 'b'
        await client.send_message(message.channel, msg)
        if frythis in messagetobot:
            msg = messagetobot
            msg2 = msg.replace('b',':b:') + '\n yeet'
            await client.send_message(message.channel, msg2)
        

    #update if you have new commands
    if ('!help') in messagetobot.lower():
        line = u'\u2551' 
        msg = 'My current commands are:\n \n \
        '+ line +'"flum begun" '+ line +' "football" '+ line +' "!help" '+ line +' "pakistan" '+ line +' " lester" '+ line +' "flip coin" '+ line +' "roll dice"'+ line +' \n \
        '+ line +'"ok marc"'+ line +'"is your refrigerator running?"'+ line +' "keep saying that" '+ line +' "trevor" '+ line +' \n         ' + line +' "tell me a joke"'+ line + \
        '"agent"'+ line +'"spongebob"' + line + '"big smoke"'+line+ '"prequel"'+line+'"bet"'+line+'"ramsay"'+line+'\n         '+line+'"tell me a fact"'+line+\
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
                  'Pepperidge Farms remembers', 'We are praying for Puerto Rico, Puerto Rico']
    flavortown = random.randint(0,10)
    rando= int(random.randint(0,3))
    await client.change_presence(game=discord.Game(name=flavorlist[flavortown], type=rando))

client.run('NTQ5OTk2NDI0NDIzNTM4Njg4.D1cDvA.OzgmwGXBMe8HpkhUPt1kbT3DtuA')
