n = int(input())
matr = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i == j) or (i == n - 1 - j):
            print(matr[n - 1 - i][j], end=' ')
        else:
            print(matr[i][j], end=' ')
    print()
