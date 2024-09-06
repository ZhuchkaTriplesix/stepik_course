import random

n = int(input())
print(*["Орёл" if random.randint(0, 1) else "Решка" for i in range(n)], sep="\n")
