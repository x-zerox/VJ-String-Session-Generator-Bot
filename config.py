from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "19134188"))
API_HASH = getenv("API_HASH", "91587601a5d898e3341b7e4a9e1c2537")

BOT_TOKEN = getenv("BOT_TOKEN", "6792003995:AAFVOt0f3tKDO085581YYiCfQF6TEb9r4Zw")
OWNER_ID = int(getenv("OWNER_ID", "6168162777"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Forward123:Forward123@cluster0.4d1ljfv.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "VJ_Botz")
