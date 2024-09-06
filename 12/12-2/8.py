import random

n, m = int(input()), int(input())
s = [i for i in '23456789']
s.extend([chr(i) for i in range(ord('a'), ord('z')) if i not in [ord('l'), ord('i'), ord('o')]])
s.extend([chr(i) for i in range(ord('A'), ord('Z')) if i not in [ord('L'), ord('I'), ord('O')]])
for _ in range(n):
    random.shuffle(s)
    p = ""
    for i in range(m):
        p += s[i][0]
    print(p)
