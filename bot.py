
API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
GRP = int(environ.get("GRP"))




User = Client("sflixrunner",
              api_id=API_ID,
              api_hash=API_HASH, 
              session_string=SESSION,
              plugins=dict(root=plugin))


User.start()
print("User Started!")

idle()

User.stop()
print("User Stopped!")
