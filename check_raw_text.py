import json
import random
import time
import discord
import asyncio
import google.generativeai as genai
import os
import platform


safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    }
]

prompt = "Your name is Flumbot, you are a knowledgeable member of the group chat, answering any questions one may " \
         "have and participating in the friendly banter in a succinct, wholesome, helpful manner. However, " \
         "You do love to input your own snark, quips, fun facts and whimsy where appropriate. You are kind and " \
         "receptive to criticism, but you can come off as harsh and direct, as your messages and responses  are very " \
         "succinct, being no more than 30 words. "

with open('token.json', "r") as file:
    data = json.load(file)
gtoken = data['token'][1]

genai.configure(api_key=gtoken)
chat = genai.GenerativeModel(model_name='gemini-2.0-flash', safety_settings=safety_settings).start_chat(history=[])
chat.send_message(prompt)

async def make_ordinal(n):          # make number ordinal
    '''
    Convert an integer into its ordinal representation::

        make_ordinal(0)   => '0th'
        make_ordinal(3)   => '3rd'
        make_ordinal(122) => '122nd'
        make_ordinal(213) => '213th'
    '''
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

async def fortune(ctx):
    chance = int(random.randrange(0, 1000))
    msg = "Let me think on what you have told me"
    await ctx.respond(msg, tts=True)
    await asyncio.sleep(4)
    msg = ":thinking:"

    if chance == 69:
        msg = "give me a couple hours to contemplate the results"
        await ctx.send(msg, tts=True)
        time.sleep(10800)
        guess = ['yes', 'no', 'poop', 'penile fracture']
        msg = random.choice(guess)
        await ctx.send(msg, tts=True)

    else:
        await ctx.send(msg, tts=True)
        await asyncio.sleep(6)
        wager = ['It would be wise to pursue other ventures', 'History does not side with you', 'no lol',
                 'I recommend you dab', 'You do you', "Just don't steal a tree",
                 "The future looks bright", "It is unlikely", "Pray on it", "Ask marc", "Ask rat", "Ask niche",
                 "Ask yourself", "best @everyone with your question",
                 "yes", "the future you seek has already happened", "marc said he will do it for you",
                 "only t-dubs will know the answer to your question", "Ask again", "It is certain",
                 "It is decidedly so", "Most likely", "Meh", "Signs point to yes", "Without a doubt", "Outlook good",
                 "Outlook not so good", "You may rely on it", "Cannot predict now",
                 "Just die", "I prescribe a midimania to heal", "Maybe think on it a few days",
                 "Rome wasn't built in a day", "The day of reckoning is approaching", "help me",
                 "Fo Sure", "Nah", "I don't feel like it", "behind you is the answer you seek", "yes", "no",
                 "yeah I think so", "Doesn't sounds right", "I think you are wrong", "Is that gamer?", "oh yeah",
                 "Think for yourself next time", "Uhhhhhhhhhhhhhhhhhhhhhhhh", "yuh", "nah", "What would Jesus Do?",
                 "Ratbuddy said ... no", "Ratbuddy said ... yes"]
        msg = random.choice(wager)
        await ctx.send(msg, tts=True)


async def call_api_and_reply(ctx, message):
    global chat
    global prompt
    global safety_settings

    try:
        response = chat.send_message(message)
        await ctx.channel.send(response.text)
    except Exception as e:
        await ctx.channel.send("me big doo doo head, you raised an " + str(e))
        chat = genai.GenerativeModel(model_name='gemini-2.0-flash', safety_settings=safety_settings).start_chat(history=[])
        chat.send_message(prompt)
        response = chat.send_message(message)
        await ctx.channel.send(response.text)
        print(e)


