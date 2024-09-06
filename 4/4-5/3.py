n, m = int(input()), int(input())
matrix = [[int(i) for i in input().split()] for i in range(n)]
change = [int(i) for i in input().split()]
a, b = change[0], change[1]

for i in range(n):
    matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]

for row in matrix:
    print(*row)
