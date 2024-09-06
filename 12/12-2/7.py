from random import *

fri = [input() for _ in range(int(input()))]
fricop = fri.copy()
a = 0


def rand(a, b):
    r = 0
    for i, j in zip(a, b):
        if i != j:
            r += 1
    return r


while a != len(fri):
    shuffle(fricop)
    a = rand(fri, fricop)
for k, l in zip(fri, fricop):
    print(k, '-', l)
