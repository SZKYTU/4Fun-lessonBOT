import os
import discord
import asyncio
import schedule
from config import cfg
from dotenv import load_dotenv
from discord.ext import commands
from volcan_lesson import embedAdd
from volcan_message import embedAddLinks

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


# @bot.command(name="plan")
# async def cmetalsPrice(ctx):
#     bot.delete_message()
#     embed = embedAdd(discord)
#     embed.set_footer(text=bot_by)
#     channel = bot.get_channel(cfg.timetable_channel)
#     await channel.send(embed=embed)

def mainNotiSend():
    def asyncloop():
        async def notyficationSend():
            # bot.delete_message()
            print('noti send')
            embed = embedAddLinks(discord)
            embed.set_footer(text=bot_by)
            channel = bot.get_channel(cfg.timetable_channel)
            await channel.send(embed=embed)
        bot.loop.create_task(notyficationSend())

    async def timeLoop():
        schedule.every(1).minutes.do(asyncloop)
        # schedule.every().day.at("01:29").do(asyncloop)
        i = 0
        while True:
            schedule.run_pending()
            print(f'dzieje{i}')
            await asyncio.sleep(60)
            i += 1

    bot.loop.create_task(timeLoop())


mainNotiSend()


@bot.command(name="link")
async def lessonLink(ctx):
    embed = embedAddLinks(discord)
    embed.set_footer(text=bot_by)
    channel = bot.get_channel(cfg.link_channel)
    await channel.send(embed=embed)

bot.run(KEY_API)
