from pyrogram import Client
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import utc


scheduler = AsyncIOScheduler(timezone="UTC")
