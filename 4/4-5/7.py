n = int(input())
matrix = []

for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for j in range(n):
    for i in range(n - 1, -1, -1):
        print(matrix[i][j], end=' ')
    print()
