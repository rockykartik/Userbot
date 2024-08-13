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


API_ID = int(getenv("API_ID", "28589698"))
API_HASH = getenv("API_HASH", "685e4dbee2d31c84bfdee1ce11a21992")
BOT_TOKEN = getenv("BOT_TOKEN", "6744138580:AAEr9_L9tu4T1xES_NCaHuf1RQP8Wn__LXc")
STRING_SESSION = getenv("STRING_SESSION", "BQG0PoIArxLlJtKaJKFnvwPXRDjvl0FP2GEepAZkbvF7MAlcaW_kWtXBUAT8jv340lMf-O4qytsORW-Z2R3DSk1uftzhQ-m39p70YIfUagWjlH9zbsFCalxgk5z9-Cmd-Z4ejnrpJmjBovw2N4FBCMsqR0eWwgzt4-yTXhE6VlbmJL_TKc4TH0J0OWg-Lkx_0nL2A7ADR3kRCSSZ2y58RSFmR2kWYKiz0VSAP3DNIVO_ULukgV16sj9Z7P0_cPOMlNuprQPgMs8L7oBJPQwsI5Uy0ehI8BkXz7RoZcN2GxmnKFS1lQ3gZXwb8uO_MKwJ_WfX6WkpYJ7DYDKvuJ_QBBZPp7VHvgAAAAFnztpJAA")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Chiku12:Chiku12@arman.wsumgkn.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002241501912"))



SESSION_STRING = getenv("SESSION_STRING", "BQG0PoIArxLlJtKaJKFnvwPXRDjvl0FP2GEepAZkbvF7MAlcaW_kWtXBUAT8jv340lMf-O4qytsORW-Z2R3DSk1uftzhQ-m39p70YIfUagWjlH9zbsFCalxgk5z9-Cmd-Z4ejnrpJmjBovw2N4FBCMsqR0eWwgzt4-yTXhE6VlbmJL_TKc4TH0J0OWg-Lkx_0nL2A7ADR3kRCSSZ2y58RSFmR2kWYKiz0VSAP3DNIVO_ULukgV16sj9Z7P0_cPOMlNuprQPgMs8L7oBJPQwsI5Uy0ehI8BkXz7RoZcN2GxmnKFS1lQ3gZXwb8uO_MKwJ_WfX6WkpYJ7DYDKvuJ_QBBZPp7VHvgAAAAFnztpJAA")
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

