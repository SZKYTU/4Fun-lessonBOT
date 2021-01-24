import os
import discord
from config import cfg
from dotenv import load_dotenv
from discord.ext import commands
from volcan_lesson import embedAdd
from volcan_message import embedAddLinks
from noti_module import mainNotiSend

load_dotenv()
KEY_API = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

bot.remove_command("help")


@bot.event
async def on_ready():
    print('ARBEITEN!!!')


mainNotiSend(bot, cfg.bot_by, embedAdd, discord, cfg.timetable_channel)


mainNotiSend(bot, cfg.bot_by, embedAddLinks, discord, cfg.link_channel)


bot.run(KEY_API)
