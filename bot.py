import os
from time import sleep
from telethon import TelegramClient, events

print("Starting deployment...")

api_id = 8079920
api_hash = '003d933d631fb5a5abc1053f40480b55'
to_channel = [-1001500045650 ,-1001543401280, -1001773024200, -1001656381315]
from_channel = -662339025
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(incoming=True, chats=from_channel))
async def _(event):
    for i in to_channel:
        time.sleep(0.2)
        try:
            await client.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)





print("Bot has been deployed.")
client.start()
client.run_until_disconnected()




