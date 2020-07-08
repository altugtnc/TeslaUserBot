
""" İnsanlarla eğlenmek için yapılmış olan UserBot modülü. """

from asyncio import sleep
from random import choice, getrandbits, randint
from re import sub
import time
from collections import deque
import requests
from userbot import CMD_HELP
from userbot.events import register
from userbot.modules.admin import get_user_from_event
from telethon import events
import asyncio
import os
import sys
import random
from telethon import events, functions, types
import asyncio
from telethon.tl.types import ChannelParticipantsAdmins
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

@register(outgoing=True, pattern="^.fakemail")
async def fakemail(event):
   if event.fwd_from:
      return
   chat = "@fakemailbot"
   command = "/generate"
   await event.edit("```Fakemail Oluşturuluyor lütfen bekle CeteUserBot...```")
   async with event.client.conversation(chat) as conv:
      try:
         m = await event.client.send_message("@fakemailbot","/generate")
         await asyncio.sleep(5)
         k = await event.client.get_messages(entity="@fakemailbot", limit=1, reverse=False)
         mail = k[0].text
         # print(k[0].text)
      except YouBlockedUserError:
         await event.reply("```Lütfe @fakemailbot engellemesini kaldırın tekrar deneyin```")
         return
      await event.edit(mail)

@register(outgoing=True, pattern="^.mailid")
async def mailid(event):
   if event.fwd_from:
      return
   chat = "@fakemailbot"
   command = "/id"
   await event.edit("```Fakemail listesi getiriliyor lütfen bekleyin```")
   async with event.client.conversation(chat) as conv:
        try:
            m = await event.client.send_message("@fakemailbot","/id")
            await asyncio.sleep(5)
            k = await event.client.get_messages(entity="@fakemailbot", limit=1, reverse=False)
            mail = k[0].text
            # print(k[0].text)
        except YouBlockedUserError:
            await event.reply("```Lütfe @fakemailbot engellemesini kaldırın tekrar deneyin```")
            return
        await event.edit(mail)
