n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]
left = sum([sum([matrix[i][j] for j in range(n) if i > j and i < n - 1 - j]) for i in range(n)])
down = sum([sum([matrix[i][j] for j in range(n) if i > j and i > n - 1 - j]) for i in range(n)])
up = sum([sum([matrix[i][j] for j in range(n) if i < j and i < n - 1 - j]) for i in range(n)])
right = sum([sum([matrix[i][j] for j in range(n) if i < j and i > n - 1 - j]) for i in range(n)])

print(f"""Верхняя четверть: {up}
Правая четверть: {right}
Нижняя четверть: {down}
Левая четверть: {left}""")
