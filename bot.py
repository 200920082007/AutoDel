import asyncio
from os import environ
from pyrogram import Client, filters, idle, enums
from datetime import datetime, timedelta
from pytz import utc

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
GRP = int(environ.get("GRP"))

class MyClient(Client):

    def __init__(self, name_, bot_token=None, session_string=None):
        super().__init__(
            name=name_,
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION,
            plugins={"root": "plugin"},
            sleep_threshold=5,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username if me.username else ""
        self.myid = me.id
        print(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")
    
    
User = MyClient(name_="sflixrunnerr",
               session_string=SESSION
                  )
