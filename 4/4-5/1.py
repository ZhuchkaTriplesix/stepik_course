n, m = int(input()), int(input())

for i in range(n):
    for j in range(m):
        if j != m - 1:
            print(str((i * j)).ljust(2), end=' ')
        else:
            print(str((i * j)), end='')
    print()