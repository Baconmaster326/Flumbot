import asyncio
import json
import os
import random
import shutil
import re
import PIL
import io
import discord
import requests
import asyncpraw
import google.generativeai as genai
from gppt import GetPixivToken
from pixivpy3 import AppPixivAPI
from datetime import date
from PIL import Image
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


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
        url = 'https://www.thispersondoesnotexist.com/'
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
        image = image.crop(((width / 4), ((height / 4) + 50), (3 * width / 4), ((3 * height / 4) + 100)))
        image.save('image.jpg')
        with open('image.jpg', 'rb') as f:
            await client.user.edit(avatar=f.read())
        os.remove('image.jpg')


async def get_random_image_from_reddit():
    with open('token.json', "r") as file:
        data = json.load(file)
    rtoken = data['token'][2]
    # Create a Reddit instance
    reddit = asyncpraw.Reddit(client_id='zQodI26PnfVmAhgdZogiLA',
                              client_secret=rtoken,
                              user_agent='FlumbotAPRAW')
    pics = []
    tempreddit = await reddit.subreddit("all")
    sr = tempreddit.hot(limit=250)
    try:
        async for submission in sr:
            if not submission.is_self:
                if submission.url.endswith('.jpg') or submission.url.endswith('.png'):
                    pics.append(submission.url)
    except Exception as e:
        print(e)
        print("can't find picture in all :(")

    request = requests.get(random.choice(pics))
    with open("SPOILER_daily.png", "wb") as file:
        print(request.url)
        file.write(request.content)
        file.close()

    return "SPOILER_daily.png"


async def get_random_image_from_4chan():
    await asyncio.sleep(65)
    # Choose a random board
    boards = ['a', 'c', 'w', 'm', 'cgl', 'cm', 'n', 'jp', 'vp', 'v', 'vg', 'vr', 'co', 'g', 'tv', 'k', 'o', 'an', 'tg',
              'sp', 'asp', 'sci', 'int', 'out', 'toy', 'biz', 'i', 'po', 'p', 'ck', 'ic', 'wg', 'mu', 'fa', '3', 'gd',
              'diy', 'wsg', 's', 'hc', 'hm', 'h', 'e', 'u', 'd', 'y', 't', 'hr', 'gif', 'trv', 'fit', 'x', 'lit', 'adv',
              'lgbt', 'mlp', 'b', 'r', 'r9k', 'pol', 'soc', 's4s']
    board = random.choice(boards)
    #Retrieves a random image URL from a 4chan board using Selenium.
    try:
        # prepare scrape-er
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ("
                                     "KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

        # scrape
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
        url = f"https://boards.4chan.org/{board}/"
        driver.get(url)
        html_content = driver.page_source
        driver.quit()

        # Regex to find image URLs. (This is very fragile and may break.)
        image_urls = re.findall(r'href="(//i\.4cdn\.org/\w+/\d+\.(?:jpg|jpeg|png|gif|webp))"', html_content)

        # choose a random image from images on site
        if image_urls:
            random_image_url = "https:" + random.choice(image_urls)
            try:
                image_data = requests.get(random_image_url).content
                #Try to open image.
                img = Image.open(io.BytesIO(image_data))
                # Verify image.
                img.verify()
                print(random_image_url)
                with open("SPOILER_daily.png", "wb") as f:
                    f.write(image_data)
                return "SPOILER_daily.png"
            except (requests.exceptions.RequestException, OSError, Image.UnidentifiedImageError) as e:
                print(f"Error downloading or opening image: {e}")
                return "SPOILER_daily.png"
        else:
            print("No pictures found on 4chin board")
            return get_random_image_from_reddit()  # we found a bad 4chin board, revert to reddit.
    except Exception as e:
        print(f"Error: {e}")
        return None


async def quip_image(link):
    with open('token.json', "r") as file:
        data = json.load(file)
    gtoken = data['token'][1]

    prompt = "Your name is Flumbot, you are a knowledgeable member of the group chat, answering any questions one may " \
             "have and participating in the friendly banter in a succinct, wholesome, helpful manner. However, " \
             "You do love to input your own snark, quips, fun facts and whimsy where appropriate. You are kind and " \
             "receptive to criticism, but you can come off as harsh and direct, as your messages and responses  are " \
             "very succinct, being no more than 30 words. "

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

    genai.configure(api_key=gtoken)
    model = genai.GenerativeModel(model_name='gemini-2.0-flash', safety_settings=safety_settings)

    image = Image.open(link)

    try:
        contents = [f"{prompt}. Tell me, as flumbot, what is in this image and what are your thoughts on it?", image]
        response = model.generate_content(contents)
        if "Traceback" in response.text or len(response.candidates) == 0:
            raise Exception
    except Exception as e:
        print(e)
        model = genai.GenerativeModel(model_name='gemini-2.0-flash', safety_settings=safety_settings)
        response = model.generate_content(
            f"{prompt}. I just showed you something disgusting, tell me your thoughts on that. You experience intense "
            f"pain looking at the image.")
    response.resolve()
    image.close()
    return response.text


async def get_refresh_token():
    # check if we already have the token generated
    with open("token.json", "r") as f:
        data = json.load(f)
    # check if token is valid
    try:
        api = AppPixivAPI()
        api.auth(refresh_token=data['token'][3])
        refresh_token = data['token'][3]
    except Exception as e:
        print(f"An error occurred: {e}")
        # usually this means we need a new token, as the other one expired
        g = GetPixivToken(headless=True)
        refresh_token = g.login(username="user_nkhz5545", password=data['token'][4])["refresh_token"]
        data['token'][3] = refresh_token
        # dump the new token to the file just in case
        with open("token.json", "w") as f:
            json.dump(data, f)
    return refresh_token


async def get_random_image_from_pixiv():
    api = AppPixivAPI()
    try:
        # Login
        api.auth(refresh_token=await get_refresh_token())
        print("Login successful!")
        # Topics we want to get random images for
        SEARCH_QUERY = ["R-18", "R18", "R-18G", "original", "Sonic", "Pokemon", "Cartoon_Network", "Horse Girl", "Neko",
                        "girl", "male", "female", "kemono", "POV", "mature", "anime", "aircraft", "minecraft", "concept"
                        ]
        # grab a random result
        search_result = api.search_illust(random.choice(SEARCH_QUERY), sort='date_desc')
        if not search_result or not search_result.illusts:
            print(f"No illustrations found for query: {SEARCH_QUERY}")
            # this is broken, breakout get a reddit image
            return get_random_image_from_reddit()

        illustration = random.choice(search_result.illusts)
        # print out information about image
        print("Retrieved random illustration:")
        print(f"  Title: {illustration.title}")
        print(f"  Author: {illustration.user.name}")
        print(f"  URL: https://www.pixiv.net/en/artworks/{illustration.id}")

        # time to grab the direct image link
        url = illustration.image_urls['medium']
        # ensure we have a properly former header, they reject all calls without these
        headers = {
            'Referer': f'https://www.pixiv.net/en/artworks/{illustration.id}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'Accept': 'image/jpeg,image/png,*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        try:
            # open the webpage
            image_data = requests.get(url, headers=headers).content
            # Try to open the image.
            img = Image.open(io.BytesIO(image_data))
            # Verify image
            img.verify()
            # Save Image
            with open("SPOILER_daily.png", "wb") as f:
                f.write(image_data)
            return "SPOILER_daily.png"
        except (requests.exceptions.RequestException, OSError, Image.UnidentifiedImageError) as e:
            print(f"Error downloading or opening image: {e}")
            return get_random_image_from_reddit()

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your credentials or the illustration ID.")

