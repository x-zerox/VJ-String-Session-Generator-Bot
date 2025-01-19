from flask import Flask
from config import API_ID, API_HASH, BOT_TOKEN, PORT
from pyrogram import Client, idle

app = Flask(__name__)

# Initialize the Pyrogram Client
bot = Client(
    "Anonymous",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="TechVJ"),
)

@app.route('/')
def health_check():
    return "Bot is running!", 200

if __name__ == "__main__":
    # Start the bot
    bot.start()
    
    # Print the bot's username
    uname = bot.get_me().username
    print(f"@{uname} Started Successfully. Made By @VJ_Botz 🤗")
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=PORT)

    # Use idle to keep the bot running
    idle()
    
    # Stop the bot when done
    bot.stop()
    print("Bot Stopped Bye!")
