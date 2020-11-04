# bot.py
import os
import discord
from dotenv import load_dotenv
import csvKorona

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):

    if message.content.startswith("-play") or message.content.startswith("!play") or message.content.startswith(";;play"):
        await message.delete()

    if "kolk je kej okuženih" in message.content or "kolk je blo okuženih" in message.content:
        msg = csvKorona.GetCases()
        await message.channel.send(msg)

client.run(TOKEN)
