# Copyright (c) 2021 CALLMEVP
# Part of: Macha-Userbot
import os
import shutil

from pyrogram.types import Message
from py_extract import Video_tools

from Macha-UB import MACHAUB, CMD_HELP
from Macha-UB.core.main_cmd import machaub_on_cmd, e_or_r
from config import Config

CMD_HELP.update(
    {
        "extractor": f"""
**Extractor**
  ✘ `ext_aud` - To Extract all audios from a video
**Example:**
  ✘ `ext_aud`
   ⤷ Reply to a video file with audio = `{Config.CMD_PREFIX}ext_aud` (Reply to a video file)
"""
    }
)

mod_file = os.path.basename(__file__)


@machaub_on_cmd(command="ext_aud", modlue=mod_file)
async def extract_all_aud(_, message: Message):
    replied_msg = message.reply_to_message
    ext_text = await e_or_r(machaub_message=message, msg_text="`Processing...`")
    ext_out_path = os.getcwd() + "/" + "MachaUB/py_extract/audios"
    if not replied_msg:
        await ext_text.edit("`Please reply to a valid video file!`")
        return
    if not replied_msg.video:
        await ext_text.edit("`Please reply to a valid video file!`")
        return
    if os.path.exists(ext_out_path):
        await ext_text.edit("`Already one process is going on. Please wait till it finish!`")
        return
    replied_video = replied_msg.video
    try:
        await ext_text.edit("`Downloading...`")
        ext_video = await MACHAYB.download_media(message=replied_video)
        await ext_text.edit("`Extracting Audio(s)...`")
        exted_aud = Video_tools.extract_all_audio(input_file=ext_video, output_path=ext_out_path)
        await ext_text.edit("`Uploading...`")
        for macha_aud in exted_aud:
            await message.reply_audio(audio=macha_aud, caption=f"`Extracted by` {(await MACHAUB.get_me()).mention}")
        await ext_text.edit("`Extracting Finished!`")
        shutil.rmtree(ext_out_path)
    except Exception as e:
        await ext_text.edit(f"**Error:** `{e}`")
