import discord
import ffmpeg
import asyncio
import random
import time

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
        player = voice_channel.create_ffmpeg_player('oof.mp3', after=lambda: print('played it'))
        player.start()
        await asyncio.sleep(15)
        player.stop()
        await voice_channel.disconnect()

    if ('good bot') in messagetobot.lower():
        thank += 1
        msg = 'Thank you are the ' + str(thank) + 'th person to thank me. :feelsgoodman:'
        await client.send_message(message.channel, msg)
        
            
    if ('flum begun') in messagetobot.lower():
        msg = '@everyone It must be Flum time'
        await client.send_message(message.channel, msg)
        
    if('lester') in messagetobot.lower():
        quoteselect = random.randint(0,12)
        
        if quoteselect == 0:
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('lester0.mp3', after=lambda: print('played it'))
            player.start()
            await asyncio.sleep(9)
            player.stop()
            await voice_channel.disconnect()
        if quoteselect == 1:
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('lester1.mp3', after=lambda: print('played it'))
            player.start()
            await asyncio.sleep(6)
            player.stop()
            await voice_channel.disconnect()
        if quoteselect == 2:
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('lester2.mp3', after=lambda: print('played it'))
            player.start()
            await asyncio.sleep(5)
            player.stop()
            await voice_channel.disconnect()
        if quoteselect == 3:
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('lester3.mp3', after=lambda: print('played it'))
            player.start()
            await asyncio.sleep(3)
            player.stop()
            await voice_channel.disconnect()
        if quoteselect == 4:
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('lester4.mp3', after=lambda: print('played it'))
            player.start()
            await asyncio.sleep(1)
            player.stop()
            await voice_channel.disconnect()
        if quoteselect == 5:
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('lester5.mp3', after=lambda: print('played it'))
            player.start()
            await asyncio.sleep(1)
            player.stop()
            await voice_channel.disconnect()
        if quoteselect == 6:
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('lester6.mp3', after=lambda: print('played it'))
            player.start()
            await asyncio.sleep(2)
            player.stop()
            await voice_channel.disconnect()
        if quoteselect == 7:
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('lester7.mp3', after=lambda: print('played it'))
            player.start()
            await asyncio.sleep(3)
            player.stop()
            await voice_channel.disconnect()
        if quoteselect == 8:
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('lester8.mp3', after=lambda: print('played it'))
            player.start()
            await asyncio.sleep(2)
            player.stop()
            await voice_channel.disconnect()
        if quoteselect == 9:
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('lester9.mp3', after=lambda: print('played it'))
            player.start()
            await asyncio.sleep(4)
            player.stop()
            await voice_channel.disconnect()
        if quoteselect == 10:
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('lester10.mp3', after=lambda: print('played it'))
            player.start()
            await asyncio.sleep(2)
            player.stop()
            await voice_channel.disconnect()
        if quoteselect == 11:
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('lester11.mp3', after=lambda: print('played it'))
            player.start()
            await asyncio.sleep(1)
            player.stop()
            await voice_channel.disconnect()
        if quoteselect == 12:
            voice_channel = await client.join_voice_channel(message.author.voice_channel)
            player = voice_channel.create_ffmpeg_player('lester12.mp3', after=lambda: print('played it'))
            player.start()
            await asyncio.sleep(3)
            player.stop()
            await voice_channel.disconnect()

    if ('ok marc') in messagetobot.lower():
        msg = 'ok marc'
        await client.send_message(message.channel,msg)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('ok.mp3', after=lambda: print('played it'))
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
        player = voice_channel.create_ffmpeg_player('lester.mp3', after=lambda: print('played it'))
        player.start()
        await asyncio.sleep(122)
        player.stop()
        await voice_channel.disconnect()
        
    if ('!help') in messagetobot.lower():
        msg = 'My current commands are \n \n \
        "flum begun" "football" "!help" "pakistan" " lester" "flip coin" "roll dice" "ok marc" "is your refrigerator running?" "good bot" \
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

client.run('NTQ5OTk2NDI0NDIzNTM4Njg4.D1cDvA.OzgmwGXBMe8HpkhUPt1kbT3DtuA')
