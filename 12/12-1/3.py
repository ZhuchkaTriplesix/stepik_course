import random

length = int(input())  # длина пароля
for i in range(length):
    a = random.choice([1, 2])
    z = chr(random.randint(65, 90)) if a == 1 else chr(random.randint(97, 122))
    print(z, end='')
