# Copyright (c) 2021 CALLMEVP
# Part of: Macha-Userbot
import asyncio

from pyrogram import idle
from Macha import MACHAUB
from Macha-UB.modules import *
from Macha-UB.core.startup_checks import check_or_set_log_channel
from Macha-UB.core.machaub_database.machaub_db_conf import get_log_channel
from config import Config


async def main_startup():
    print("""
|| ϻѧϲʜѧ υ𝒔ᴇʀʙο𝞽 ||
Copyright (c) 2021 ϲѧււϻᴇ𝘃ᴩ
"""
    )
    await MACHAUB.start()
    await check_or_set_log_channel()
    log_channel_id = await get_log_channel()
    await MACHAUB.send_message(chat_id=log_channel_id, text="`ϻѧϲʜѧ υ𝒔ᴇʀʙο𝞽 ɪ𝒔 𝒔𝞽ѧʀ𝞽ᴇᴅ!`")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(main_startup())
