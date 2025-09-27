import asyncio
import discord
import librosa
import json


async def join(channel):
    try:
        voice_client = await channel.connect()
    except AttributeError:
        voice_client = None
    return voice_client


async def leave(voice_client):
    await voice_client.disconnect(force=True)
    return True

async def playclip(cliplocation, ctx, client, overide):
    def check(m):
        return m.content.lower() == 'stop' or m.content.lower() == 'skip'
                                                                              # is user in a voice channel?
    try:
        voice_client = await join(ctx.author.voice.channel)
    except AttributeError:
        ctx.send("Can't fool me :triumph: you aren't even in the voice chat :triumph:")
        return

    duration = librosa.get_duration(filename=cliplocation) + 1.5                              # get duration

    if overide != 0:                                                                       # are we constrained on time?
        duration = overide
    await voice_client.connect()

    if duration > 60:
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("./Clips/Oneoff/alert.wav"))
        await asyncio.sleep(1.5)
        ctx.voice_client.play(source, after=lambda e: print(f"Player error: {e}") if e else None)
        await asyncio.sleep(5.3)

    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(cliplocation))
    await asyncio.sleep(1.5)
    ctx.voice_client.play(source, after=lambda e: print(f"Player error: {e}") if e else None)

    print(f"Now Playing {cliplocation}")

    filename = './bin/en_data/repeats.json'
    with open(filename, "r") as file:
        data = json.load(file)

    if not overide:
        if '\\' in cliplocation:
            cliplocation = cliplocation.split('\\').pop()
        else:
            cliplocation = cliplocation.split('/').pop()
        try:
            data[cliplocation] += 1
        except KeyError:
            data[cliplocation] = 0

        with open(filename, "w") as file:
            json.dump(data, file)

    try:
        await client.wait_for('message', check=check, timeout=duration)
        print('done playing clip')
        await ctx.voice_client.disconnect(force=True)
        if overide:
            return
        if data[cliplocation] % 10 == 0:
            if data[cliplocation] == 0:
                await ctx.send("That was the first time " + "'" + cliplocation + "'" + " has been played, please clap...", tts=True)
                return
            await ctx.send("Clip " + "'" + cliplocation + "'" + " has played " + str(data[cliplocation]) +\
                     " times... \nP\nO\nG", tts=True)
    except asyncio.TimeoutError:
        await ctx.voice_client.disconnect(force=True)
        print('done playing clip')
        if overide:
            return
        if data[cliplocation] % 10 == 0:
            if data[cliplocation] == 0:
                await ctx.send("That was the first time " + "'" + cliplocation + "'" + " has been played, please clap...", tts=True)
                return
            await ctx.send("Clip " + "'" + cliplocation + "'" + " has played " + str(data[cliplocation]) +\
                     " times... \nP\nO\nG", tts=True)
            return