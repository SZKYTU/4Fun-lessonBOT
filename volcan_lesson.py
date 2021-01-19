import json
from vulcan import Vulcan
import itertools
import datetime


with open('cert.json') as f:
    certificate = json.load(f)

client = Vulcan(certificate)


teacher = []
timelessonfrom = []
timelessonto = []
namelesson = []

lesson_plan = client.get_lessons()
lesson = list(itertools.islice(lesson_plan, 0, None))

i = 0
while i < len(lesson):
    teacher.append(lesson[i].teacher.short)
    namelesson.append(lesson[i].subject.short)
    timelessonto.append(lesson[i].time.to)
    timelessonfrom.append(lesson[i].time.from_)
    i += 1
    # return testlist


# def addToEmbed():


print(namelesson)


# def embedAdd(title, hexColor, takepricetype):
#     embed = discord.Embed(title=title, color=hexColor)
#     take_price = takeprice(takepricetype)
#     i = 0
#     for x in take_price:
#         embed.add_field(name=f"{take_price[i][1]}", value=f"{take_price[i][0]}", inline=False)
#         i += 1
#     return embed
