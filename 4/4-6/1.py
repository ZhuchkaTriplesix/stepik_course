x, y = [int(i) for i in input().split()]

matrix = [['.'] * y for _ in range(x)]

for i in range(x):
    if i == 0 or i % 2 == 0:
        for j in range(1, y, 2):
            matrix[i][j] = '*'
    else:
        for j in range(0, y, 2):
            matrix[i][j] = '*'

for row in matrix:
    print(*row)
