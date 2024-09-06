set_1 = set(list(map(int, input().split())))
set_2 = set(list(map(int, input().split())))
print(*sorted(set_1.difference(set_2)))
