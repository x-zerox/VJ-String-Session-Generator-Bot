from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://telegra.ph/file/5c586e00f34665267ab5b.jpg",  # Replace with the URL of your image
        caption=f"""<b>𝐇𝐞𝐲 {msg.from_user.mention}🍷,

ɪ ᴀᴍ {me2},
ᴛʀᴜsᴛᴇᴅ 𝗦𝗧𝗥𝗜𝗡𝗚 𝗚𝗥𝗡𝗘𝗥𝗔𝗧𝗢𝗥 ʙᴏᴛ.ғᴜʟʟʏ sᴀғᴇ & sᴇᴄᴜʀᴇ.
ɴᴏ ᴀɴʏ ᴇʀʀᴏʀ

Create Your Own Bot By Using 
/clone `yourbottoken`

Deleting Your Clone Bot By Using
/deletecloned `yourbottoken`

Made With By : [VJ Botz](https://t.me/VJ_Botz) !</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⚡Generate String⚡", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("❣️ Support Group ❣️", url="https://t.me/VJ_Bot_Disscussion"),
                    InlineKeyboardButton("🥀 Update Channel 🥀", url="https://t.me/VJ_Botz")
                ]
            ]
        )
    )
