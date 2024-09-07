from fractions import Fraction as F

a = input()
b = input()

print(a, '+', b, '=', F(a) + F(b))
print(a, '-', b, '=', F(a) - F(b))
print(a, '*', b, '=', F(a) * F(b))
print(a, '/', b, '=', F(a) / F(b))
