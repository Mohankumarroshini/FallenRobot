import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from FallenRobot.events import register
from FallenRobot import telethn as tbot, SUPPORT_CHAT, OWNER_USERNAME, dispatcher


PHOTO = [
       "https://telegra.ph/file/0c63efafefa0a214d8df8.jpg".

"https://telegra.ph/file/0a020df4a384b96462559.jpg",

"https://telegra.ph/file/4b5abc8970bc2bc282040.jpg",

"https://telegra.ph/file/6a420caf4e279ed68b7ea.jpg",

"https://telegra.ph/file/3b155e569ee34f6be90c2.jpg",

"https://telegra.ph/file/f75ebb454c6c8993fef9e.jpg",

"https://telegra.ph/file/a67dc5bce8e4cc4552064.jpg",

"https://telegra.ph/file/f24142a097b9a877cad42.jpg",

"https://telegra.ph/file/339d6bf3f0b05f3b13123.jpg",

]


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ {dispatcher.bot.first_name}**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [எம்.எஸ்.டி🇮🇳](https://t.me/{OWNER_USERNAME})** \n\n"
    TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
    TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", f"https://t.me/{dispatcher.bot.username}?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


__mod_name__ = "Aʟɪᴠᴇ"
