import asyncio
import schedule


def mainNotiSend(bot, bot_by, embedAdd, discord, noti_channel):
    def asyncloop():
        async def notyficationSend():
            print('noti send')
            embed = embedAdd(discord)
            embed.set_footer(text=bot_by)
            channel = bot.get_channel(noti_channel)
            await channel.send(embed=embed)
        bot.loop.create_task(notyficationSend())

    async def timeLoop():
        schedule.every(1).minutes.do(asyncloop)
        schedule.every().day.at("18:29").do(asyncloop)
        while True:
            schedule.run_pending()
            await asyncio.sleep(60)

    bot.loop.create_task(timeLoop())
