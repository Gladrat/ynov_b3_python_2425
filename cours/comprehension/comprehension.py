import random

from rich.pretty import pprint

l = list(range(101))
pprint(l)

l = []
for i in range(100):
    l.append(random.randint(0, 10))
pprint(l)

pprint([random.randint(0, 10) for i in range(100)])

age = 43


majeur = True if age > 18 else False

majeur = True
if age < 18:
    majeur = False
else:
    majeur = True