f = input()
d = {}
for u in f:
    d.setdefault(f.count(u), u)

for _ in range(int(input())):
    key, value = input().split(':')
    f = f.replace(d[int(value)], key)
print(f)
