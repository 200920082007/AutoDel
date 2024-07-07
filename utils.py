from pyrogram import Client
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import utc
from bot import User, Bot


scheduler = AsyncIOScheduler(timezone="UTC")



scheduler.start()
