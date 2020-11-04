# bot.py
from discord.ext.commands import Bot
from dotenv import load_dotenv
import os
import discord
import asyncio

import csvKorona
from mutagen.mp3 import MP3

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = Bot(command_prefix='~')


@bot.command(pass_context=True)
async def okuzeni(ctx):
    msg = csvKorona.GetCases()
    await ctx.send(msg)


@bot.command(pass_context=True)
async def cigaret(ctx):
    await predvajajZvok("faracajg", ctx)


@bot.command(pass_context=True)
async def mackurina(ctx):
    await predvajajZvok("mackurina", ctx)


async def predvajajZvok(source, ctx):
    connected = ctx.author.voice
    if connected:
        voice_player = await connected.channel.connect()
        voice_player.play(discord.FFmpegPCMAudio(executable="exes\\ffmpeg.exe", source="mp3\\" + source + ".mp3",
                                                 options="-loglevel panic"))

        server = ctx.message.guild.voice_client

        audio = MP3("mp3\\" + source + ".mp3")
        await asyncio.sleep(int(audio.info.length))
        await server.disconnect()

bot.run(TOKEN)
