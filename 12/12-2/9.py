import string
import random


def generate_password(length):
    s = ''.join([i for i in (string.printable[:62]) if i not in '10OolI'])
    return (''.join(random.sample(s[:8], 1) + random.sample(s[8:30], 1) + random.sample(s[30:], length - 2)))


def generate_passwords(count):
    return [generate_password(m) for _ in range(count)]


n, m = int(input()), int(input())
print(*generate_passwords(n), sep='\n')