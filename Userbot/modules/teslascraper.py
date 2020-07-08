
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot.events import register
from userbot import bot, CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from time import sleep
import os
from telethon.tl.types import MessageMediaPhoto
import asyncio
from userbot.modules.admin import get_user_from_event

@register(outgoing=True, pattern="^.scan")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
       await event.edit("`Lütfen bir mesaja yanıt verin.`")
       return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
       await event.edit("`Lütfen bir dosyaya yanıt verin.`")
       return
    chat = "@DrWebBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("`Lütfen gerçekten bir kullanıcının mesajına yanıt verin.`")
       return
    await event.edit("`Musallet.exe var mı yok mu bakıyorum...`")
    async with event.client.conversation(chat) as conv:
      try:
         response = conv.wait_event(events.NewMessage(incoming=True,from_users=161163358))
         await event.client.forward_messages(chat, reply_message)
         response = await response
      except YouBlockedUserError:
         await event.reply(f"`Mmmh sanırım` {chat} `engellemişsin. Lütfen engeli aç.`")
         return

      if response.text.startswith("Forward"):
         await event.edit("`Gizlilik ayarları yüzenden alıntı yapamadım.`")
      elif response.text.startswith("Select"):
         await event.client.send_message(chat, "English")
         await event.edit("`Lütfen bekleyiniz...`")

         response = conv.wait_event(events.NewMessage(incoming=True,from_users=161163358))
         await event.client.forward_messages(chat, reply_message)
         response = conv.wait_event(events.NewMessage(incoming=True,from_users=161163358))
         response = await response

         await event.edit(f"**Virüs taraması bitti. İşte sonuçlar:**\n {response.message.message}")


      elif response.text.startswith("Still"):
         await event.edit(f"`Dosya taranıyor...`")

         response = conv.wait_event(events.NewMessage(incoming=True,from_users=161163358))
         response = await response
         if response.text.startswith("No threats"):
            await event.edit(f"**Virüs taraması bitti. Bu dosya temiz. Geç!**")
         else:
            await event.edit(f"**Virüs taraması bitti. Whopsie! Bu dosya tehlikeli. Sakın yükleme!**\n\nDetaylı bilgi: {response.message.message}")

@register(outgoing=True, pattern="^.creation")
async def creation(event):
    if not event.reply_to_msg_id:
        await event.edit("`Lütfen bir mesaja yanıt verin.`")
        return
    reply_message = await event.get_reply_message()
    if event.fwd_from:
        return
    chat = "@creationdatebot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("`Lütfen gerçekten bir kullanıcının mesajına yanıt verin.`")
       return
    await event.edit("`Tarih hesaplanıyor...`")
    async with event.client.conversation(chat) as conv:
        try:
            await event.client.forward_messages(chat, reply_message)
        except YouBlockedUserError:
            await event.reply(f"`Mmmh sanırım` {chat} `engellemişsin. Lütfen engeli aç.`")
            return

        response = conv.wait_event(events.NewMessage(incoming=True,from_users=747653812))
        response = await response
        if response.text.startswith("Looks"):
            await event.edit("`Gizlilik ayarları yüzenden sonuç çıkartamadım.`")
        else:
            await event.edit(f"**Rapor hazır: **`{response.text.replace('**','')}`")

@register(outgoing=True, pattern="^.voicy")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
       await event.edit("`Lütfen bir mesaja yanıt verin.`")
       return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
       await event.edit("`Lütfen bir dosyaya yanıt verin.`")
       return
    chat = "@Voicybot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("`Lütfen gerçekten bir kullanıcının mesajına yanıt verin.`")
       return
    await event.edit("`CeteUserBot Sesi Dinliyor Lütfen Bekleyin...`")
    async with event.client.conversation(chat) as conv:
        try:
            await event.client.forward_messages(chat, reply_message)
        except YouBlockedUserError:
            await event.reply(f"`Mmmh sanırım` {chat} `engellemişsin. Lütfen engeli aç.`")
            return

        response = conv.wait_event(events.MessageEdited(incoming=True,from_users=259276793))
        response = await response
        if response.text.startswith("__👋"):
            await event.edit("`Botu başlatıp Türkçe yapmanız gerekmektedir.`")
        elif response.text.startswith("__👮"):
            await event.edit("`Ses bozuk, ses. Ne dediğini anlamadım.`")
        else:
            await event.edit(f"**Bir şeyler duydum: **`{response.text}`")

CMD_HELP.update({
"scan":
".scan \
\nKullanım: Belirtilen dosyada virüs var mı yok mu bakın.\n",
"creation":
".creation üst;alt \
\nKullanım: Hesabın ne zaman kuruldugunu öğrenin.\n",
})
