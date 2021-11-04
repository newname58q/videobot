# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Veez


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ ʙᴜ ʙᴏᴛᴜ ɴᴀꜱıʟ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀɪᴍ :

1.) ᴠɪᴅᴇᴏ ʏᴀʏɪɴʟᴀᴅɪᴋᴛᴀɴ ꜱᴏɴʀᴀ ʙᴀşᴋᴀ ᴠɪᴅᴇᴏ ʏᴀʏɪɴʟᴀᴍᴀᴋ ɪçɪɴ ʟüᴛꜰᴇɴ /ᴅᴜʀ ᴋᴏᴍᴜᴛᴜɴᴜ ᴋᴜʟʟᴀɴᴅɪᴋᴛᴀɴ ꜱᴏɴʀᴀ ʏᴇɴɪ ᴠɪᴅᴇᴏʏᴜ ʏᴀʏɪɴʟᴀʏɪɴɪᴢ!!!.
2.) öɴᴄᴇ ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇʏɴɪᴢ ꜱᴏɴʀᴀ ʙᴇɴɪ ʏöɴᴇᴛɪᴄɪ ʏᴀᴘ.
3.) @ { Veez . ASSISTANT_NAME  } ɢʀᴜʙᴜɴᴜᴢᴀ.
4.) ᴠɪᴅᴇᴏ ᴀᴋışıɴᴀ ʙᴀşʟᴀᴍᴀᴅᴀɴ öɴᴄᴇ ꜱᴇꜱʟɪ ꜱᴏʜʙᴇᴛɪ ᴀçıɴ.
5.) ʙᴀşʟᴀᴛᴍᴀᴋ ɪçɪɴ /ɪᴢʟᴇᴛ (ᴠɪᴅᴇᴏʏᴀ ʏᴀɴıᴛʟᴀ) ʏᴀᴢıɴ.
6.) ᴠɪᴅᴇᴏ ᴅüᴢᴇɴʟᴇᴍᴇᴋ ɪçɪɴ /ᴅᴜʀ ʏᴀᴢıɴ.

📝 **ɴᴏᴛ: ʙᴜ ʙᴏᴛᴜ ꜱᴀᴅᴇᴄᴇ ɢʀᴜᴘ ᴀᴅᴍɪɴʟᴇʀɪ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀ!**

⚡ __[ᴘᴀʀᴀᴅɪꜱᴇ](https://t.me/jackdanielssx) ᴛᴀʀᴀꜰıɴᴅᴀɴ ɢᴇʟɪşᴛɪʀɪʟᴅɪ__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 geri dön", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"✨ **ᴍᴇʀʜᴀʙᴀ, ʙᴇɴ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴜᴘʟᴀʀɪɴᴅᴀ ᴍüᴢɪᴋ ᴠᴇ ᴠɪᴅᴇᴏ ᴏʏɴᴀᴛᴍᴀᴋ ɪçɪɴ ɢᴇʟɪşᴛɪʀɪʟᴅɪᴍ.**\n\n💭 **ɢʀᴜᴘᴛᴀ ᴠɪᴅᴇᴏ ᴀᴋışı ʏᴀᴘᴍᴀᴋ ɪçɪɴ ʏᴀʀᴀᴛıʟᴅıᴍ "
        f"ᴠɪᴅᴇᴏ ɪᴢʟᴇᴍᴇᴋ ᴠᴇ ᴍüᴢɪᴋ ᴅɪɴʟᴇᴍᴇᴋ ɪçɪɴ.**\n\n❔ **ᴀşᴀɢɪᴅᴀᴋɪ ʙᴜᴛᴏɴᴀ ᴛɪᴋʟᴀʏɪɴɪᴢ** 👇🏻",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "➕ ʙᴇɴɪ ɢʀᴜʙᴜɴᴀ ᴇᴋʟᴇ ➕", url=f"https://t.me/{Veez.BOT_USERNAME}?startgroup=true")
            ], [
                InlineKeyboardButton(
                    "❔ ʙᴜ ʙᴏᴛᴜ ɴᴀꜱıʟ ᴋᴜʟʟᴀɴᴀʙɪʟɪʀɪᴍ", callback_data="cbguide")
            ], [
                InlineKeyboardButton(
                    "🌐 ɢᴇʟɪşᴛɪʀɪᴄɪʟᴇʀ", callback_data="cbinfo")
            ], [
                InlineKeyboardButton(
                    "💬 ɢʀᴜᴘ", url=f"https://t.me/{Veez.GROUP_NAME}"),
                InlineKeyboardButton(
                    "📣 ᴋᴀɴᴀʟ", url=f"https://t.me/{Veez.CHANNEL_NAME}")
            ], [
                InlineKeyboardButton(
                    "🧙🏻‍♂️ ᴄʀᴇᴀᴛᴏʀ", url=f"https://t.me/{Veez.OWNER_NAME}")
            ], [
                InlineKeyboardButton(
                    "📚 Tᴛüᴍ ᴋᴏᴍᴜᴛ ʟɪꜱᴛᴇꜱɪİ", callback_data="cblist")
            ]]
        ))


