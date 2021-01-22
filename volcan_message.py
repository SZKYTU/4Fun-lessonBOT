import datetime
import itertools
from take_cert import client


yesterday = datetime.date(2021, 1, 21)
today = datetime.date.today()


class Message:
    def __init__(self, name, content):
        self.name = name
        self.content = content


mess = client.get_messages(yesterday, today)
tesm = []
for el in mess:
    tesm.append(Message(el.title, el.content))

for tesms in tesm:
    print(tesms.name, "\n")
    print(tesms.content, "\n")
