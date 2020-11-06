# bot.py
from discord.ext.commands import Bot, CommandNotFound
from dotenv import load_dotenv
import discord, os, asyncio, ffmpeg
from mutagen.mp3 import MP3

import csvKorona

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = Bot(command_prefix=':')
bot.remove_command("help")

@bot.event
async def on_ready():
	print("Zalaufu sm se!:" + bot.user.name)


@bot.event
async def on_command_error(ctx, error):
	await ctx.send("Komanda `" + ctx.message.content + "` ne obstaja. Uporabi `:pomoc` ali `:help`.")
	await ctx.message.add_reaction("⁉️") 

# OKUZENI
@bot.command(pass_context=True)
async def okuzeni(ctx):
	msg = csvKorona.GetCases()
	await ctx.send(msg)
	

# FARACAJG
@bot.command(pass_context=True)
async def cigaret(ctx):
	await predvajajZvok("faracajg", ctx)


# MACKURINA
@bot.command(pass_context=True)
async def mackurina(ctx):
	await predvajajZvok("mackurina", ctx)
	

# MURJA
@bot.command(pass_context=True)
async def murja(ctx):
	await predvajajZvok("murja", ctx)
	
# Pomoc
@bot.command(pass_context=True, aliases=['help'])
async def pomoc(ctx):
	await getHelp(ctx)
	

async def getHelp(ctx):
	msg = """
	**Serbus, js sm Marlboro Gold Bot, razvija me pa stropy.**
	> **KOMANDE**\n
**Predvajanje zvokov** 🔊
```:murja
:mackurina```
**Covid-19** 😷
```:okuzeni``` 
"""
	await ctx.message.add_reaction("✅")
	await ctx.message.add_reaction("🚬")
	await ctx.send(msg)

	

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

		vc.play(discord.FFmpegPCMAudio(source))
		
		audio = MP3(source)
		await asyncio.sleep(int(audio.info.length))
		await vc.disconnect()

bot.run(TOKEN)













