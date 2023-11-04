from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "24942531"))
API_HASH = getenv("API_HASH", "018f82cf994bd252038e9739fd68ba44")

BOT_TOKEN = getenv("BOT_TOKEN", "6786394544:AAEN5cjPGj_Ii4uYDLGWjEXAJzPDOuzD5JM")
OWNER_ID = int(getenv("OWNER_ID", "6366990600"))

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Forward123:Forward123@cluster0.4d1ljfv.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", "VJ_Botz")
