import discord
import ffmpeg

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if ('ok marc') in message.content:
        msg = 'ok marc'.format(message)
        await client.send_message(message.channel, msg)
        voice_channel = await client.join_voice_channel(message.author.voice_channel)
        player = voice_channel.create_ffmpeg_player('Futbol.mp3', after=lambda: print('played it'))
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        player.stop()
        await voice_channel.disconnect()
    else:
        await client.say('cant find that mofo')
        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTQ5OTk2NDI0NDIzNTM4Njg4.D1cDvA.OzgmwGXBMe8HpkhUPt1kbT3DtuA')
