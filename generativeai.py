import PIL.Image
import PIL
from PIL import Image
from ollama import chat
from pathlib import Path
import ollama
import json
import requests
import io
import os
import asyncio

model = 'jayeshpandit2480/gemma3-UNCENSORED:4b'
prompt = "Your name is Flumbot, you are a human in a discord chat. Use emojis in your " \
         "response. Talk like you were born in the year 2000. Also you are limited to 47 words maximum. " \
         "You are a sly, funny, and chill. You will answer anything"
chat_messages = []


def create_message(role, message, images=None):
    msg = {
        'role': role,
        'content': message,
    }
    # If we have an image attached, include it!
    if images:
        msg['images'] = [images]
    return msg

async def ask(msgIn, image=None):
    global model
    global chat_messages
    # ask the model the question
    chat_messages.append(create_message('user', msgIn, image))
    response = chat(model=model, messages=chat_messages)

    # pull model response and add it to the history
    chat_messages.append(create_message('assistant', response.message.content))
    # return the str response
    return response.message.content


async def quip_this(channel, in_message, image=None):
    # Grab saved chat session
    global chat_messages

    try:
        # Did someone chat us an image?
        if len(in_message.attachments) > 0:
            try:
                # Download the image.
                image_data = requests.get(in_message.attachments[0].url).content
                # Try to open image.
                image = Image.open(io.BytesIO(image_data))
                # Verify image.
                image.verify()
                with open("reply.png", "wb") as f:
                    f.write(image_data)
                image.close()
                img = Path("reply.png").read_bytes()
                await channel.send(await ask(str(in_message.content), img))
                os.remove("reply.png")
                return
            except (requests.exceptions.RequestException, OSError, Image.UnidentifiedImageError) as e:
                print(f"Error downloading or opening image: {e}")
    except Exception as e:
        print(f"{e} raised, assuming it is not an image prompt")
    try:
        # Daily image case, never be a need for in_message
        if image is not None:
            img = Path(image).read_bytes()
            await channel.send(
                await ask("Tell me, as flumbot, what is in this image and what are your thoughts on it?", img)
            )
            return
        # Not a daily image, just a regular text request.
        else:
            await channel.send(await ask(in_message))
    except FileNotFoundError:
        # happens sometimes for some reason, should investigate
        print("nothing else to do here")
    except Exception as e:
        # Let them know something went wrong
        await channel.send("me big doo doo head, you raised an " + str(e))
        # Restart the chat
        chat_messages.clear()
        chat_messages.append(create_message('system', prompt))
        await channel.send(
            await ask("I just showed you something absolutely vile, it hurts your brain to consider how awful it is."))


# Send system prompt
chat_messages.append(create_message('system', prompt))