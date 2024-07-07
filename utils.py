from pyrogram import Client
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import utc
from bot import User, Bot


scheduler = AsyncIOScheduler(timezone="UTC")


def delete(user, msg):
    try:
        deleted = await user.delete_messages((msg.chat.id),(msg.id))
    except Exception as e:
        print(e)


scheduler.start()
