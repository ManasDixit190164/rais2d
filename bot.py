import os
from distutils.command.clean import clean
from time import sleep
from telethon import TelegramClient, events

print("Starting deployment...")

api_id = 8079920
api_hash = '003d933d631fb5a5abc1053f40480b55'

client = TelegramClient('session_name', api_id, api_hash)

running = False
#print

@client.on(events.NewMessage(pattern=r'\.getmsg'))
async def stophsandler(event):
    global running
    running = True
    to_chat = [ -1001750591319,-1001656381315,-1001589760491]
    c = 0
    j=0
    chat = -662339025
    replied_msg = await event.get_reply_message()
    msg_id = replied_msg.id
    await client.delete_messages(chat , event.message)
    while running:
        allmsg = await client.get_messages(chat , None , reverse=True , min_id=msg_id , max_id=(msg_id + 5))
        for msg in allmsg:
            for i in to_chat:
                await client.send_message(i , msg)
            c = c + 1
            if c == 5:
                c = 0
                msg_id = msg_id + 5
                sleep(3600)


@client.on(events.NewMessage(pattern=r'\.stopmsg'))
async def stophandler(event):
    global running
    running = False
    await client
    await client.edit_message(event.message, "STOPPED F!!")

print("Bot has been deployed.")
client.start()
client.run_until_disconnected()




