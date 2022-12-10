from pyrogram import Client, filters
from pyrogram.types import Message

from gezet.modules.help import add_command_help


@Client.on_message(filters.command("create", ".") & filters.me)
async def create(client: Client, message: Message):
    if len(message.command) < 3:
        return await message.edit_text(
            message, f"**Ketik .help create jika Anda membutuhkan bantuan**"
        )
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.edit_text("`Processing...`")
    desc = "Selamat datang ke " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "gc":  # for supergroup
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id["id"])
        await xd.edit(
            f"**Berhasil Membuat Grup Telegram: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )
    elif group_type == "ch":  # for channel
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id["id"])
        await xd.edit(
            f"**Berhasil Membuat Saluran Telegram: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )


add_command_help(
    "create",
    [
        ["create ch", "membuat saluran"],
        ["create gc", "membuat grup"],
    ],
)
