n, m = map(int, input().split())
matrix = []
counter = 1

for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(counter)
        counter += 1

        print(f'{matrix[i][j]}'.ljust(3), end='')
    print()
