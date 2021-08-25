# Copyright (c) 2021 CALLMEVP
# Part of: Macha-Userbot

from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

mongodb = AsyncIOMotorClient(Config.MONGODB_URL)
macha_mongodb = mongodb["MACHAUB"]
