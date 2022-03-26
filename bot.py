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


v1_s = -1001166732740
v1_d = [-1001701508412]

v2_s = -1001318942027
v2_d = [-1001632606017]

v3_s = -1001572749134
v3_d = [-1001663607450]

v4_s = -1001213730666
v4_d = [-1001247725526]

v5_s = -1001237325544
v5_d = [-1001661268099]

v6_s = -1001471085094
v6_d = [-1001576059626]

v7_s = -1001499366132
v7_d = [-1001674225031]

v8_s = -1001264973891
v8_d = [-1001602245687]

ip_s1 = -1001376505879
ip_s2 = -1001200363662
ip_s3 = -1001737470504
ip_d = -1001723920884

iplS = -1001716769309
iplT = -1001511223693

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
            
#########################################################################################################################################

#########################################################################################################################################


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

@client.on(events.NewMessage(chats=v2_s))
async def _(event):
    for i in v2_d:
        try:
            await client.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)
            
            
@client.on(events.NewMessage(chats=v3_s))
async def _(event):
    for i in v3_d:
        try:
            await client.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)

@client.on(events.NewMessage(chats=v4_s))
async def _(event):
    for i in v4_d:
        try:
            await client.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)

@client.on(events.NewMessage(chats=v5_s))
async def _(event):
    for i in v5_d:
        try:
            await client.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)
            
            
@client.on(events.NewMessage(chats=v6_s))
async def _(event):
    for i in v6_d:
        try:
            await client.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)
            
@client.on(events.NewMessage(chats=v7_s))
async def _(event):
    for i in v7_d:
        try:
            await client.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)

@client.on(events.NewMessage(chats=v8_s))
async def _(event):
    for i in v8_d:
        try:
            await client.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)
            
##################################################  I P O  ########################################################
            
@client.on(events.NewMessage(incoming=True, chats=ip_s1))
async def _(event):
    txt  = "\n〰️〰️❤️‍🔥@IPO_STOCK_MARKET_GMP "
    try:
        if event.photo:
            photo = event.media.photo
            text_to_forward = "**"+event.text+"\n"+txt+"**"
            await client.send_file(ip_d, photo, caption=text_to_forward, parse_mode = "md", link_preview=False)
          
        elif event.media:
            try:
                if event.media.webpage:
                    text_to_forward = "**"+event.text+"\n"+txt+"**"
                    await client.send_message(ip_d, text_to_forward, parse_mode = "md", link_preview=False)
                    return
            except:
                media = event.media.document
                text_to_forward = "**"+event.text+"\n"+txt+"**"
                await client.send_file(ip_d, media, caption=text_to_forward, parse_mode = "md", link_preview=False)
                return
        else:
            text_to_forward = "**"+event.text+"\n"+txt+"**"
            await client.send_message(ip_d, text_to_forward, parse_mode = "md", link_preview=False)
    except Exception as e:
        print(e)
            
            
            
@client.on(events.NewMessage(incoming=True, chats=ip_s2))
async def _(event):
    txt  = "\n〰️〰️❤️‍🔥@IPO_STOCK_MARKET_GMP "
    try:
        if event.photo:
            photo = event.media.photo
            text_to_forward = "**"+event.text+"\n"+txt+"**"
            await client.send_file(ip_d, photo, caption=text_to_forward, parse_mode = "md", link_preview=False)
          
        elif event.media:
            try:
                if event.media.webpage:
                    text_to_forward = "**"+event.text+"\n"+txt+"**"
                    await client.send_message(ip_d, text_to_forward, parse_mode = "md", link_preview=False)
                    return
            except:
                media = event.media.document
                text_to_forward = "**"+event.text+"\n"+txt+"**"
                await client.send_file(ip_d, media, caption=text_to_forward, parse_mode = "md", link_preview=False)
                return
        else:
            text_to_forward = "**"+event.text+"\n"+txt+"**"
            await client.send_message(ip_d, text_to_forward, parse_mode = "md", link_preview=False)
    except Exception as e:
        print(e)

#########################  IPL ########################

@client.on(events.NewMessage(incoming=True, chats=iplS))
async def _(event):
    txt  = "\n🌀 Join :- @watchipllivee "
    try:
        if event.photo:
            photo = event.media.photo
            text_to_forward = "**"+event.text+"\n"+txt+"**"
            await client.send_file(iplT, photo, caption=text_to_forward, parse_mode = "md", link_preview=False)
          
        elif event.media:
            try:
                if event.media.webpage:
                    text_to_forward = "**"+event.text+"\n"+txt+"**"
                    await client.send_message(iplT, text_to_forward, parse_mode = "md", link_preview=False)
                    return
            except:
                media = event.media.document
                text_to_forward = "**"+event.text+"\n"+txt+"**"
                await client.send_file(iplT, media, caption=text_to_forward, parse_mode = "md", link_preview=False)
                return
        else:
            text_to_forward = "**"+event.text+"\n"+txt+"**"
            await client.send_message(iplT, text_to_forward, parse_mode = "md", link_preview=False)
    except Exception as e:
        print(e)




print("Bot has been deployed.")
client.start()
client.run_until_disconnected()




