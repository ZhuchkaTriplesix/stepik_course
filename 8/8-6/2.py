set_1 = set(map(int, input().split()))
set_2 = set(map(int, input().split()))
print(*sorted(set_1 & set_2))
