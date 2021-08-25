# Copyright (c) 2021 CALLMEVP
# Part of: Macha-Userbot
# Credits: Friday Userbot | DevsExpo
import os
from pyrogram.types import Message

from Macha-UB import MACHAUB, CMD_HELP
from Macha-UB.helpers.pictool_help import gib_carbon_sar
from Macha-UB.helpers.pyrogram_help import get_arg
from Macha-UB.core.main_cmd import machaub_on_cmd, e_or_r
from config import Config


# Help
CMD_HELP.update(
    {
        "pictools": f"""
**Picure Tools**
  ✘ `carbon` - To Carbonize a text
**Example:**
  ✘ `carbon`,
   ⤷ Send command with text to make a carbon = `{Config.CMD_PREFIX}carbon Carbon Text`
   ⤷ Reply to a text message to carbon it = `{Config.CMD_PREFIX}carbon` (Reply to a text message)
"""
    }
)

mod_file = os.path.basename(__file__)

# Carbon a text
@machaub_on_cmd(command="carbon", modlue=mod_file)
async def gibcarbon(_, message: Message):
    r_msg = message.reply_to_message
    carbon_msg = await e_or_r(machaub_message=message, msg_text="`Processing...`")
    carbonpic_msg = get_arg(message)
    if not carbonpic_msg:
        if not r_msg:
            await carbon_msg.edit("`Reply to a Text Message Lol!`")
            return
        if not r_msg.text:
            await carbon_msg.edit("`Reply to a Text Message Lol!`")
            return
        else:
            carbonpic_msg = r_msg.text
    carboned_pic = await gib_carbon_sar(carbonpic_msg)
    await carbon_msg.edit("`Uploading...`")
    await MACHAUB.send_photo(message.chat.id, carboned_pic)
    await carbon_msg.delete()
    carboned_pic.close()
