a = set(input().split() + input().split() + input().split())
b = set(map(str, range(11)))
print(*sorted(b - a, key=int))
