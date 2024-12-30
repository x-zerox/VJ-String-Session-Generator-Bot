from config import API_ID, API_HASH, BOT_TOKEN
from pyrogram import Client, idle

app = Client(
    "Anonymous",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="TechVJ"),
)

if __name__ == "__main__":
    app.start()
    uname = app.get_me().username
    print(f"@{uname} Started Successfully. Made By @VJ_Botz 🤗")
    idle()
    app.stop()
    print("Bot Stopped Bye !")
