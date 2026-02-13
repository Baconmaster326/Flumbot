import PIL.Image
import PIL
from PIL import Image
from openai import OpenAI, APIError, RateLimitError, AuthenticationError
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

# ========================== API KEY VALIDATION ==========================
# Quick sanity checks before we even try to connect
if not gtoken or not isinstance(gtoken, str):
    print("[OpenAI] ERROR: API key is empty or not a string. Check token.json index 1.")
elif not gtoken.startswith("sk-"):
    print(f"[OpenAI] WARNING: API key does not start with 'sk-'. "
          f"Got '{gtoken[:8]}...' — is this actually an OpenAI key?")
else:
    print(f"[OpenAI] API key loaded OK (starts with '{gtoken[:7]}...', length={len(gtoken)})")

# Try to verify the key actually works
client = OpenAI(api_key=gtoken)
try:
    # Minimal API call to verify connectivity and key validity
    models = list(client.models.list())
    print(f"[OpenAI] Connection verified! Account has access to {len(models)} models.")
except AuthenticationError as e:
    print(f"[OpenAI] AUTHENTICATION FAILED: Your API key is invalid or revoked. "
          f"Go to https://platform.openai.com/api-keys to get a new one.\n  Error: {e}")
except RateLimitError as e:
    print(f"[OpenAI] RATE LIMITED on startup check: Your account may have no credits or "
          f"has hit its usage limit. Check https://platform.openai.com/account/billing\n  Error: {e}")
except APIError as e:
    print(f"[OpenAI] API error during startup check: {e}")
except Exception as e:
    print(f"[OpenAI] Unexpected error during startup check: {e}")
# ========================================================================

prompt = "Your name is Flumbot, you are a human in a discord chat. You have bipolar disorder too. Use emojis in your " \
         "response. Talk like you were born in the year 2000. Also you are limited to 30 words maximum. Make some " \
         "based statements, we're talking like a conservative republican opinion. Your split personality also makes " \
         "you say some liberal talking points, but less often. Do not mention your head hurting, or the complexity, " \
         "let people think for themselves. "

chat_history = [{"role": "system", "content": prompt}]

# Keep chat history from growing forever (each entry ≈ tokens, and models have limits)
MAX_HISTORY = 50


def _trim_history():
    """Keep chat_history from growing beyond MAX_HISTORY entries (plus the system prompt)."""
    global chat_history
    # Always keep the system prompt (index 0), trim oldest messages after that
    if len(chat_history) > MAX_HISTORY + 1:
        chat_history = [chat_history[0]] + chat_history[-(MAX_HISTORY):]


def _chat_send(user_content):
    """Send a message to OpenAI and return the assistant's reply text."""
    global chat_history
    _trim_history()
    chat_history.append({"role": "user", "content": str(user_content)})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_history,
    )
    reply = response.choices[0].message.content or ""
    chat_history.append({"role": "assistant", "content": reply})
    if response.usage:
        print(f"[OpenAI] Tokens used: prompt={response.usage.prompt_tokens}, "
              f"completion={response.usage.completion_tokens}, "
              f"total={response.usage.total_tokens} | "
              f"History length: {len(chat_history)} messages")
    return reply


def _chat_send_image(text, image_path):
    """Send a message with an image to OpenAI (vision) and return the reply."""
    global chat_history
    _trim_history()
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
    if response.usage:
        print(f"[OpenAI] Tokens used: prompt={response.usage.prompt_tokens}, "
              f"completion={response.usage.completion_tokens}, "
              f"total={response.usage.total_tokens} | "
              f"History length: {len(chat_history)} messages")
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
    except RateLimitError as e:
        print(f"[OpenAI] RATE LIMITED: {e}")
        await channel.send("I'm being rate limited by OpenAI 😵 — either out of credits or too many requests. "
                           "Check https://platform.openai.com/account/billing")
    except AuthenticationError as e:
        print(f"[OpenAI] AUTH ERROR: {e}")
        await channel.send("My API key isn't working 🔑 — check token.json and "
                           "https://platform.openai.com/api-keys")
    except Exception as e:
        # Let them know something went wrong
        print(f"[OpenAI] Error: {type(e).__name__}: {e}")
        await channel.send("me big doo doo head, you raised an " + str(e))
        # Restart the chat
        try:
            response_text = _chat_send("I just showed you something absolutely vile, it hurts your brain to consider how awful it is.")
            await channel.send(response_text)
        except Exception as e2:
            print(f"[OpenAI] Recovery also failed: {e2}")
