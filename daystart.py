import json
import os
import random
import shutil
from datetime import date
import discord
import requests
import string
from bs4 import BeautifulSoup
from PIL import Image

def game():
    quips = './bin/en_data/quips.json'
    with open(quips, "r") as file:
        line = json.load(file)
    game = str(random.choice(line['gamemsg']))
    return game


def getad():
    quips = './bin/en_data/quips.json'
    with open(quips, "r") as file:
        line = json.load(file)
    ad = str(random.choice(line['adlinks']))
    return ad


def awake():
    quips = './bin/en_data/quips.json'
    with open(quips, "r") as file:
        line = json.load(file)
    awake = str(random.choice(line['startmsg']))
    return awake

def days():
    today = date.today()
    start = today - date(2019, 2, 26)
    return int(start.days)

async def activity():
    quips = './bin/en_data/quips.json'
    with open(quips, "r") as file:
        line = json.load(file)
        return discord.Streaming(name=game(), url=str(random.choice(line['ytlinks'])))

def datecheck():
    today = date.today()
    # compare to flumbot birthday
    start = today - date(2019, 2, 26)
    filename = './bin/en_data/userdata.json'
    altfilename = './bin/en_data/longtermdata.json'
    with open(altfilename, "r") as file:
        data = json.load(file)
    with open(filename, "r") as file:
        userdata = json.load(file)
    # check if bot has restarted today already, saved value from end of this loop yesterday
    if int(start.days) == data['dayvalues']['days']:
        return 0

    # else check if new year is upon us
    if (int(start.days) % 365) == 0:
        data[0] = str(start.days) + '\n'
        with open(altfilename, "w") as file:
            json.dump(data, file)
        return int(start.days)

    # else must be a new day so start new day protocall
    else:
        data['dayvalues']['days'] = start.days
        data['dayvalues']['game'] = 'not set'
        data['dayvalues']['check-in'] = 'empty'
        for x in userdata:
            try:
                userdata[x]['status'] = 0
            except KeyError:
                userdata[x] = userdata[x]
                userdata[x]['status'] = 0
            if x == 'ratbuddy#9913' or x == 'Dunsparce#0080':
                userdata[x]['status'] = -1
        with open(filename, "w") as file:
            json.dump(userdata, file)
        with open(altfilename, "w") as file:
            json.dump(data, file)
        return 1

async def profile(client):
    if random.randint(1, 100) > 10:
        selector = random.randint(0, 1)
        with open('./Pics/big' + str(selector) + '.png', 'rb') as f:
            await client.user.edit(avatar=f.read())
        return
    else:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/78.0.3904.108 Safari/537.36 '
        }
        currentDir = os.getcwd()
        path = currentDir  # saving images to Images folder
        url = 'https://www.thispersondoesnotexist.com/image'
        attempts = 0
        while attempts < 5:  # retry 5 times
            try:
                filename = 'image.jpg'
                r = requests.get(url, headers=headers, stream=True, timeout=5)
                if r.status_code == 200:
                    with open(os.path.join(path, filename), 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                break
            except Exception as e:
                attempts += 1
                print(e)
        image = Image.open('image.jpg')
        width, height = image.size
        image = image.crop(((width/4), ((height/4)+50), (3*width/4), ((3*height/4)+100)))
        image.save('image.jpg')
        with open('image.jpg', 'rb') as f:
            await client.user.edit(avatar=f.read())
        os.remove('image.jpg')

async def link():
    fails = 1
    imgur_url = "https://i.imgur.com/"
    selection = string.ascii_letters + string.digits
    leng = random.choices(population=[5, 6, 7], weights=[.8, .15, .05])
    leng = leng[0]
    ext = [".png", ".jpg"]
    ext = random.choice(ext)
    while fails == 1:
        r1, r2, r3, r4, r5, r6, r7 = random.sample(selection, 7)
        if leng == 7:
            print("Trying Length 7 links")
            code = r1 + r2 + r3 + r4 + r5 + r6 + r7
        elif leng == 6:
            print("Trying Length 6 links")
            code = r1 + r2 + r3 + r4 + r5 + r6
        else:
            print("Trying Length 5 links")
            code = r1 + r2 + r3 + r4 + r5
        file_name = code
        full_url = imgur_url + file_name + ext

        # does imgur link exist?
        request = requests.get(full_url)
        if request.status_code == 200:
            f_name = 'SPOILER_daily' + ext
            with open(f_name, 'wb') as f:
                f.write(request.content)
            try:
                image = Image.open(f_name)
            except:
                os.remove(f_name)
                continue
            width, height = image.size
            if width < 200 or height < 200:
                print("too small")
                image.close()
                os.remove(f_name)
                continue
            image.close()
            return f_name

async def link2():
    possible = string.ascii_lowercase + string.digits
    possible = list(possible)
    possible.remove('0')
    while (1):
        link = []
        for each in range(0,6):
            link.append(random.choice(possible))
        link = ''.join(link)
        link = "https://prnt.sc/" + link
        user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        request = requests.get(link, headers={"User-Agent": user_agent}, allow_redirects=False)
        soup = BeautifulSoup(request.content, "html.parser")
        images = soup.find_all("img", {"class": "no-click screenshot-image"})
        for tag in images:
            src_img_from_html = tag["src"]

            if not src_img_from_html.startswith("http"):
                continue

            img = requests.get(src_img_from_html)

            if img.status_code == 520:
                continue

            with open("SPOILER_daily.png", "wb") as file:
                file.write(img.content)
                file.close()

            f_name = "./SPOILER_daily.png"
            try:
                image = Image.open(f_name)
            except:
                os.remove(f_name)
                continue
            width, height = image.size
            if width < 200 or height < 200:
                print("too small")
                image.close()
                os.remove(f_name)
                continue
            image.close()
            return "SPOILER_daily.png"
