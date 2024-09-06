n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n // 2):
    matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
for row in matrix:
    print(*row)
