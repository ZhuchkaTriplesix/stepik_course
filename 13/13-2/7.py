from fractions import Fraction
from math import gcd

n = int(input())

for i in range((n - 1) // 2, 0, -1):
    if gcd(i, n - i) == 1:
        print(Fraction(i, n - i))
        break
