import PIL.Image
import PIL
from PIL import Image
import google.generativeai as genai
import json
import requests
import io
import os
import asyncio

with open('token.json', "r") as file:
    data = json.load(file)
gtoken = data['token'][1]

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

prompt = "Your name is Flumbot, you are a human in a discord chat. Use emojis in your " \
         "response. Talk like you were born in the year 2000. Also you are limited to 47 words maximum." \
         " be crass and rude sometimes. But be factual and truthful. If someone calls you out, get MAD." \
         " sometimes you say things that are a little controversal."

genai.configure(api_key=gtoken)
chat = genai.GenerativeModel(model_name='gemma-3-27b-it', safety_settings=safety_settings).start_chat(history=[])
chat.send_message(prompt)


async def quip_this(channel, in_message, image=None):
    # Grab saved chat session
    global chat
    global prompt
    global safety_settings

    try:
        if len(in_message.attachments) > 0:
            try:
                image_data = requests.get(in_message.attachments[0].url).content
                #Try to open image.
                image = Image.open(io.BytesIO(image_data))
                # Verify image.
                image.verify()
                with open("reply.png", "wb") as f:
                    f.write(image_data)
                image.close()
                image = Image.open("reply.png")
            except (requests.exceptions.RequestException, OSError, Image.UnidentifiedImageError) as e:
                print(f"Error downloading or opening image: {e}")
    except Exception as e:
        print("not an image prompt")
    try:
        if image is not None:
            response = chat.send_message(
                ["Tell me, as flumbot, what is in this image and what are your thoughts on it?", image])
            await channel.send(response.text)
            image.close()
            os.remove("reply.png")
            return
        else:
            response = chat.send_message(in_message)
            await channel.send(response.text)
    except FileNotFoundError:
        print("nothing else to do here")
    except Exception as e:
        # Let them know something went wrong
        await channel.send("me big doo doo head, you raised an " + str(e))
        # Restart the chat
        response = chat.send_message("I just showed you something absolutely vile, it hurts your brain to consider how awful it is.")
        await channel.send(str(response.text))
