import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7373486317").split()))

API_ID = int(os.getenv("API_ID", "12250297"))

API_HASH = os.getenv("API_HASH", "b51b5dfc5e5f90a7a05e07d874981ddd")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7919784798:AAHCH9F32Jiuzb88GOhED5VKNeyMFCYVj6A")

OWNER_ID = int(os.getenv("OWNER_ID", "7373486317"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002419662880").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Ipanndongok:Ipanndongok@ipanndongok.bg7xf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002419662880"))
