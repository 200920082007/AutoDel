from pyrogram import idle
from plugin import User

async def startBot():
    await User.start()
    await idle()
    await User.stop()

User.run(startBot())
