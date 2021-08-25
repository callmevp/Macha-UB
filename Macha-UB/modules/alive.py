# Copyright (c) 2021 CALLMEVP
# Part of: Macha-Userbot
# Credits: Developers Userbot | Macha Userbot

import time
import os
from datetime import datetime
from pyrogram import __version__ as pyrogram_version
from pyrogram.types import Message
from sys import version_info

from Macha-UB import MACHAUB, CMD_HELP, MACHAUB_VERSION, StartTime
from Macha-UB.helpers.pyrogram_help import get_arg
from Macha-UB.core.machaub_database.machaub_db_conf import set_custom_alive_msg, get_custom_alive_msg
from Macha-UB.core.main_cmd import machaub_on_cmd, e_or_r
from Macha-UB.core.startup_checks import check_or_set_log_channel
from config import Config


# Help
CMD_HELP.update(
    {
        "alive": f"""
**Alive,**
  ✘ `alive` - To Check If Your Macha Userbot Alive
  ✘ `ping` - To Check Ping Speed
  ✘ `setalive` - To Set Custom Alive Message
  ✘ `getalive` - To Get 
**Example:**
  ✘ `setalive`,
   ⤷ Send with alive text = `{Config.CMD_PREFIX}setalive This is the alive text`
   ⤷ Reply to a text message with `{Config.CMD_PREFIX}setalive`
"""
    }
)

mod_file = os.path.basename(__file__)

# Get python version
python_version = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"
# Conver time in to readable format
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@machaub_on_cmd(command="alive", modlue=mod_file)
async def pyroalive(_, message: Message):
    uptime = get_readable_time((time.time() - StartTime))
    alive_bef_msg = await e_or_r(machaub_message=message, msg_text="`Processing...`")
    get_alive_msg = await get_custom_alive_msg()
    custom_alive_msg = get_alive_msg if get_alive_msg else "Heya, I'm Using Macha Userbot"
    alive_pic = "cache/MACHUB.png"
    alive_msg = f"""
**{custom_alive_msg}**
**ϻѧϲʜѧ υ𝒔ᴇʀʙο𝞽 ɪ𝒔 ѧւɪ𝘃ᴇ**
    
    **Python Version:** `{python_version}`
    **Pyrogram Version:** `{pyrogram_version}`
    **Macha Userbot Version:** `{MACHAUB_VERSION}`
    **Uptime: `{uptime}`**
**ᴅᴇᴩւο𝞬 ουʀ ο𝐰ɴ: @MACHA_USERBOT**"""
    await alive_bef_msg.delete()
    await MACHAUB.send_photo(chat_id=message.chat.id, photo=alive_pic, caption=alive_msg)

@machaub_on_cmd(command="ping", modlue=mod_file)
async def pingme(_, message: Message):
    start = datetime.now()
    end = datetime.now()
    ping_time = (end - start).microseconds / 1000
    ping_msg = await e_or_r(machaub_message=message, msg_text="`Processing...`")
    await e_or_r(machaub_message=message, msg_text=f"**Pong:** `{ping_time} ms`", disable_web_page_preview=True)

@machaub_on_cmd(command="setalive", modlue=mod_file)
async def pyroalive(_, message: Message):
    alive_r_msg = await e_or_r(machaub_message=message, msg_text="`Processing...`")
    c_alive_msg = get_arg(message)
    r_msg = message.reply_to_message
    if not c_alive_msg:
        if r_msg:
            c_alive_msg = r_msg.text
        else:
            await e_or_r(machaub_message=message, msg_text="`Please reply to a text message!`")
            return
    await set_custom_alive_msg(a_text=c_alive_msg)
    await e_or_r(machaub_message=message, msg_text="`Successfully Updated Custom Alive Message!`")

@machaub_on_cmd(command="getalive", modlue=mod_file)
async def pyroalive(_, message: Message):
    g_alive_msg = await e_or_r(machaub_message=message, msg_text="`Processing...`")
    try:
        get_al = await get_custom_alive_msg()
        saved_alive_msg = get_al if get_al else "No Custom Message is saved!"
        await g_alive_msg.edit(f"**Current Alive Message:** \n{get_al}")
    except Exception as e:
        print(e)

@machaub_on_cmd(command="clc", modlue=mod_file)
async def pyroalive(_, message: Message):
    clc_func = await check_or_set_log_channel()
    lc_id = clc_func[1] if clc_func[1]  else None
    await e_or_r(machaub_message=message, msg_text=f"**Is Log Channel Set?** `{clc_func[0]}` \n**Channel ID:** `{lc_id}`")
