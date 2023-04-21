from telethon.sync import TelegramClient
from telethon import events
from datetime import datetime, timedelta
import asyncio

# fill in your API key, API hash, and string session here
api_id = <your api id>
api_hash = '<your api hash>'
string_session = '<your string session>'

# fill in the group ID and the messages you want to send here
group_id = <your group id>
messages = [
    "Hello, world!",
    "How are you doing?",
    "What's up?",
    "How's your day going?"
]

# fill in the paths to your profile picture files here
profile_pics = [
    '/path/to/first/profile/pic.jpg',
    '/path/to/second/profile/pic.jpg',
    '/path/to/third/profile/pic.jpg'
]

# fill in the names you want to use here
names = [
    'John',
    'Jane',
    'Alex',
    'Sam'
]

async def send_messages():
    # create a client object with the API key, API hash, and string session
    client = TelegramClient(string_session, api_id, api_hash)

    # connect to Telegram
    await client.connect()

    # start the client's event loop
    client.start()

    # loop through the messages and send them to the group
    while True:
        for message in messages:
            await client.send_message(group_id, message)
            await asyncio.sleep(60)  # wait for 60 seconds before sending the next message

async def reply_messages():
    # create a client object with the API key, API hash, and string session
    client = TelegramClient(string_session, api_id, api_hash)

    # connect to Telegram
    await client.connect()

    # start the client's event loop
    client.start()

    # reply to personal messages
    @client.on(events.NewMessage(chats=client.get_me()))
    async def handle_new_message(event):
        await asyncio.sleep(5) # wait for 5 seconds before replying
        await event.respond('Hi there, thanks for messaging me!')

    # run the client's event loop
    client.run_until_disconnected()

async def change_profile():
    # create a client object with the API key, API hash, and string session
    client = TelegramClient(string_session, api_id, api_hash)

    # connect to Telegram
    await client.connect()

    # start the client's event loop
    client.start()

    # loop through the profile pictures and names and update the bot's profile
    while True:
        for i in range(len(profile_pics)):
            # read the profile picture file
            with open(profile_pics[i], 'rb') as f:
                profile_pic = await client.upload_file(f)

            # update the bot's profile picture and name
            await client(UpdateProfileRequest(photo=InputPhoto(id=profile_pic),
                                               first_name=names[i],
                                               last_name='Bot'))
            await asyncio.sleep(60)  # wait for 60 seconds before changing the profile again

if __name__ == '__main__':
    tasks = [
        asyncio.create_task(send_messages()),
        asyncio.create_task(reply_messages()),
        asyncio.create_task(change_profile())
    ]
    asyncio.run(asyncio.wait(tasks))
