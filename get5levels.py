#!/usr/bin/python

import random

flags = [
    "level00",
    "x24ti5gi3x0ol2eh4esiuxias",
    "f2av5il02puano7naaf6adaaf",
    "kooda2puivaav1idi4f57q8iq",
    "qi0maab88jeaj46qoumi7maus",
    "ne2searoevaevoem4ov4ar8ap",
    "viuaaale9huek52boumoomioc",
    "wiok45aaoguiboiki2tuin6ub",
    "fiumuikeil55xe9cu4dood66h",
    "25749xKZ8L7DkSCwJkT9dyv6f",
    "s5cAJpM8ev6XHw998pRWG728z",
    "feulo4b72j7edeahuete3no7c",
    "fa6v5ateaw21peobuub8ipe6s",
    "g1qKMiRpXf53AWhDaU7FEkczr",
    "2A31L79asukciNyi8uppkEuSx"
]

num = random.sample(range(15), 5)
num.sort()

for e in num:
    if e < 10:
        print("Levle0" + str(e), flags[e])
    else:
        print("Levle" + str(e), flags[e])


