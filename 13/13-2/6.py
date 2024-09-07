from fractions import Fraction as F


def fact(n):
    res = 1
    for i in range(1, n + 1): res *= i
    return res


n = int(input())
print(sum([F(1, fact(i)) for i in range(1, n + 1)]))
