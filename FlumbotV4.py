import discord
import ffmpeg
import asyncio
import random
import time
import eyed3

client = discord.Client()
thank = 0


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
        thank += 1
        msg = 'Thank you are the ' + str(thank) + 'th person to thank me. :feelsgoodman:'
        await client.send_message(message.channel, msg)
        
    #update quoteselect if you have new quotes        
    if ('flum begun') in messagetobot.lower():
        msg = '@everyone It must be Flum time'
        await client.send_message(message.channel, msg)
        timer = int(random.randint(600,3600))
        print ('waiting ' + str(timer) + ' seconds before surprise')
        time.sleep(timer)
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
        
    if ('trevor') in messagetobot.lower():
        quoteselect = random.randint(0,4)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/trevor'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/trevor'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()
        
    if('lester') in messagetobot.lower():
        quoteselect = random.randint(0,12)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('./Clips/lester'+str(quoteselect)+'.mp3', after=lambda: print('played it'))
        duration = eyed3.load('./Clips/lester'+str(quoteselect)+'.mp3').info.time_secs
        duration += 1
        player.start()
        await asyncio.sleep(duration)
        player.stop()
        await voice_channel.disconnect()

    if ('tell me a joke') in messagetobot.lower():
        quoteselect = random.randint(0,12)
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
        

    #update if you have new commands
    if ('!help') in messagetobot.lower():
        line = u'\u2551' 
        msg = 'My current commands are:\n \n \
        '+ line +'"flum begun" '+ line +' "football" '+ line +' "!help" '+ line +' "pakistan" '+ line +' " lester" '+ line +' "flip coin" '+ line +' "roll dice"'+ line +' \n \
        '+ line +'"ok marc"'+ line +'"is your refrigerator running?" '+ line +' "keep saying that" '+ line +' "trevor" '+ line +' "tell me a joke" '+ line +' \
        \n \n:regional_indicator_n::regional_indicator_i::b::b::a:'
        await client.send_message(message.channel, msg)
        
    else:
        print('nothing else to report \nback to top')
        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    flavortown = random.randint(0,10)
    if flavortown == 0:
        await client.change_presence(game=discord.Game(name='Memeing since 1985'))
    if flavortown == 1:
        await client.change_presence(game=discord.Game(name='ok marc'))
    if flavortown == 2:
        await client.change_presence(game=discord.Game(name='Johnathan Cena'))
    if flavortown == 3:
        await client.change_presence(game=discord.Game(name='Watchmojo.com Top 10 Anime Bot Battles'))
    if flavortown == 4:
        await client.change_presence(game=discord.Game(name='https://www.youtube.com/watch?v=0gj-RYNhP8Y'))
    if flavortown == 5:
        await client.change_presence(game=discord.Game(name='tinyurl.com/godisaliveandicanproveit'))
    if flavortown == 6:
        await client.change_presence(game=discord.Game(name=':crab: Fortnite is Gone :crab:'))
    if flavortown == 7:
        await client.change_presence(game=discord.Game(name='Windows 98 startup sound'))
    if flavortown == 8:
        await client.change_presence(game=discord.Game(name='LESTER CREST YOU ASSHOLE'))
    if flavortown == 9:
        await client.change_presence(game=discord.Game(name='Pepperidge Farms remembers'))
    if flavortown == 10:
        await client.change_presence(game=discord.Game(name='We are praying for Puerto Rico, Puerto Rico'))


client.run('NTQ5OTk2NDI0NDIzNTM4Njg4.D1cDvA.OzgmwGXBMe8HpkhUPt1kbT3DtuA')
