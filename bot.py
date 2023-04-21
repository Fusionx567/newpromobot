from telethon.sync import TelegramClient
from telethon import events
from datetime import datetime, timedelta
import asyncio

# fill in your API key, API hash, and string session here
api_id = '24639866'
api_hash = 'd04ab3fca3e8b8bd2477d8dd1b3e2c97'
string_session = '1BVtsOJIBu7ZVVXLiiHN5w6n0efhnc8EVc6zGyOf2ygYCuTZUrWzS_-AVzH0OBExFKZFXynfLLoR2WbzDKWuNZLo835A6P9Mb-_7398tH_zwdPD0vln8uyRYounP2tBFpqOTQIlypakazCHLhNQ2J5pZBOlPLZP_XBfweiu4GkQCrRXer5aB9UmlZ4uiJRSYnPEaaaFH0Bu9sdznB2PztbU0o9IFq6taMmXpVsTi16gt7vIM1kBi2LcJVHvMlR_tjKdP6LG_MUjV7SBwU3DSEB8y-5g1pIGxM38t8bNyppJ1cBfZIIeiIh_3BDPtnhXF_Xk3UKtI0ocXT8N5lZnqVv4MdyFNaKy0='

# fill in the group ID and the messages you want to send here
group_id = '-1001633934133'
messages = [
    "Hello!",
    "How are you doing?",
    "What's up?",
    "How's your day going?"
]

# fill in the paths to your profile picture files here
profile_pics = [
    'https://telegra.ph/file/0c3c9cb1028a50724968a.jpg',
    'https://telegra.ph/file/6c7285e9fa075393b375b.jpg',
    'https://telegra.ph/file/5854d74e7e74213151140.jpg'
]

# fill in the names you want to use here
names = [
    'Anjali',
    'Natasha',
    'Kajal',
    'Shanti'
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
            await asyncio.sleep(20)  # wait for 60 seconds before sending the next message

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
