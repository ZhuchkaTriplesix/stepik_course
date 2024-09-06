n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for _ in range(n)]
input()
m, k = [int(i) for i in input().split()]
b = [[int(j) for j in input().split()] for _ in range(m)]

c = [[0] * k for i in range(n)]

for i in range(n):
    for j in range(k):
        el = 0
        for r in range(m):
            el += a[i][r] * b[r][j]
        c[i][j] = el

for row in c:
    print(*row)
