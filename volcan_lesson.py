import datetime
import itertools
from take_cert import client


timetable = list(itertools.islice(client.get_lessons(), 0, None))

lessons = []


class Lesson:
    def __init__(self, teacher, name, time_from, time_to):
        self.teacher = teacher
        self.name = name
        self.time_from = str(time_from)[:-3]
        self.time_to = str(time_to)[:-3]


for el in timetable:
    lessons.append(Lesson(el.teacher.short, el.subject.name, el.time.from_, el.time.to))


def embedAdd(discord):
    embed = discord.Embed(color=0x00f7ff)
    for lesson in lessons:
        embed.add_field(
            name=f"{lesson.time_from} -> {lesson.time_to}", value=f"{lesson.name}", inline=False)
    return embed

##
