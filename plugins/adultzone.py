#Kang With Credits Developed By @P_4_PEEYUSH
"""""
Ported For Ultroid BY @moon_knight69 & @itzyournil

Command Available:
.xxshorts
.xxlong
.picx
.les 

"""""


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from . import *
from . import ultroid_cmd

@ultroid_cmd(pattern="xxshort?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@OpGufaBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1649926429)
            )
            await event.client.send_message(chat, "ðĪŠ{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @OpGufaBot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("ð")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


@ultroid_cmd(pattern="xxlong?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@OpGufaBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1649926429)
            )
            await event.client.send_message(chat, "ð{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @OpGufaBot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("ð")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)
@ultroid_cmd(pattern="xnxx?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "ð2016 Videolarð{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("ð")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


@ultroid_cmd(pattern="picx?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "âĻïļOld photoð{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("ð")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)


@ultroid_cmd(pattern="les?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.get_reply_message()
    chat = "@SeXn1bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=264121194)
            )
            await event.client.send_message(chat, "ðUz_sexâĻïļ{}".format(input_str))
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @SeXn1bot```")
            return
        if response.text.startswith("I can't find that"):
            await event.edit("ð")
        else:
            await event.delete()
            await event.client.send_file(event.chat_id, response.message)
