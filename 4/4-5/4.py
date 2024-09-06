n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]
flag = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flag = False
    if flag is False:
        print('NO')
        break
else:
    print('YES')
