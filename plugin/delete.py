import asyncio
from os import environ
from bot import User, GRP
from pyrogram import Client, filters, idle, enums
from datetime import datetime, timedelta
from pytz import utc
from utils import scheduler 

@User.on_message(filters.group & filters.text & filters.incoming)
async def delete(user, message):
    if message.chat.id != GRP:
        return
    try:
        msg = message
        chat_id = msg.chat.id
        admkns = user.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS)
        for admin in admkns:
            if msg.from_user.id == admin.user.id:
             return
                
        await scheduler.add_job(
            delete,
            "date",
            [user, msg],
            run_date=datetime.now() + timedelta(seconds=TIME),
        )
    except Exception as e:
        print(e)

async def delete(user, msg):
    try:
        deleted = await user.delete_messages((msg.chat.id),(msg.id))
    except Exception as e:
        print(e)
