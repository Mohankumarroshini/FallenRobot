from pyrogram import filters
from pyrogram.types import Message as message
from FallenRobot import bot


@bot.on_message(filters.command("write"))
async def handwriting(_, message):
    if len(message.command) < 2:
        return await message.reply_text("» ʟᴏʟ,, ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴡʀɪᴛᴇ...")
    m = await message.reply_text("» ɪ ᴀᴍ ᴡʀɪᴛɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...")
    name = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    hand = "https://apis.xditya.me/write?text=" + name
    await m.edit("» Uploading...")
    await message.reply_photo(hand, caption="🖊ᴡʀɪᴛᴛᴇɴ ʙʏ @HeraXRoBot")
