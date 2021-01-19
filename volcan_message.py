import json
from vulcan import Vulcan
import itertools
import datetime

with open('cert.json') as f:
    certificate = json.load(f)

client = Vulcan(certificate)

yesterday = datetime.date(2020, 12, 22)
today = datetime.date.today()
print(today)

less = client.get_messages()
# less = client.get_messages(date_from=today, date_to=today)
# next(less.title)
# less_sub = less.title
# print(type(less))
#

# for grade in client.get_messages(date_from=yesterday, date_to=today):
# print(grade.title)
# print(less)
list = list(itertools.islice(less, 2, 4))

# print(len(list))
element = list[0]

print(element)
