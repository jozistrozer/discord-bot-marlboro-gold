# bot.py
from discord.ext.commands import Bot
from dotenv import load_dotenv
import discord, os, asyncio
from mutagen.mp3 import MP3

import csvKorona

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = Bot(command_prefix=':')
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Zalaufu sm se!: " + bot.user.name)


@bot.event
async def on_command_error(ctx, error):
    await ctx.send("Ukaz `" + ctx.message.content + "` ne obstaja. Uporabi `:pomoc` ali `:help`.")
    await ctx.message.add_reaction("⁉️")
    print(error)
    """
    user = ctx.message.author
    try:
        voice_channel = user.voice.channel
    except AttributeError:
        voice_channel = None
    
    if voice_channel is None:
        await ctx.send("Za predvajanje zvokov moraš biti povezan na kanal!")
    else:
        if isinstance(error, discord.ClientException):
            await ctx.send("Trenutno predvajam zvok, mal počaki.")
        else:
            await ctx.send("Ukaz `" + ctx.message.content + "` ne obstaja. Uporabi `:pomoc` ali `:help`.")
            await ctx.message.add_reaction("⁉️")
    """


# OKUZENI
@bot.command(pass_context=True)
async def okuzeni(ctx, arg=None):
    msg = ""
    if arg == None:
        msg = csvKorona.GetCases()
    else:
        msg = csvKorona.GetCases(arg)

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


# POZABI
@bot.command(pass_context=True, aliases=['ausbahforzingis'])
async def pozabi(ctx):
    await predvajajZvok("pozabi", ctx)


# JOZEF
@bot.command(pass_context=True)
async def jozef(ctx):
    await predvajajZvok("jozef", ctx)


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
:mackurina
:pozabi, :ausbahforzingis
:jozef```
**Covid-19** 😷
```:okuzeni
:okuzeni [dan.mesec.leto]``` 
"""
    await ctx.message.add_reaction("✅")
    await ctx.message.add_reaction("🚬")
    await ctx.send(msg)


async def predvajajZvok(source, ctx):
    source = "./mp3/" + source + ".mp3"
    user = ctx.message.author
    voice_channel = user.voice.channel

    if voice_channel is not None:
        # create StreamPlayer
        vc = await voice_channel.connect()

        vc.play(discord.FFmpegPCMAudio(source))

        audio = MP3(source)
        await asyncio.sleep(int(audio.info.length))
        await vc.disconnect()


bot.run(TOKEN)
