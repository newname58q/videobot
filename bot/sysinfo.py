# Copyright (C) 2021 Veez Project

import platform
import re
import socket
import uuid

import psutil
from pyrogram import Client, filters
from config import Veez
from helpers.decorators import sudo_users_only, humanbytes
from helpers.filters import command


# FETCH SYSINFO

@Client.on_message(command(["sysinfo", f"sysinfo@{Veez.BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def give_sysinfo(client, message):
    splatform = platform.system()
    platform_release = platform.release()
    platform_version = platform.version()
    architecture = platform.machine()
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    processor = platform.processor()
    ram = humanbytes(round(psutil.virtual_memory().total))
    cpu_freq = psutil.cpu_freq().current
    if cpu_freq >= 1000:
        cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
    else:
        cpu_freq = f"{round(cpu_freq, 2)}MHz"
    du = psutil.disk_usage(client.workdir)
    psutil.disk_io_counters()
    disk = f"{humanbytes(du.used)} / {humanbytes(du.total)} " f"({du.percent}%)"
    cpu_len = len(psutil.Process().cpu_affinity())
    somsg = f"""**🖥 SYSTEM INFO**
    
**ᴘʟᴀᴛꜰᴏʀᴍ :** `{splatform}`
**ᴘʟᴀᴛꜰᴏʀᴍ - ꜱüʀüᴍ :** `{platform_release}`
**ᴘʟᴀᴛꜰᴏʀᴍ - ꜱüʀüᴍ :** `{platform_version}`
**ᴍɪᴍᴀʀɪ :** `{architecture}`
**ᴀɴᴀ ʙɪʟɢɪꜱᴀʏᴀʀ ᴀᴅı :** `{hostname}`
**ɪᴘ :** `{ip_address}`
**ᴍᴀᴄ :** `{mac_address}`
**İşʟᴇᴍᴄɪ :** `{processor}`
**ʀᴀᴍ : ** `{ram}`
**ᴄᴘᴜ :** `{cpu_len}`
**ᴄᴘᴜ ꜰʀᴇᴋ :** `{cpu_freq}`
**ᴅɪꜱᴋ :** `{disk}`
    """
    await message.reply(somsg)
