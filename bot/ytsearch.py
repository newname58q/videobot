# Copyright (C) 2021 By VeezMusicProject


from pyrogram import Client as app
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from config import Veez
from helpers.filters import command

@app.on_message(command(["bul", f"bul@{Veez.BOT_USERNAME}"]))
async def ytsearch(_, message: Message):
    m = await message.reply_text("🔎 **ᴜʀʟ ʙᴜʟᴜʏᴏʀᴜᴍ...**")
    try:
        if len(message.command) < 2:
            await message.reply_text("`/bul` needs an argument!")
            return
        query = message.text.split(None, 1)[1]
        results = YoutubeSearch(query, max_results=5).to_dict()
        i = 0
        text = ""
        while i < 5:
            text += f"**ɪꜱɪᴍ:** `{results[i]['title']}`\n"
            text += f"**ꜱüʀᴇ:** {results[i]['duration']}\n"
            text += f"**ɢöʀüɴᴛüʟᴇɴᴍᴇ:** {results[i]['views']}\n"
            text += f"**ᴋᴀɴᴀʟ:** {results[i]['channel']}\n"
            text += f"https://www.youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        await m.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await m.edit(str(e))
