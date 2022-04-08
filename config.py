from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
SESSION_NAME = getenv("SESSION_NAME", "session")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME")
ALIVE_NAME = getenv("ALIVE_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/LOGI-TECH/MUSIC")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "music")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "logi_channel")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "logi_channel")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/1f87eb5d6c3fa1c2090e6.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/03e6088e20ef94ad78847.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/76a73c8c740622076bd12.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/45189008a90b9cf8bf4e4.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/63300139d232dc12452ab.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/2fc8882813e32c8f90e08.jpg")
