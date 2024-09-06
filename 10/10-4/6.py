res = {}
for i in range(int(input())):
    a, b = input().lower().split()
    res[b] = res.get(b, []) + [a]

for i in range(int(input())):
    name = input().lower()
    print(*res.get(name, ['абонент не найден']))
