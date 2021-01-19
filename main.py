import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from volcan_lesson import embedAdd

load_dotenv()
KEY_API = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

bot.remove_command("help")

bot_by = "by SZKYTU ❤️"


@bot.event
async def on_ready():
    print('ARBEITEN!!!')


@bot.command(name="pomoc")
async def helpComand(ctx):
    embed = discord.Embed(
        title="DiggerInfo", description=f"!plan -> wyświetla plan lekcji", color=0x630f00)
    embed.set_footer(text=bot_by)
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(embed=embed)


@bot.command(name="plan")
async def cmetalsPrice(ctx):
    embed = embedAdd(discord)
    embed.set_footer(text=bot_by)
    await ctx.author.create_dm()
    await ctx.author.dm_channel.send(embed=embed)

bot.run(KEY_API)
