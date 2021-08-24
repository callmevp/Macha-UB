# Copyright (c) 2021 CALLMEVP
# Part of: Macha-Userbot

from . import macha_mongodb

machaub_conf = macha_mongodb["config_db"]

# Database for log channel
async def set_log_channel(tgcc_id):
    log_chanel_id = tgcc_id
    p_log_c_id = await machaub_conf.find_one({"_id": "LOG_CHANNEL_ID"})
    if p_log_c_id:
        return True
    else:
        await machaub_conf.insert_one({"_id": "LOG_CHANNEL_ID", "machaub_conf": log_chanel_id})

async def get_log_channel():
    log_channel = await machaub_conf.find_one({"_id": "LOG_CHANNEL_ID"})
    if log_channel:
        return int(log_channel["machaub_conf"])
    else:
        return None

# Database for custom alive message

async def set_custom_alive_msg(a_text=None):
    if a_text is None:
        alive_msg = "ʜᴇ𝞬ѧ, ɪ᾽ϻ υ𝒔ɪɴɢ ϻѧϲʜѧ υ𝒔ᴇʀʙο𝞽"
    else:
        alive_msg = a_text
    p_alive_msg = await machaub_conf.find_one({"_id": "CUSTOM_ALIVE_MSG"})
    if p_alive_msg:
        await machaub_conf.update_one({"_id": "CUSTOM_ALIVE_MSG"}, {"$set": {"machaub_conf": alive_msg}})
    else:
        await machaub_conf.insert_one({"_id": "CUSTOM_ALIVE_MSG", "machaub_conf": alive_msg})

async def get_custom_alive_msg():
    alive_msg = await machaub_conf.find_one({"_id": "CUSTOM_ALIVE_MSG"})
    if alive_msg:
        return alive_msg["machaub_conf"]
    else:
        return None

# Databse for set cutom variable
async def set_custom_var(var, value):
    p_variable = await machaub_conf.find_one({"_id": var})
    if p_variable:
        await machaub_conf.update_one({"_id": var}, {"$set": {"machaub_conf": value}})
    else:
        await machaub_conf.insert_one({"_id": var, "machaub_conf": value})

async def get_custom_var(var):
    custom_var = await machaub_conf.find_one({"_id": var})
    if not custom_var:
        return None
    else:
        g_custom_var = custom_var["machaub_conf"]
        return g_custom_var
