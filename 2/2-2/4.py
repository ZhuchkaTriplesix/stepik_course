n = list(map(int, input().split()))
n.insert(0, n[-1])
del n[-1]
print(*n)
