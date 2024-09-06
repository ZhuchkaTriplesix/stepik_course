import random


def generate_ip():
    res, a = '', 0
    for i in range(4):
        a = str(random.randint(0, 255)) + '.'
        res += a
    return res[:-1]


print(generate_ip())
