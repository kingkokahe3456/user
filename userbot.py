from telethon import TelegramClient, events
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import User
from telethon.errors import (
    UserAlreadyParticipantError,
    InviteHashExpiredError,
    InviteHashInvalidError,
    ChannelPrivateError,
    FloodWaitError
)
from collections import defaultdict
import time
api_id = 34707349                         
api_hash = "db4dc97b21c25de284f3a7d4ade65755"            
session_name = 'king_userbot'
OWNER_ID = 8615180080                      
BOT_TOKENS = [
"9226373020:AAGKhy6nR5dKm_411cJVnUgXR952JYAwST8",    
]

MAX_JOINS = 15                            
client = TelegramClient(session_name, api_id, api_hash)
sudo_users = set()
joined_chats = set()
flood_tracker = defaultdict(list)

def is_owner(user_id: int) -> bool:
    return user_id == OWNER_ID

def is_sudo(user_id: int) -> bool:
    return user_id in sudo_users or is_owner(user_id)

async def check_sudo(event):
    if is_sudo(event.sender_id):
        return True
    await event.reply("𝙆𝙄𝙉𝙂 𝙆𝙊 𝘽𝘼𝘼𝙋 𝘽𝘼𝙉𝘼 𝙈𝘼𝘿𝘼𝙍𝘾𝙃𝙊𝘿 🗿")
    return False
@client.on(events.NewMessage(incoming=True))
async def flood_detector(event):
    if event.sender_id is None:
        return

    user_id = event.sender_id
    current_time = time.time()
    flood_tracker[user_id] = [
        t for t in flood_tracker[user_id]
        if current_time - t < 1
    ]

    # Agar pehle se 6 messages ho chuke hain to block
    if len(flood_tracker[user_id]) >= 6:
        try:
            await event.delete()
            await event.reply("⚠️ Flood! ")
        except:
            pass
        return

    flood_tracker[user_id].append(current_time)

# ====================== NORMAL COMMANDS ======================
@client.on(events.NewMessage(pattern=r'(?i)^!start$'))
async def start_handler(event):
    if not await check_sudo(event):
        return
    await event.reply("𝙆𝙄𝙉𝙂 𝘼𝘽𝘽𝙐 𝘼𝙂𝘼𝙔𝙀 💀")

@client.on(events.NewMessage(pattern=r'(?i)^!menu$'))
async def menu_handler(event):
    if not await check_sudo(event):
        return

    menu_text = """𝙆𝙄𝙉𝙂 𝙐𝙇𝙏𝙍𝘼 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 𝙈𝙀𝙉𝙐 ~

╭━━━「 𝘽𝘼𝙎𝙄𝘾 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 」━━━╮
┃
┣➤ !start  ~  𝙎𝙩𝙖𝙧𝙩 𝙩𝙝𝙚 𝙗𝙤𝙩
┣➤ !ping  ~  𝙋𝙞𝙣𝙜 𝙋𝙤𝙣𝙜
┣➤ !menu  ~  𝙊𝙥𝙚𝙣 𝙢𝙚𝙣𝙪
┃
╰━━━━━━━━━━━━━━━━━━╯

╭━━━「 𝙎𝙇𝙄𝘿𝙀 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 」━━━╮
┃
┣➤ !slide  ~  𝙁𝙖𝙨𝙩 𝙎𝙡𝙞𝙙𝙚
┣➤ !reply  ~  𝙍𝙚𝙥𝙡𝙮
┣➤ !lockreply  ~  𝙍𝙚𝙥𝙡𝙮 𝙖𝙩 𝙋𝙖𝙧𝙩𝙞𝙘𝙪𝙡𝙖𝙧 𝙐𝙨𝙚𝙧
┣➤ !rspam  ~  𝙏𝙖𝙧𝙜𝙚𝙩𝙚𝙙 𝙎𝙥𝙖𝙢
┣➤ !drspam  ~  𝙎𝙩𝙤𝙥 𝙏𝙖𝙧𝙜𝙚𝙩𝙚𝙙 𝙎𝙥𝙖𝙢
┣➤ !dreply  ~  𝙎𝙩𝙤𝙥 𝙍𝙚𝙥𝙡𝙮
┣➤ !dlr  ~  𝙎𝙩𝙤𝙥 𝙇𝙤𝙘𝙠 𝙍𝙚𝙥𝙡𝙮
┃
╰━━━━━━━━━━━━━━━━━━╯

╭━━━「 𝙎𝙋𝘼𝙈 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 」━━━╮
┃
┣➤ !spam  ~  𝙎𝙥𝙖𝙢 𝙂𝙞𝙫𝙚𝙣 𝙏𝙚𝙭𝙩
┃
╰━━━━━━━━━━━━━━━━━━╯

╭━━━「 𝘼𝘿𝙈𝙄𝙉 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎 」━━━╮
┃
┣➤ !sudo  ~  𝘼𝙪𝙩𝙝
┣➤ !delsudo  ~  𝙍𝙚𝙢𝙤𝙫𝙚 𝘼𝙪𝙩𝙝
┣➤ !refresh  ~  𝙍𝙚𝙨𝙩𝙖𝙧𝙩 𝘽𝙤𝙩
┣➤ !join < link >  ~  𝙅𝙤𝙞𝙣 𝙂𝙧𝙤𝙪𝙥
┣➤ !mute  ~  𝙈𝙪𝙩𝙚 𝙐𝙨𝙚𝙧
┣➤ !unmute  ~  𝙐𝙣𝙢𝙪𝙩𝙚 𝙐𝙨𝙚𝙧
┣➤ !clone  ~  𝘾𝙡𝙤𝙣𝙚 𝙐𝙨𝙚𝙧
┣➤ !id  ~  𝘾𝙝𝙖𝙩 𝙄𝘿
┣➤ !lock  ~  𝙇𝙤𝙘𝙠 𝙂𝙧𝙤𝙪𝙥
┣➤ !unlock  ~  𝙐𝙣𝙡𝙤𝙘𝙠 𝙂𝙧𝙤𝙪𝙥
┣➤ !dall  ~  𝙎𝙩𝙤𝙥 𝘼𝙡𝙡 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨
┣➤ !speed  ~  𝘼𝙙𝙟𝙪𝙨𝙩 𝙎𝙥𝙚𝙚𝙙
┃
╰━━━━━━━━━━━━━━━━━━╯

♡ 𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙆𝙄𝙉𝙂 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ~"""
    await event.reply(menu_text)

