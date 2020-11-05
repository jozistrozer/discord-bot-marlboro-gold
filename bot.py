# bot.py
from discord.ext.commands import Bot
from dotenv import load_dotenv
import os
import discord
import asyncio
import ffmpeg

import csvKorona
from mutagen.mp3 import MP3

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = Bot(command_prefix=':')


@bot.event
async def on_ready():
	print("Zalaufu sm se! " + bot.user.name)

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
	source = "./mp3/" + source + ".mp3"
	user = ctx.message.author
	voice_channel = user.voice.channel
	channel = None	
	
	if voice_channel != None:
		# User voice channel
		channel = voice_channel.name
		
		# create StreamPlayer
		vc = await voice_channel.connect()

		vc.play(discord.FFmpegPCMAudio(source), after=lambda e: print('done', e))
		
		audio = MP3(source)
		await asyncio.sleep(int(audio.info.length))
		await vc.disconnect()

bot.run(TOKEN)













