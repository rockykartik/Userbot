import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", "25609334"))
API_HASH = getenv("API_HASH", "ad0ff353206ea1ebce1ab8bfca9f3f7b")
BOT_TOKEN = getenv("BOT_TOKEN", "6744138580:AAEr9_L9tu4T1xES_NCaHuf1RQP8Wn__LXc")
STRING_SESSION = getenv("STRING_SESSION", "BQFMJkgAdw6SBlZlj3QDdznHidu2hsAvdKDZv0cf8GtaBq1XGU9U-SZKwgQH1gLz7goiTHUwKK-y0hWCQBAvl9-mRJder-_56IjyjYEwiajeaO6BZmGSFhYH5mVNVAM826LmVTXC2cpWj2goFbtTPW_h6PzVn_vX53RRLUcc2vEEG7g22i1ahur6lFjs5A8_rDngRcYQ-sYdoUuosboNtqASUAkQApX7auM_yHjvijorj0oo1GZt3dBTdsWvwKdT8fVbOYGK6f4pnjeUxFwgE82gSQjfuPhjC7vwUdFdw2keQYDoR-nJYcG8eZD8qMBPdvc5_2Lcz7FXfcy4nDTiPNugi17jWQAAAAFC8M17AA")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Chiku12:Chiku12@arman.wsumgkn.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001764180763"))



SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())




PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**Hᴇʏ ᴛʜᴇʀᴇ! I'ᴍ ᴀ ʀᴇᴀʟʟʏ sᴍᴀʀᴛ ᴀɴᴅ ғᴀsᴛ ᴀssɪsᴛᴀɴᴛ ʙᴏᴛ ᴡɪᴛʜ ᴛᴏᴘ-ɴᴏᴛᴄʜ sᴇᴄᴜʀɪᴛʏ.\n I ᴡᴏɴ'ᴛ ʟᴇᴛ ʏᴏᴜ ᴍᴇssᴀɢᴇ ᴍʏ ᴏᴡɴᴇʀ ᴅɪʀᴇᴄᴛʟʏ ᴜɴʟᴇss ᴛʜᴇʏ sᴀʏ ɪᴛ's ᴏᴋᴀʏ. Rɪɢʜᴛ ɴᴏᴡ, ᴍʏ ᴏᴡɴᴇʀ ɪsɴ'ᴛ ᴏɴʟɪɴᴇ, sᴏ ʏᴏᴜ'ʟʟ ʜᴀᴠᴇ ᴛᴏ ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴛʜᴇʏ ɢɪᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ. Aɴᴅ ᴘʟᴇᴀsᴇ, ᴅᴏɴ'ᴛ sᴘᴀᴍ ʜᴇʀᴇ – ɪғ ʏᴏᴜ ᴅᴏ,\n\n I ᴍɪɢʜᴛ ʜᴀᴠᴇ ᴛᴏ ʙʟᴏᴄᴋ ʏᴏᴜ ғʀᴏᴍ ᴄᴏɴᴛᴀᴄᴛɪɴɢ ᴍʏ ᴏᴡɴᴇʀ.**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 5))



USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://te.legra.ph/file/6926207a8c9c4b8e4b93c.jpg")



LOGGER = logging.getLogger("DIL")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

