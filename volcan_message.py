import re
import datetime
from config import cfg
from take_cert import client


today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

mess = client.get_messages(yesterday, today)


class Message:
    def __init__(self, name, content, titledate):
        self.name = name
        self.content = re.search(cfg.reg, content).group()
        self.titledate = re.search(r"\d\d.\d\d", titledate).group()


tesm = []
for el in mess:
    tesm.append(Message(el.title, el.content, el.title))


def embedAddLinks(discord):
    embed = discord.Embed(color=0x666666)
    for tesms in tesm:
        embed.add_field(
            name=f"{tesms.name}", value=f"{tesms.content}", inline=False)
    return embed
