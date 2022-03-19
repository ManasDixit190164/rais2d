import os
from telethon import TelegramClient, events

print("Starting deployment...")

api_id = 8079920
api_hash = '003d933d631fb5a5abc1053f40480b55'

shivaS= -1001775308909
serD = [-1001737470504]
s1 = -1001384606870
s2 = -1001188182423
s3 = -1001773024200
# s4 = -1001656381315
des = [-1001500045650]


v1_s = -1001737470504
v1_d = [-1001701508412]
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(incoming=True, chats=shivaS))
async def _(event):
    for i in serD:
        try:
            await client.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)

@client.on(events.NewMessage(incoming=True, chats=s1))
async def _(event):
    for i in des:
        try:
            await client.forward_messages(
                i,
                event.message
            )
        except Exception as e:
            print(e)
            
            
@client.on(events.NewMessage(incoming=True, chats=s2))
async def _(event):
    for i in des:
        try:
            await client.forward_messages(
                i,
                event.message
            )
        except Exception as e:
            print(e)
            
@client.on(events.NewMessage(incoming=True, chats=s3))
async def _(event):
    for i in des:
        try:
            await client.forward_messages(
                i,
                event.message
            )
        except Exception as e:
            print(e)
            
            
@client.on(events.NewMessage(chats=v1_s))
async def _(event):
    for i in v1_d:
        try:
            await client.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)

# @client.on(events.NewMessage(incoming=True, chats=s4))
# async def _(event):
#     for i in des:
#         try:
#             await client.forward_messages(
#                 i,
#                 event.message
#             )
#         except Exception as e:
#             print(e)


print("Bot has been deployed.")
client.start()
client.run_until_disconnected()