@client.on(events.NewMessage(pattern=r'(?i)^!ping$'))
async def ping_handler(event):
    if not await check_sudo(event):
        return
    await event.reply("Pong! ⚡")

@client.on(events.NewMessage(pattern=r'(?i)^!refresh$'))
async def refresh_handler(event):
    if not await check_sudo(event):
        return
    await event.reply("Refreshed successfully ✅")

# ====================== SUDO SYSTEM ======================
@client.on(events.NewMessage(pattern=r'(?i)^!sudo$'))
async def sudo_handler(event):
    if not is_owner(event.sender_id):
        await event.reply("you are not sudo")
        return

    if not event.is_reply:
        await event.reply("Reply to a user to give sudo!")
        return

    reply_msg = await event.get_reply_message()
    user = await reply_msg.get_sender()

    if not isinstance(user, User):
        await event.reply("Can only give sudo to users.")
        return

    if is_owner(user.id):
        await event.reply("Owner already has full access.")
        return

    if user.id in sudo_users:
        await event.reply(f"{user.first_name} is already a sudo user.")
        return

    sudo_users.add(user.id)
    await event.reply(f"✅ Sudo given to **{user.first_name}** (`{user.id}`)")

@client.on(events.NewMessage(pattern=r'(?i)^!delsudo$'))
async def delsudo_handler(event):
    if not is_owner(event.sender_id):
        await event.reply("you are not sudo")
        return

    if not event.is_reply:
        await event.reply("Reply to a user to remove sudo!")
        return

    reply_msg = await event.get_reply_message()
    user = await reply_msg.get_sender()

    if not isinstance(user, User):
        await event.reply("Can only remove sudo from users.")
        return

    if user.id not in sudo_users:
        await event.reply(f"{user.first_name} is not a sudo user.")
        return

    sudo_users.discard(user.id)
    await event.reply(f"❌ Sudo removed from **{user.first_name}** (`{user.id}`)")

# ====================== JOIN BOT SYSTEM ======================
@client.on(events.NewMessage(pattern=r'(?i)^!joinbot(?:\s+(.+))?$'))
async def joinbot_handler(event):
    if not await check_sudo(event):
        return

    if len(joined_chats) >= MAX_JOINS:
        await event.reply(f"❌ Join limit reached! Maximum {MAX_JOINS} allowed.")
        return

    link = event.pattern_match.group(1)
    if not link:
        await event.reply("Usage: `!joinbot <invite_link>`")
        return

    link = link.strip()
    success = 0
    failed = 0

    for token in BOT_TOKENS:
        bot = None
        try:
            bot = TelegramClient(f"bot_{token[:8]}", api_id, api_hash)
            await bot.start(bot_token=token)

            if "joinchat/" in link or "/+" in link:
                invite_hash = link.split("/")[-1].replace("+", "")
                result = await bot(ImportChatInviteRequest(invite_hash))
            else:
                username = link.split("/")[-1]
                result = await bot(JoinChannelRequest(username))

            chat = result.chats[0]
            joined_chats.add(chat.id)
            success += 1

        except UserAlreadyParticipantError:
            success += 1
        except Exception:
            failed += 1
        finally:
            if bot:
                await bot.disconnect()

    await event.reply(
        f"✅ Join Process Complete\n"
        f"Successful: {success}\n"
        f"Failed: {failed}\n"
        f"Total Joined: {len(joined_chats)}/{MAX_JOINS}"
    )

# ====================== START ======================
async def main():
    print("Starting King Ultra Userbot...")
    await client.start()
    me = await client.get_me()
    print(f"Logged in as: {me.first_name} ({me.id})")
    print("Userbot is running...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())