# Copyright (c) 2021 CALLMEVP
# Part of: Macha-Userbot

from . import macha_mongodb

machaub_gban = macha_mongodb["gban_db"]

# Database for storing gban details
async def gban_usr(gban_id, gban_reason="Abusing People!"):
    gban_user_id = int(gban_id)
    p_gbanned = await machaub_gban.find_one({"gbanned_usr": gban_user_id})
    if p_gbanned:
        return True
    else:
        await machaub_gban.insert_one({"gbanned_usr": gban_user_id, "reason_for_gban": gban_reason})

# Get gbanned user list
# Credits: Friday Userbot
async def get_gbanned():
    return [gban_usrs async for gban_usrs in machaub_gban.find({})]

# Get gbaned reason
async def get_gban_reason(gban_id):
    gban_user_id = int(gban_id)
    pr_gbanned = await machaub_gban.find_one({"gbanned_usr": gban_user_id})
    if pr_gbanned:
        return pr_gbanned["reason_for_gban"]
    else:
        return None

# Ungban a user
async def ungban_usr(gban_id):
    gban_user_id = int(gban_id)
    alr_gbanned = await machaub_gban.find_one({"gbanned_usr": gban_user_id})
    if alr_gbanned:
        await machaub_gban.delete_one({"gbanned_usr": gban_user_id})
    else:
        return False
