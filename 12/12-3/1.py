from random import uniform

k, n = 0, 10 ** 6  # количество испытаний

for _ in range(n):
    x = uniform(-2, 2)
    y = uniform(-2, 2)
    if x ** 3 + y ** 4 + 2 >= 0 >= 3 * x + y ** 2 - 2:
        k += 1

print(k / n * 16)