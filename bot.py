import time
from telethon import TelegramClient, events, sync
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest

# Your Telegram API credentials
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
session_file = 'YOUR_SESSION_FILE'

# Create a Telegram client with the given API credentials
client = TelegramClient(session_file, api_id, api_hash)

# Send a message to a Telegram group at a given time interval with different messages
@client.on(events.NewMessage(chats='YOUR_GROUP'))
async def send_message(event):
    # Define your messages
    messages = [
        'Hello, everyone!',
        'How are you doing today?',
        'Just wanted to say hi!'
    ]
    # Send a message every 30 seconds
    for message in messages:
        await client.send_message('YOUR_GROUP', message)
        time.sleep(30)

# Auto-reply to personal chats
@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):
    # Define your auto-reply message
    auto_reply_message = 'Thanks for your message! I will get back to you as soon as possible.'
    # Send an auto-reply to all personal chats
    if not event.is_group:
        await client.send_message(event.chat_id, auto_reply_message)

# Auto-change the name and profile picture of your Telegram account at different time intervals
async def change_profile():
    # Define your profile names and profile picture paths
    profile_names = [
        'Name 1',
        'Name 2',
        'Name 3'
    ]
    profile_pics = [
        'path/to/profile/pic1.jpg',
        'path/to/profile/pic2.jpg',
        'path/to/profile/pic3.jpg'
    ]
    # Change your profile every 30 seconds
    while True:
        for i in range(len(profile_names)):
            await client(UpdateProfileRequest(first_name=profile_names[i]))
            await client(UploadProfilePhotoRequest(await client.upload_file(profile_pics[i])))
            time.sleep(30)

# Start the Telegram client and run the auto-reply and auto-profile functions
with client:
    client.loop.run_until_complete(change_profile())
    client.run_until_disconnected()
