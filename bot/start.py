# Copyright (C) 2021 By VeezMusicProject

from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from config import Veez
from helpers.decorators import sudo_users_only
from helpers.filters import command

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{Veez.BOT_USERNAME}"]))
async def start(_, m: Message):
    if m.chat.type == "private":
        await m.reply_text(
            f"✨ **ᴍᴇʀʜᴀʙᴀ, ʙᴇɴ ʙɪʀ ᴠɪᴅᴇᴏ ʙᴏᴛᴜʏᴜᴍ**\n\n💭 **ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛʟᴇʀɪɴɪᴢᴅᴇ ᴠɪᴅᴇᴏ ɪᴢʟᴇᴍᴇɴɪᴢɪ ꜱᴀɢʟᴀʏᴀʙɪʟɪʀɪᴍ "
            f"ᴋᴏʟᴀʏ ʏᴏʟ.**\n\n❔ **ɴᴀꜱıʟ ᴋᴜʟʟᴀɴᴀᴄᴀɢıɴıᴢı ɢöʀᴍᴇᴋ ɪçɪɴ ʏᴀʀᴅıᴍ ɪꜱᴛᴇʏɪɴ** 👇🏻",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "➕ ʙᴇɴɪ ɢʀᴜᴘ ᴇᴋʟᴇ  ➕", url=f"https://t.me/{Veez.BOT_USERNAME}?startgroup=true")
                ], [
                    InlineKeyboardButton(
                        "❔ ʙᴜ ʙᴏᴛ ɴᴀꜱɪʟ ᴋᴜʟʟᴀɴɪʟɪʀ", callback_data="cbguide")
                ], [
                    InlineKeyboardButton(
                        "🌐 ɢᴇʟɪşᴛɪʀɪᴄɪʟᴇʀ", callback_data="cbinfo")
                ], [
                    InlineKeyboardButton(
                        "💬 ɢʀᴜᴘ", url="https://t.me/paradiseailesi"),
                    InlineKeyboardButton(
                        "📣 ᴋᴀɴᴀʟ", url="https://t.me/paradisekanal")
                ], [
                    InlineKeyboardButton(
                        "👩🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/jackdanielssx")
                ], [
                    InlineKeyboardButton(
                        "📚 ᴋᴏᴍᴜᴛ ʟɪꜱᴛᴇꜱɪ", callback_data="cblist")
                ]]
            ))
    else:
        await m.reply_text("**✨ ʙᴏᴛ şᴜ ᴀɴ ᴀᴋᴛɪꜰ  ✨**",
                           reply_markup=InlineKeyboardMarkup(
                               [[
                                   InlineKeyboardButton(
                                       "❔ ʙᴜ ʙᴏᴛᴜ ɴᴀꜱıʟ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀɪᴍ", callback_data="cbguide")
                               ], [
                                   InlineKeyboardButton(
                                       "🌐 ʏᴏᴜᴛᴜʙᴇ ᴅᴇ ᴀʀᴀᴛ", switch_inline_query='')
                               ], [
                                   InlineKeyboardButton(
                                       "📚 ᴋᴏᴍᴜᴛ ʟɪꜱᴛᴇꜱɪ", callback_data="cblist")
                               ]]
                           )
                           )


@Client.on_message(command(["alive", f"alive@{Veez.BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def alive(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        f"""✅ **bot çalışıyor **\n<b>💠 **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨ ɢʀᴜᴘ", url=f"https://t.me/paradiseailesi"
                    ),
                    InlineKeyboardButton(
                        "📣 ᴋᴀɴᴀʟ", url=f"https://t.me/paradisekanal"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{Veez.BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(_, m: Message):
    sturt = time()
    m_reply = await m.reply_text("ᴘɪɴɢ...")
    delta_ping = time() - sturt
    await m_reply.edit_text(
        "🏓 `PONG!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{Veez.BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(_, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        "🤖 ʙᴏᴛ ᴅᴜʀᴜᴍᴜ 🤖\n\n"
        f"• **çᴀʟışᴍᴀ ꜱüʀᴇꜱɪ:** `{uptime}`\n"
        f"• **ʙᴀşʟᴀɴɢıç ​​ꜱᴀᴀᴛɪ:** `{START_TIME_ISO}`"
    )
