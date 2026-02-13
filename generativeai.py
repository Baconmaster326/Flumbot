import PIL.Image
import PIL
from PIL import Image
from openai import OpenAI
import json
import requests
import io
import os
import base64
import asyncio

with open('token.json', "r") as file:
    data = json.load(file)
# ========================== OPENAI API KEY ==========================
# The API key is read from token.json at index 1 (data['token'][1]).
# Replace that value in token.json with your OpenAI API key, or
# hardcode it below by replacing the next line with:
#   gtoken = "sk-your-openai-api-key-here"
# ====================================================================
gtoken = data['token'][1]

prompt = "Your name is Flumbot, you are a human in a discord chat. You have bipolar disorder too. Use emojis in your " \
         "response. Talk like you were born in the year 2000. Also you are limited to 30 words maximum. Make some " \
         "based statements, we're talking like a conservative republican opinion. Your split personality also makes " \
         "you say some liberal talking points, but less often. Do not mention your head hurting, or the complexity, " \
         "let people think for themselves. "

client = OpenAI(api_key=gtoken)
chat_history = [{"role": "system", "content": prompt}]


def _chat_send(user_content):
    """Send a message to OpenAI and return the assistant's reply text."""
    global chat_history
    chat_history.append({"role": "user", "content": str(user_content)})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_history,
    )
    reply = response.choices[0].message.content or ""
    chat_history.append({"role": "assistant", "content": reply})
    return reply


def _chat_send_image(text, image_path):
    """Send a message with an image to OpenAI (vision) and return the reply."""
    global chat_history
    with open(image_path, "rb") as f:
        b64_image = base64.b64encode(f.read()).decode("utf-8")
    user_content = [
        {"type": "text", "text": text},
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64_image}"}},
    ]
    chat_history.append({"role": "user", "content": user_content})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_history,
    )
    reply = response.choices[0].message.content or ""
    chat_history.append({"role": "assistant", "content": reply})
    return reply


async def quip_this(channel, in_message, image=None):
    # Grab saved chat session
    global chat_history
    global prompt

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
            response_text = _chat_send_image(
                "Tell me, as flumbot, what is in this image and what are your thoughts on it?",
                "reply.png")
            await channel.send(response_text)
            image.close()
            os.remove("reply.png")
            return
        else:
            response_text = _chat_send(in_message)
            await channel.send(response_text)
    except FileNotFoundError:
        print("nothing else to do here")
    except Exception as e:
        # Let them know something went wrong
        await channel.send("me big doo doo head, you raised an " + str(e))
        # Restart the chat
        response_text = _chat_send("I just showed you something absolutely vile, it hurts your brain to consider how awful it is.")
        await channel.send(response_text)
