n = int(input())

matrix = []
for i in range(n):
    ii = n - i - 1
    row = [1 if i == j or ii == j else 0 for j in range(n)]
    matrix.append(row)

for row in matrix:
    print(*row)
