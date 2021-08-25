# Copyright (c) 2021 CALLMEVP
# Part of: Macha-Userbot

import asyncio
import tgcrypto
from pyrogram import Client

print("""
|| ϻѧϲʜѧ υ𝒔ᴇʀʙο𝞽 ||
Copyright (c) 2021 CALLMEVP
""")

async def pyro_str():
    print("\nPlease Enter All Required Values to Generate Pyrogram String Session for your Account! \n")
    api_id = int(input("Enter Your APP ID: "))
    api_hash = input("Enter Your API HASH: ")
    async with Client(":memory:", api_id, api_hash) as MACHAUB:
        pyro_session = await MACHAUB.export_session_string()
        session_msg = await MACHAUB.send_message("me", f"`{pyro_session}`")
        await session_msg.reply_text("Successfully Generated String Session! Thanks for trying [Macha Userbot](https://github.com/callmevp/,acha-UB) \n\n**Join @Macha_Userbot**", disable_web_page_preview=True)
        print("\nString Session has been sent to your saved messages. Please check it. Thank You!\n")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(pyro_str())
