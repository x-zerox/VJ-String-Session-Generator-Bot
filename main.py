from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

bot = Client(
    "Anonymous",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="TechVJ"),
)

if __name__ == "__main__":
    bot.start()
    uname = bot.get_me().username
    print(f"@{uname} Started Successfully. Made By @VJ_Botz 🤗")
