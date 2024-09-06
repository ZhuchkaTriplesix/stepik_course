import random

num = random.sample(range(1, 76), 25)
num[12] = 0

for i in range(len(num)):
    print(str(num[i]).ljust(3), end='')
    if i in [4, 9, 14, 19]:
        print()
