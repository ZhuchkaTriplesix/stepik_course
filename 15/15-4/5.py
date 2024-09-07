from math import *


def get_res(n, f):
    funcs = {'квадрат': n ** 2,
             'куб': n ** 3,
             'корень': n ** 0.5,
             'модуль': abs(n),
             'синус': sin(n)}
    return funcs[f]


a, b = int(input()), input().lower()
print(get_res(a, b))
