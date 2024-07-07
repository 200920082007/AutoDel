import asyncio
from os import environ
from pyrogram import Client, filters, idle, enums
from datetime import datetime, timedelta
from utils import scheduler
from pytz import utc


API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
GRP = int(environ.get("GRP"))
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))



START_MSG = """<b>Hai {},\nI'm a simple bot to delete group messages after a specific time</b>
if You want To Set This Bot To Your Group Tell <a href='https://t.me/abhisheksvlog'>༒ᶜʳᵃᶻʸᴮᴼˢˢ卂乃卄丨丂卄乇Ҝ༒</a>
For PAID!"""


User = Client("sflixrunner",
              api_id=API_ID,
              api_hash=API_HASH, 
              session_string=SESSION)

Bot = Client(name="sflixrunner",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))
    
@User.on_message(filters.chat(GRP))
async def delete(user, message):
    try:
        msg = message
        chat_id = msg.chat.id
        admkns = user.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS)
        for admin in admkns:
            if msg.from_user.id == admin.user.id:
             return
                
        await scheduler.add_job(
            lete,
            "date",
            [user, msg],
            run_date=datetime.now() + timedelta(seconds=TIME),
        )
    except Exception as e:
        print(e)



User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
