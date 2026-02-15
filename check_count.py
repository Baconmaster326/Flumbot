import asyncio
import json
import os
import random

async def parse(ctx):
    try:
        number = int(ctx.content)       # do we have a number?
    except ValueError:
        return

    serverid = str(ctx.guild.name)
    username = str(ctx.author)
    print(f"{username} is attempting to continue the count, with the number {number} in server {serverid}")

    while os.path.exists("./write.lock"):
        await asyncio.sleep(1)
        print("waiting for other server to finish with the file...")

    altfilename = './data/longtermdata.json'
    with open(altfilename, "r") as file:
        data = json.load(file)
    filename = 'data/userdata.json'
    with open(filename, "r") as file:
        userdata = json.load(file)

    try:                                    # do we have a count entry for the server?
        print(data["count"][serverid])
    except KeyError:
        data["count"][serverid] = []        # if no make a list, containing username, current count, current highscore for server
        data["count"][serverid].append("username")
        data["count"][serverid].append(0)
        data["count"][serverid].append(0)

    prev_counter = data["count"][serverid][0]
    current_count = data["count"][serverid][1]
    high_score = data["count"][serverid][2]

    if prev_counter != username:                             # is this person counting twice?
        if number == current_count + 1:                     # different person, are they doing the correct number?
            if number > high_score:                     # new record?
                data["count"][serverid][2] = number     # update records
                await ctx.add_reaction('🏆')
            data["count"][serverid][0] = username       # update records
            data["count"][serverid][1] = number

            # award person credit for counting
            try:    # do they have wallet?
                userdata[username]["score"] = userdata[username]["score"] + number      # yes, give them money
            except KeyError:
                try:
                    userdata[username]["score"] = number                # do they have an inventory
                except KeyError:
                    userdata[username] = {}                             # no inventory, make database entry
                    userdata[username]["score"] = number

            with open('data/emoji.json', "r", encoding="utf8") as file:
                emoji = json.load(file)
            tries = 0
            while True:
                tries += 1
                try:
                    if username == "emrmann":
                        goji = []
                        if random.randint(0, 5) == 2:
                            for each in range(9):
                                goji.append(random.choice(emoji[random.choice(list(emoji.keys()))]))
                            for each in goji:
                                await ctx.add_reaction(each['emoji'])
                    key = list(emoji.keys())
                    key = random.choice(key)
                    emoji = random.choice(emoji[key])['emoji']
                    await ctx.add_reaction(emoji)
                    break
                except:
                    if tries == 5:
                        try:
                            await ctx.add_reaction('<:monkaS:583814789298651154>')
                        except:
                            await ctx.add_reaction('👀')
                        break
                    else:
                        continue

        else:       # wrong number handler
            await ctx.channel.send(f"{username[:-5]} ruined the count at {data['count'][serverid][1]}. They typed the wrong number!")

            try:
                userdata[username]["score"] = userdata[username]["score"] - data["count"][serverid][1]
            except KeyError:
                try:
                    userdata[username]["score"] = 0
                except KeyError:
                    userdata[username] = {}
                    userdata[username]["score"] = 0

            data["count"][serverid][0] = "Flumbot#1927"         # reset to default values
            data["count"][serverid][1] = 0
            await ctx.add_reaction('💦')

    else:           # double count handler
        await ctx.channel.send(f"{username[:-5]} ruined the count at {data['count'][serverid][1]}. They counted twice...")
        try:
            userdata[username]["score"] = userdata[username]["score"] - data["count"][serverid][1]
        except KeyError:
            try:
                userdata[username]["score"] = 0
            except KeyError:
                userdata[username] = {}
                userdata[username]["score"] = 0

        data["count"][serverid][0] = "Flumbot#1927"             # reset to default values
        data["count"][serverid][1] = 0
        await ctx.add_reaction('💦')

    file = open('write.lock', 'w')
    file.close()

    with open(filename, "w") as file:
        json.dump(userdata, file)
    with open(altfilename, "w") as file:
        json.dump(data, file)

    os.remove("write.lock")
