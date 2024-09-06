a, b, c = (set(int(i) for i in input().split()) for i in range(3))
print(*sorted(set(a.intersection(b).difference(c)))[::-1])
