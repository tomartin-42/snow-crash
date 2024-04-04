#!/usr/bin/python
import random

num = random.sample(range(15), 5)
num.sort()

for e in num:
    if e < 10:
        print("Levle0" + str(e))
    else:
        print("Levle" + str(e))


