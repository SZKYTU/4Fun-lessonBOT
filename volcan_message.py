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
        match = re.search(r"\d\d.\d\d", titledate)
        if match:
            self.titledate = match.group()
        else:
            self.titledate = "- - -"


tesm = []
for el in mess:
    tesm.append(Message(el.title, el.content, el.title))


def embedAddLinks(discord):
    embed = discord.Embed(title="Linki do lekcji", color=0x440885)
    for tesms in tesm:
        embed.add_field(
            name=f"{tesms.name}", value=f"{tesms.content}", inline=False)
    return embed
