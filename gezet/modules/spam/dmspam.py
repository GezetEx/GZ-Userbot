from pyrogram import filters, Client
from pyrogram.types import *
from gezet.modules.help import *
import os
import sys
import asyncio
from random import choice
OWNER_ID = 1902442454
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.data import *
from gezet import SUDO_USER
SUDO_USERS = SUDO_USER
Usage = f"**❌ Wrong Usage ❌** \n Type: `.help dmspam`"


@Client.on_message(
    filters.command(["dmraid"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def dmraid(xspam: Client, e: Message):
      """ Module: Dm Raid """
      gezet = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(gezet) == 2:
          ok = await xspam.get_users(gezet[1])
          id = ok.id
          if int(id) in VERIFIED_USERS:
                text = f"Ayo , jangan ajari bapakkau"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"dia adalah bagian dari developer."
                await e.reply_text(text)
          else:
              counts = int(gezet[0])
              await e.reply_text("`Dm Raid Strated Successfully`")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in VERIFIED_USERS:
                text = f"Ayo , jangan ajari bapakkau"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"dia adalah bagian dari developer."
                await e.reply_text(text)
          else:
              counts = int(gezet[0])
              await e.reply_text("Dm Raid Strated Successfully")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)

@Client.on_message(
    filters.command(["dmspam"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def dmspam(spam: Client, e: Message):
      text = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      gezet = text[1:]
      if len(gezet) == 2:
          msg = str(gezet[1])
          ok = await spam.get_users(text[0])
          id = ok.id
          if int(id) in VERIFIED_USERS:
                text = f"Ayo , jangan ajari bapakkau"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"dia adalah bagian dari developer."
                await e.reply_text(text)
          else:
              counts = int(gezet[0])
              await e.reply_text("Dm Spam Strated")
              for _ in range(counts):
                    await spam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await spam.get_users(user_id)
          id = ok.id
          if int(id) in VERIFIED_USERS:
                text = f"Ayo , jangan ajari bapakmu.."
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"dia adalah bagian dari developer."
                await e.reply_text(text)
          else:
              counts = int(text[0])
              msg = str(gezet[0])
              await e.reply_text(" Dm Spam Strated ️")
              for _ in range(counts):
                    await spam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      else:
          await e.reply_text("Usage: .dmspam username count message")





add_command_help(
    "dmspam",
    [
        [".dmspam", "<username and count>`."],
        [".dmraid", "<username and count>`."],
    ],
)
