# 𝐃𝐎𝐍𝐓 𝐌𝐄𝐒𝐒 𝐖𝐈𝐓𝐇 𝐂𝐎𝐃𝐄𝐒 𝐂𝐎𝐏𝐘𝐑𝐈𝐆𝐇𝐓 @SHAILENDRA34 |
# 𝐃𝐞𝐚𝐫 𝐏𝐞𝐫𝐨 𝐩𝐩𝐥𝐬 𝐏𝐥𝐢𝐬𝐡 𝐃𝐨𝐧'𝐭 𝐫𝐞𝐦𝐨𝐯𝐞 𝐭𝐡𝐢𝐬 𝐥𝐢𝐧𝐞 𝐟𝐫𝐨𝐦 𝐡𝐞𝐫𝐞 🌚


import asyncio
from pyrogram.types import Message
from pyrogram import Client, filters
from helpers.filters import command, other_filters
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import authorized_users_only
from callsmusic.callsmusic import client as user

STR_ID = "CAACAgIAAx0CW9EqKAACEoZiT-Pqtg1RKtr06xxZWMwSAhye2AACghsAAiKAeEqwv4PkzvkmQiME"

@Client.on_message(
    command(["join", "joinassistant", "userbotjoin"]) & ~filters.bot
)
@authorized_users_only
async def join_chat(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invite_link = await m.chat.export_invite_link()
        if "+" in invite_link:
            link_hash = (invite_link.replace("+", "")).split("t.me/")[1]
            await user.join_chat(f"https://t.me/joinchat/{link_hash}")
        await m.chat.promote_member(
            (await user.get_me()).id,
            can_manage_voice_chats=True
        )
        return await user.send_message(chat_id, "ᴀssɪsᴛᴀɴᴛ ᴊᴏɪɴᴇᴅ ᴛʜɪs ɢʀᴏᴜᴘ ɴᴏᴡ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ 💫")
    except UserAlreadyParticipant:
        admin = await m.chat.get_member((await user.get_me()).id)
        if not admin.can_manage_voice_chats:
            await m.chat.promote_member(
                (await user.get_me()).id,
                can_manage_voice_chats=True
            )
            return await user.send_message(chat_id, "🙄 ᴀssɪsᴛᴀɴᴛ ɪᴢ sᴛɪʟʟ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ")
        return await user.send_message(chat_id, "🙄 ᴀssɪsᴛᴀɴᴛ ɪᴢ sᴛɪʟʟ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ")
