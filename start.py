import random
from random import randint

n = 0
n = int(input())

tmp = []
ress = []
while len(tmp) < n:
    x = randint(1, 100)
    if x not in tmp:
        tmp.append(x)
    for i in range(1):
        if (n % 2) == 0:
            gen = sorted([random.choice([i for i in range(100)]) for j in range(x)])
            ress.append(gen)
        else:
            gen = sorted([random.choice([i for i in range(100)]) for j in range(x)],reverse = True)
            ress.append(gen)
print(ress)