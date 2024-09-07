progress = []
for i in range(int(input())):
    progress.append(any(['5' in input().split() for j in range(int(input()))]))

print('YES' if all(progress) else 'NO')
