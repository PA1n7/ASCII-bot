import sys
sys.path.append("imports")

import os
import ASCII
import requests

import discord

bot_intents= discord.Intents.default()
bot_intents.typing = True
bot_intents.message_content = True
bot = discord.Client(intents=bot_intents)

@bot.event
async def on_ready():
	print("bot is ready!")

@bot.event
async def on_message(message):
    msg = ""
    if message.content[0] == "?":
        msg = message.content[1:]
    else:
        return
    if msg == "quit_bot":
        await bot.close()
    else:
        cmd = msg.split(" ")
        if cmd[0] == "ascii":
            imgs = message.attachments
            if len(imgs) > 0:
                url = imgs[0].url
                extension = url.split(".")[-1].split("?")[0]
                extension = extension.lower()
                if extension not in ["png", "jpg", "jpeg"]:
                    await message.reply(content="Nono file")
                    return
                response = requests.get(url)
                filename = "temp."+extension
                open(filename, "wb").write(response.content)
                ASCII.ascii(filename, "temp.txt", 50)
                file = discord.File("temp.txt")
                await message.reply(file=file, content="Here you go!")
                os.remove(filename)
                os.remove("temp.txt")

bot.run()#put token in here