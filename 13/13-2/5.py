from fractions import Fraction

n = int(input())
p = 0
for i in range(1, n + 1):
    a = Fraction(1, i) ** 2
    p += a
print(Fraction(p))
