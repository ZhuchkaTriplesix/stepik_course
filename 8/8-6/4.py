n = int(input())
digits = [set(input()) for _ in range(n)]
myset = set(digits[0])
for i in range(1, n):
    myset.intersection_update(digits[i])

print(*sorted(myset))