async def parse(ctx):
    
    message = str(ctx.content)                  # message is the full string
    words = message.lower().split(" ")          # words is string seperated into a list of words

    if 'bet' in words:                          # if person types "bet" respond with bet quip
        quips = './bin/en_data/quips.json'
        with open(quips, "r") as file:
            line = json.load(file)
        msg = "I'll bet " + str(random.choice(line['betmsg']))
        await ctx.channel.send(msg)

    positive = ["good", "amazing", "epic", "gamer", "funny"]            # good bot command key words
    negative = ["bad", "horrible", "awful", "annoying", "unfunny"]      # bad bot command key words
    context = ["bot"]                              # awarding key words

    if any(x in words for x in positive) and any(x in words for x in context):      # good bot check
        with open("./bin/en_data/longtermdata.json", "r") as file:
            data = json.load(file)

        data['dayvalues']['goodness'] = data['dayvalues']['goodness'] + 1
        msg = f"Thank :clap: you :clap: are :clap: the :clap: {await make_ordinal(data['dayvalues']['goodness'])} :clap: person :clap: to :clap: thank :clap: me. :clap:"

        with open("./bin/en_data/longtermdata.json", "w") as file:
            json.dump(data, file)

        await ctx.channel.send(msg, tts=True)

    if any(x in words for x in negative) and any(x in words for x in context):     # bad bot check
        with open("./bin/en_data/longtermdata.json", "r") as file:
            data = json.load(file)

        data['dayvalues']['goodness'] = data['dayvalues']['goodness'] - 1
        msg = f":rage: You :rage: brought :rage: my :rage: thanks :rage: to :rage: {await make_ordinal(data['dayvalues']['goodness'])} :rage: hope :rage: you :rage: feel :rage: good :rage:"

        with open("./bin/en_data/longtermdata.json", "w") as file:
            json.dump(data, file)

        await ctx.channel.send(msg, tts=True)

    if ('f') in words:                  # F recognition for respects
        msg = "F"
        await ctx.channel.send(msg)

    if "http" in message.lower():       # link recognition
        msg = "nice"
        await ctx.channel.send(msg)


    if "hey flumbot" in message.lower() and len(words) > 2:
        asyncio.create_task(call_api_and_reply(ctx, message))
        return

    if "flumbot" in message.lower():    # self awareness
        quips = './bin/en_data/quips.json'
        with open(quips, "r") as file:
            line = json.load(file)
        msg = str(random.choice(line['namemsg']))
        await ctx.channel.send(msg)

    if 'meow' in words and len(words) == 1:   # copypasta meme
        msg = "Wowwwww, you meow like a cat! That means you are one, right? Shut the fuck up. If you really want to " \
              "be put on a leash and treated like a domestic animal then that’s called a fetish, not “quirky” or " \
              "“cute”. What part of you seriously thinks that any part of acting like a feline establishes a " \
              "reputation of appreciation? Is it your lack of any defining aspect of personality that urges you to " \
              "resort to shitty representations of cats to create an illusion of meaning in your worthless life? " \
              "Wearing “cat ears” in the shape of headbands further notes the complete absence of human attribution " \
              "to your false sense of personality, such as intelligence or charisma in any form or shape. Where do " \
              "you think this mindset’s gonna lead you? You think you’re funny, random, quirky even? What makes you " \
              "think that acting like a fucking cat will make a goddamn hyena laugh? I, personally, feel extremely " \
              "sympathetic towards you as your only escape from the worthless thing you call your existence is to " \
              "pretend to be an animal. But it’s not a worthy choice to assert this horrifying fact as a dominant " \
              "trait, mainly because personality traits require an initial personality to lay their foundation on. " \
              "You’re not worthy of anybody’s time, so go fuck off, “cat-girl”. "
        await ctx.channel.send(msg)

    if "i see" in message.lower() and len(words) == 2:                  # EVE ad meme
        await ctx.channel.send(file=discord.File('./Pics/doyou.png'))
        await asyncio.sleep(5)
        await ctx.channel.send(file=discord.File('./Pics/hedo.png'))

    if "8 ball" in message.lower():
        msg = "Let me think on what you have told me"
        await ctx.channel.send(msg, tts=True)
        await asyncio.sleep(4)
        msg = ":thinking:"
        await ctx.channel.send(msg, tts=True)
        await asyncio.sleep(6)
        wager = ['It would be wise to pursue other ventures', 'History does not side with you', 'no lol',
                 'I recommend you dab', 'You do you', "Just don't steal a tree",
                 "The future looks bright", "It is unlikely", "Pray on it", "Ask marc", "Ask rat", "Ask niche",
                 "Ask yourself", "best @everyone with your question",
                 "yes", "the future you seek has already happened", "marc said he will do it for you",
                 "only t-dubs will know the answer to your question", "Ask again", "It is certain",
                 "It is decidedly so", "Most likely", "Meh", "Signs point to yes", "Without a doubt", "Outlook good",
                 "Outlook not so good", "You may rely on it", "Cannot predict now",
                 "Just die", "I prescribe a midimania to heal", "Maybe think on it a few days",
                 "Rome wasn't built in a day", "The day of reckoning is approaching", "help me",
                 "Fo Sure", "Nah", "I don't feel like it", "behind you is the answer you seek", "yes", "no",
                 "yeah I think so", "Doesn't sounds right", "I think you are wrong", "Is that gamer?", "oh yeah",
                 "Think for yourself next time", "Uhhhhhhhhhhhhhhhhhhhhhhhh", "yuh", "nah", "What would Jesus Do?",
                 "Ratbuddy said ... no", "Ratbuddy said ... yes"]
        msg = random.choice(wager)
        await ctx.channel.send(msg, tts=True)

    if "ok marc" in message.lower() and len(words) == 2:                # ok marc
        msg = "ok marc"
        await ctx.channel.send(msg, tts=True)

    if "hey peter" in message.lower() and len(words) == 2:              # peter ascii art
        msg1 = await ctx.channel.send("⠀⠀⠀⠀⡠⠔⠒⠉⢉⣉⣙⣒⣠⣀\n⠀⠀⠀⢠⠊⠐⡞⢩⣭⣭⣭⣀⡔⣒⡚⠇\n⠀⠀⠠⠁⠀⠀⠉⢿⡘⠃⣸⠃⠓⠒⢦⠌⢦⡀\n⠀⢀⠇⠀⠀⠀⠀⠠⢍⡉⠁⠐⠦⠤⠞⡀⠀⠀⢣\n"
                                          "⠀⠘⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠉⠉⢳⠄⠀⠸⡆\n⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⠁⠀⠀⠀⠀⡇\n⠀⡇⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⡇\n"
                                          "⡠⡇⠀⠀⠀⠀⠀⠀⠀⢷⣄⣀⡴⣤⣀⠴⠁⠀⠀⡇\n⢣⠘⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏\n⠀⠑⣄⠈⠢⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⡰\n"
                                          "⠀⠀⠈⠑⢄⡀⠁⠢⢄⡀⠀⠀⠀⠀⠀⢀⡠⠒⢁⠔\n⠀⠀⠀⠀⠀⠈⠒⠤⣀⠀⠉⠒⡂⢤⡰⠫⣄⡰⠃\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠼⠀⠠⡷⡀⠈\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱")
        await asyncio.sleep(30)
        await msg1.delete()

    if "default dance" in message.lower() and len(words) == 2:          # default dance
        for x in range(0, 2):
            if x == 0:
                msg = await ctx.channel.send("⠀⠀⠀⠀⣀⣤\n⠀⠀⠀⠀⣿⠿⣶\n⠀⠀⠀⠀⣿⣿⣀\n⠀⠀⠀⣶⣶⣿⠿⠛⣶\n⠤⣀⠛⣿⣿⣿⣿⣿⣿⣭⣿⣤\n⠒⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠉⣀\n"
                                                 "⠀⠤⣤⣤⣀⣿⣿⣿⣿⣀⠀⠀⣿\n⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣭⣶⠉\n⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⣭⣿⣿⣿⠀⣿⣿⣿\n⠀⠀⠀⣉⣿⣿⠿⠀⠿⣿⣿\n"
                                                 "⠀⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⣤\n⠀⠀⠀⣀⣿⣿⠀⠀⠀⣿⣿⣿\n⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿\n⠀⠀⠀⣿⣿⠛⠀⠀⠀⠉⣿⣿\n⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠛⣿\n"
                                                 "⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⣿\n⠀⠀⠀⠀⣛⠀⠀⠀⠀⠀⠀⠛⠿⠿⠿\n⠀⠀⠀⠛⠛")
            else:
                await msg.edit(content="⠀⠀⠀⠀⣀⣤\n⠀⠀⠀⠀⣿⠿⣶\n⠀⠀⠀⠀⣿⣿⣀\n⠀⠀⠀⣶⣶⣿⠿⠛⣶\n⠤⣀⠛⣿⣿⣿⣿⣿⣿⣭⣿⣤\n⠒⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠉⣀\n"
                                       "⠀⠤⣤⣤⣀⣿⣿⣿⣿⣀⠀⠀⣿\n⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣭⣶⠉\n⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⣭⣿⣿⣿⠀⣿⣿⣿\n⠀⠀⠀⣉⣿⣿⠿⠀⠿⣿⣿\n"
                                       "⠀⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⣤\n⠀⠀⠀⣀⣿⣿⠀⠀⠀⣿⣿⣿\n⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿\n⠀⠀⠀⣿⣿⠛⠀⠀⠀⠉⣿⣿\n⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠛⣿\n"
                                       "⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⣿\n⠀⠀⠀⠀⣛⠀⠀⠀⠀⠀⠀⠛⠿⠿⠿\n⠀⠀⠀⠛⠛")

            await asyncio.sleep(1)
            await msg.edit(content="⠀⠀⠀⣀⣶⣀\n⠀⠀⠀⠒⣛⣭\n⠀⠀⠀⣀⠿⣿⣶\n⠀⣤⣿⠤⣭⣿⣿\n⣤⣿⣿⣿⠛⣿⣿⠀⣀\n⠀⣀⠤⣿⣿⣶⣤⣒⣛\n⠉⠀⣀⣿⣿⣿⣿⣭⠉\n⠀⠀⣭⣿⣿⠿⠿⣿\n"
                                   "⠀⣶⣿⣿⠛⠀⣿⣿\n "
                                   "⣤⣿⣿⠉⠤⣿⣿⠿\n⣿⣿⠛⠀⠿⣿⣿\n⣿⣿⣤⠀⣿⣿⠿\n⠀⣿⣿⣶⠀⣿⣿⣶\n⠀⠀⠛⣿⠀⠿⣿⣿\n⠀⠀⠀⣉⣿⠀⣿⣿\n⠀⠶⣶⠿⠛⠀⠉⣿\n⠀⠀⠀⠀⠀⠀⣀⣿\n"
                                   "⠀⠀⠀⠀⠀⣶⣿⠿")
            await asyncio.sleep(1)
            await msg.edit(content="⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠶⠀⠀⣀⣀\n⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿\n⠀⠀⣀⣶⣤⣤⠿⠶⠿⠿⠿⣿⣿⣿⣉⣿⣿\n⠿⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣤⣿⣿⣿⣀\n"
                                   "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣶⣤\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⠿⣛⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣿⣿⣿⣿\n"
                                   "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠿⠀⣿⣿⣿⠛\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⣿⠀⠀⣿⣶\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⣿⣿⣶\n"
                                   "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⠤\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿\n"
                                   "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀\n "
                                   "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿")
            await asyncio.sleep(1)
            await msg.edit(content="⠀⠀⣀\n⠀⠿⣿⣿⣀\n⠀⠉⣿⣿⣀\n⠀⠀⠛⣿⣭⣀⣀⣤\n⠀⠀⣿⣿⣿⣿⣿⠛⠿⣶⣀\n⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⣉⣶\n⠀⠀⠉⣿⣿⣿⣿⣀⠀⠀⣿⠉\n⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿\n"
                                   "⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⠿\n⠀⣿⣿⣿⠿⠉⣿⣿⣿⣿\n⠀⣿⣿⠿⠀⠀⣿⣿⣿⣿\n⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿\n⠛⣿⣿⣀⠀⠀⠀⣿⣿⣿⣿⣶⣀\n⠀⣿⣿⠉⠀⠀⠀⠉⠉⠉⠛⠛⠿⣿⣶\n"
                                   "⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿\n⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉\n⣀⣶⣿⠛")
            await asyncio.sleep(1)
            await msg.edit(content="⠀⠀⠀⠀⠀⠀⠀⣀⣀\n⠀⠀⠀⠀⠀⠀⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿\n⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣶⣿⣿⣿⣶⣶⣤⣶⣶⠶⠛⠉⠉\n⠀⠀⠀⠀⠀⠀⣤⣿⠿⣿⣿⣿⣿⣿⠀⠀⠉\n"
                                   "⠛⣿⣤⣤⣀⣤⠿⠉⠀⠉⣿⣿⣿⣿\n⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⣿⣿⣿⣀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
                                   "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠛\n "
                                   "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣛⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠛⠿⣿⣿⣿⣶⣤\n⠀⠀⠀⠀⠀⠀⠀⣿⠛⠉⠀⠀⠀⠛⠿⣿⣿⣶⣀\n"
                                   "⠀⠀⠀⠀⠀⠀⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤\n⠀⠀⠀⠀⠀⠛⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠉")
            await asyncio.sleep(1)
            await msg.edit(content="⠀⠀⠀⠀⠀⠀⣤⣶⣶\n⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀\n⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿\n⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿\n⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿\n"
                                   "⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤\n "
                                   "⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿\n⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿\n⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛\n"
                                   "⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀\n⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿\n⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿\n⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿\n⠀⠀⠀⠀⠀⠀⣀⣿⣿\n"
                                   "⠀⠀⠀⠀⠤⣿⠿⠿⠿")
            await asyncio.sleep(1)
            await msg.edit(content="⠀⠀⠀⠀⣀\n⠀⠀⣶⣿⠿⠀⠀⠀⣀⠀⣤⣤\n⠀⣶⣿⠀⠀⠀⠀⣿⣿⣿⠛⠛⠿⣤⣀\n⣶⣿⣤⣤⣤⣤⣤⣿⣿⣿⣀⣤⣶⣭⣿⣶⣀\n⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠿⠿\n"
                                   "⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿\n⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿\n"
                                   "⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠛⠿⣿⣤\n"
                                   "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⣿⣿⣤\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣶⣿⠛⠉\n⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠀⠀⠉\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉")
            await asyncio.sleep(1)
            await msg.edit(content="⠀⠀⠀⠀⠀⠀⣶⣿⣶\n⠀⠀⠀⣤⣤⣤⣿⣿⣿\n⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶\n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶\n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿\n"
                                   "⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶\n⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤\n⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿\n⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉\n⠀⠀⠀⣿⣿⣿⣿⣿⣶\n"
                                   "⠀⠀⠀⠀⣿⠉⠿⣿⣿\n "
                                   "⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿\n⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉")
            await asyncio.sleep(1)
            await msg.edit(content="⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶\n⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶\n⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤\n⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀\n⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿\n"
                                   "⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶\n⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒\n⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉\n"
                                   "⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛\n "
                                   "⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤\n⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿\n⠀⠀⠀⠀⠀⠀⣿⠛\n⠀⠀⠀⠀⠀⠀⣭⣶")
            await asyncio.sleep(1)
            await msg.edit(content="⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿\n⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀\n⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀\n⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤\n"
                                   "⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿\n⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿\n⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉\n"
                                   "⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿\n⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉\n⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀\n⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿\n"
                                   "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿\n⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿\n⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛")
            await asyncio.sleep(1)
            await msg.edit(content="⠀⠀⠀⣶⣿⣶\n⠀⠀⠀⣿⣿⣿⣀\n⠀⣀⣿⣿⣿⣿⣿⣿\n⣶⣿⠛⣭⣿⣿⣿⣿\n⠛⠛⠛⣿⣿⣿⣿⠿\n⠀⠀⠀⠀⣿⣿⣿\n⠀⠀⣀⣭⣿⣿⣿⣿⣀\n⠀⠤⣿⣿⣿⣿⣿⣿⠉\n"
                                   "⠀⣿⣿⣿⣿⣿⣿⠉\n⣿⣿⣿⣿⣿⣿\n⣿⣿⣶⣿⣿\n⠉⠛⣿⣿⣶⣤\n⠀⠀⠉⠿⣿⣿⣤\n⠀⠀⣀⣤⣿⣿⣿\n⠀⠒⠿⠛⠉⠿⣿\n⠀⠀⠀⠀⠀⣀⣿⣿\n⠀⠀⠀⠀⣶⠿⠿⠛")
            await asyncio.sleep(3)
        await msg.delete()
        