@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🌐 **ʙᴏᴛ ʙɪʟɢɪꜱɪ !**

🤖 __ʙᴜ ʙᴏᴛ, ᴡᴇʙʀᴛᴄ'ᴅᴇɴ çᴇşɪᴛʟɪ ʏöɴᴛᴇᴍʟᴇʀ ᴋᴜʟʟᴀɴıʟᴀʀᴀᴋ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴜʙᴜ ɢöʀüɴᴛüʟü ꜱᴏʜʙᴇᴛʟᴇʀɪɴᴅᴇ ᴠɪᴅᴇᴏ ᴀᴋışı ʏᴀᴘᴍᴀᴋ ɪçɪɴ ᴏʟᴜşᴛᴜʀᴜʟᴅᴜ.__


👩🏻‍✈️ » [Jack`DaNieL`s](https://t.me/jackdanielssx)
🤵🏻 » [PARADİSE](https://t.me/HzBarbie)

__ʙᴜ ʙᴏᴛ, ɢɴᴜ-ɢᴘʟ 3.0 ʟɪꜱᴀɴꜱı ᴀʟᴛıɴᴅᴀ ʟɪꜱᴀɴꜱʟᴀɴᴍışᴛıʀ.__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 ɢᴇʀɪ", callback_data="cbstart")
            ]]
        ),
        disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cblist"))
async def cblist(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""📚 ᴋᴏᴍᴜᴛ ʟɪꜱᴛᴇꜱɪ:

» /izlet (ɪɴᴅɪʀɪʟᴇɴ ᴠᴇʏᴀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋɪɴɪ ʏᴀɴıᴛʟᴀʏıᴘ ʏᴀᴢıɴ) 
» /dur - ʏᴀʏıɴı ᴅᴜʀᴅᴜʀ
» /ara (şarkı adı) - Şᴀʀᴋı ᴀʀᴀʀ ɪɴᴅɪʀɪʀ ꜱᴀᴅᴇᴄᴇ ʏᴛ
» /bul (video adı) - ᴠɪᴅᴇᴏʏᴜ ᴀʀᴀʀ ɪɴᴅɪʀɪʀ ꜱᴀᴅᴇᴄᴇ ʏᴛ
» /lyric (şarkı adı ) - şᴀʀᴋı ꜱöᴢü ᴀʀᴀʀ
» /gel - ᴀꜱɪꜱᴛᴀɴı ꜱᴏʜʙᴇᴛᴇ ᴅᴀᴠᴇᴛ ᴇᴅᴇʀ


⚡ __ʙᴀᴋıᴍı ᴊᴀᴄᴋᴍᴇᴅʏᴀ ᴇᴋɪʙɪ ᴛᴀʀᴀꜰıɴᴅᴀɴ ʏᴀᴘıʟıʀ__""",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton(
                    "🏡 ɢᴇʀɪ ", callback_data="cbstart")
            ]]
        ))


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
