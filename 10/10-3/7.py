d, l = {}, []

for c in input().split():
    if c not in l:
        l.append(c)
    else:
        d[c] = d.get(c, 0) + 1
        l.append(c + '_' + str(d[c]))

print(*l)
