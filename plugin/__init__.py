import asyncio
from os import environ
from pyrogram import Client, filters, idle, enums, __version__
from pyrogram.raw.all import layer
from datetime import datetime, timedelta
from pytz import utc
from utils import scheduler


API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
GRP = int(environ.get("GRP"))

class MyClient(Client):

    def __init__(self, name_, bot_token=None, session_string=None):
        super().__init__(
            name="sflixrunnerr",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session_string,
            plugins={"root": "plugins"},
            scheduler.start())

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username if me.username else ""
        self.myid = me.id
        scheduler.start()
        print(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")
    
    
User = MyClient(name_="spamBanBot",
                session_string=SESSION
                  )
