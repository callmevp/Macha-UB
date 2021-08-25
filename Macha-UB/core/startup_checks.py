# Copyright (c) 2021 CALLMEVP
# Part of: Macha-Userbot

from Macha-UB import MACHAUB
from Macha-UB.core.machaub_database.machaub_db_conf import set_log_channel, get_log_channel
from config import Config


async def check_or_set_log_channel():
    try:
        log_channel_id = await get_log_channel()
        if log_channel_id:
            return [True, log_channel_id]
        else:
            log_channel = await MACHAUB.create_channel(title="Macha Userbot Logs", description="Logs of your Macha Userbot")
            welcome_to_machaub = f"""
**𝐰ᴇւϲοϻᴇ 𝞽ο ϻѧϲʜѧ υ𝒔ᴇʀʙο𝞽**
𝞽ʜѧɴ𝞳𝒔 ғοʀ 𝞽ʀ𝞬ɪɴɢ ϻѧϲʜѧ υ𝒔ᴇʀʙο𝞽. ɪғ 𝞬ου ғουɴᴅ ѧɴ𝞬 ᴇʀʀοʀ, ʙυɢ οʀ ᴇ𝘃ᴇɴ ѧ ғᴇѧ𝞽υʀᴇ ʀᴇǫυᴇ𝒔𝞽 ᴩւᴇѧ𝒔ᴇ ʀᴇᴩοʀ𝞽 ɪ𝞽 ѧ𝞽  **@MachaSupport**
**⌲ Quick Start,**
ɪғ 𝞬ου ᴅοɴ᾽𝞽 𝞳ɴο𝐰 ʜο𝞽 𝞽ο υ𝒔ᴇ 𝞽ʜɪ𝒔 υ𝒔ᴇʀʙο𝞽 ᴩւᴇѧ𝒔ᴇ 𝒔ᴇɴᴅ  `{Config.CMD_PREFIX}help` ɪɴ ѧɴ𝞬 ϲʜѧ𝞽. ɪ𝞽᾽ււ 𝒔ʜο𝐰 ѧււ ᴩւυɢɪɴ𝒔 𝞬ουʀ υ𝒔ᴇʀʙο𝞽 ʜѧ𝒔. 𝞬ου ϲѧɴ υ𝒔ᴇ 𝞽ʜο𝒔ᴇ ᴩւυɢɪɴ ɴѧϻᴇ𝒔 𝞽ο ɢᴇ𝞽 ɪɴғο ѧʙου𝞽 ʜο𝐰 𝞽ο υ𝒔ᴇ ɪ𝞽
**~ ϻѧϲʜѧ υ𝒔ᴇʀʙο𝞽 ѧυ𝞽ʜοʀ𝒔**"""
            log_channel_id = log_channel.id
            await set_log_channel(log_channel_id)
            await MACHAUB.send_message(chat_id=log_channel_id, text=welcome_to_machaub)
            return [True, log_channel_id]
    except Exception as e:
        print(f"Error \n\n{e} \n\nPlease check all variables and try again! \nReport this with logs at @MachaSupport if the problem persists!")
        exit()
