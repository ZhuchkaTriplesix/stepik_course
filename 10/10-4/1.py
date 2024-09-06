data = [(input().split(':')) for i in range(int(input()))]
data = {i[0].lower(): i[1].strip() for i in data}
for i in [input().lower() for i in range(int(input()))]:
    print(data.get(i, "Не найдено"))
