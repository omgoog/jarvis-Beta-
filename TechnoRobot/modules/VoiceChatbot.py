import os
import aiofiles
import aiohttp
from random import randint
from pyrogram import filters
from JarvisRobot import pbot as LYCIA

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = await resp.text()
    return data

async def ai_amelia(url):
    ai_name = "Amelia.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(ai_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return ai_name


@LYCIA.on_message(filters.command("Amelia"))
async def Lycia(_, message):
    if len(message.command) < 2:
        await message.reply_text("Lycia AI Voice Chatbot")
        return
    text = message.text.split(None, 1)[1]
    amelia = text.replace(" ", "%20")
    m = await message.reply_text("Amelia Is Best...")
    try:
        L = await fetch(f"https://api.affiliateplus.xyz/api/chatbot?message={lycia}&botname=amelia&ownername=Abhishek&user=1")
        chatbot = L["message"]
        VoiceAi = f"https://lyciavoice.herokuapp.com/lycia?text={chatbot}&lang=hi"
        name = "techno"
    except Exception as e:
        await m.edit(str(e))
        return
    await m.edit("Made By @Saury12p...")
    LyciaVoice = await ai_lycia(VoiceAi)
    await m.edit("Repyping...")
    await message.reply_audio(audio=LyciaVoice, title=chatbot, performer=name)
    os.remove(LyciaVoice)
    await m.delete()
