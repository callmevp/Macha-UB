# Copyright (c) 2021 CALLMEVP
# Part of: Macha-Userbot

import os
import importlib
import logging

from pyrogram.types import Message
from Macha-UB import MACHAUB, CMD_HELP
from config import Config
from Macha-UB.core.main_cmd import machaub_on_cmd, e_or_r


# Help
CMD_HELP.update(
    {
        "installer": f"""
**Plugin Installler,**
  ✘ `install` - To Install a Plugin
**Example:**
  ✘ `install`
   ⤷ Reply to pyrogram module made by Macha UB Author with `{Config.CMD_PREFIX}install`
**Note:** `All Official Plugins are available at` **@MachaSupport**! `Please don't install unofficial Plugins!`
"""
    }
)

mod_file = os.path.basename(__file__)

# Load Plugins | Thanks for Friday Userbot for the idea
def import_plugin(p_name):
    macha_plugin_path = "Macha-UB.modules." + p_name
    importlib.import_module(macha_plugin_path)
    logging.info(f"LOADED PLUGIN: - {p_name} - Macha-Userbot")


@machaub_on_cmd(command="install", modlue=mod_file)
async def install_plugin(_, message: Message):
    msg = await e_or_r(machaub_message=message, msg_text="`Processing...`")
    replied_msg = message.reply_to_message
    if not replied_msg:
        await msg.edit("`Please reply to a valid python module to install!`")
        return
    if not replied_msg.document:
        await msg.edit("`Please reply to a valid python module to install!`")
        return
    plugin_name = replied_msg.document.file_name
    plugin_path = f"Macha-ub/modules/{plugin_name}"
    plugin_extension = plugin_name.split(".")[1].lower()
    plugin_name_no_exe = plugin_name.split(".")[0]
    if plugin_extension != "py":
        await msg.edit("`This file isn't a python file`")
        return
    if os.path.isfile(plugin_path):
        await msg.edit("`Plugin already installed!`")
        return
    await replied_msg.download(file_name=plugin_path)
    try:
        await msg.edit("`Loading Plugin, Please wait...`")
        import_plugin(plugin_name_no_exe)
        await msg.edit(f"**Successfully Loaded Plugin** \n\n** ✗ Plugin Name:** `{plugin_name_no_exe}`")
    except Exception as e:
        await msg.edit(f"**Error:** {e}")
