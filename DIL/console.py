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


API_ID = int(getenv("API_ID", "21767752"))
API_HASH = getenv("API_HASH", "8817c95b20fca899462336cdf36dd958")
BOT_TOKEN = getenv("BOT_TOKEN", "6744138580:AAEr9_L9tu4T1xES_NCaHuf1RQP8Wn__LXc")
STRING_SESSION = getenv("STRING_SESSION", "BQFMJkgAXZNBAJ7MvFrB-P1CKnX5C3KQNYCwHxDI8GnDoAa7EveN_0he8TcHeIO7lYgdaBIaqjQmTbB0Q1rK0QTvniXzeoi3DiHGaukyvEKBVQSt5LD9UZJT8_9gFBZBww5bbhYdLswzI_PXgc6KXRhJThDKwYhuMxgzEI5Tqbt0Lm19PPHDv0QN0yIb8LpGCTXL5_gmgVPj2B2wjk4kslaPWSqAExfY5t0iLOyVd-bn8OfJy4CSST0mPFvKr25w81kBiWf2Jurp6wvmAh17BksgiKP4VGjcUKEwO_VXc1twx7yvCoyyn84oLUi8HFas1FKohAhhbSpTV_9KTmxCt7ufaiMbzQAAAAE5zUGcAA")
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

