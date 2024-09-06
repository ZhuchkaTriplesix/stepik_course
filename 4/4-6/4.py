s = input().split()
n = int(s[0])
m = int(s[1])
matrix = [[0 for i in range(m)] for _ in range(n)]
count = 1
for i in range(m):
    for j in range(n):
        matrix[j][i] += count
        count += 1
for i in range(n):
    print(*matrix[i])
