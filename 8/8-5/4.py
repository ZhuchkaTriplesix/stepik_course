t = input().split()
m = set()
for i in t:
    if i.lstrip('0') in m:
        print('YES')
    else:
        m.add(i)
        print('NO')
