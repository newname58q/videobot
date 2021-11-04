# text to speech funtion
# ported from juvia group bot / module / tts.py
# Copyright (C) 2021 Veez Project

import traceback
from asyncio import get_running_loop
from io import BytesIO

from googletrans import Translator
from gtts import gTTS
from pyrogram import filters, Client
from pyrogram.types import Message


def convert(text):
    audio = BytesIO()
    i = Translator().translate(text, dest="en")
    lang = i.src
    tts = gTTS(text, lang=lang)
    audio.name = lang + ".mp3"
    tts.write_to_fp(audio)
    return audio


@Client.on_message(filters.command("ses"))
async def text_to_speech(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("💡 ʙɪʀ ᴍᴇᴛɴᴇ ᴄᴇᴠᴀᴘ ᴠᴇʀɪɴ...")
    if not message.reply_to_message.text:
        return await message.reply_text("💡 ʙɪʀ ᴍᴇᴛɴᴇ ᴄᴇᴠᴀᴘ ᴠᴇʀɪɴ...")
    m = await message.reply_text("🔁 ɪşʟᴇɴɪʏᴏʀ...")
    text = message.reply_to_message.text
    try:
        loop = get_running_loop()
        audio = await loop.run_in_executor(None, convert, text)
        await message.reply_audio(audio)
        await m.delete()
        audio.close()
    except Exception as e:
        await m.edit(str(e))
        es = traceback.format_exc()
        print(es)
