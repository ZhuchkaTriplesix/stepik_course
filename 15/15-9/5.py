a, b = int(input()), int(input())

print(*filter(lambda n: all(map(lambda x: x != 0 and n % x == 0, map(int, str(n)))), range(a, b + 1)))
