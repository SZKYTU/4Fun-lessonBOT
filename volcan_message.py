import re
import datetime
from take_cert import client


yesterday = datetime.date(2021, 1, 21)
today = datetime.date.today()


class Message:
    def __init__(self, name, content, titledate):
        self.name = name
        self.content = content
        self.titledate = re.search(r"\d\d.\d\d", titledate).group()


mess = client.get_messages(yesterday, today)
tesm = []
for el in mess:
    tesm.append(Message(el.title, el.content, el.title))

# for tesms in tesm:
#     # print(tesms.name, "\n")
#     # print(tesms.titledate)
#     print(tesms.content, "\n")

# test = tesm[0].name
# x = reg.search(test)
# print(x.group())
# print(type(x.group()))
