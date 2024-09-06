import random

numbers = [random.randrange(1, 50) for _ in range(7)]

print(*sorted(numbers))