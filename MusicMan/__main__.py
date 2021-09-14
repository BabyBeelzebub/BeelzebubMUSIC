
import requests
from pyrogram import Client as Bot

from MusicMan.config import API_HASH
from MusicMan.config import API_ID
from MusicMan.config import BG_IMAGE
from MusicMan.config import BOT_TOKEN
from MusicMan.services.callsmusic import run

response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)
bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="MusicMan.modules"),
)

bot.start()
run()
