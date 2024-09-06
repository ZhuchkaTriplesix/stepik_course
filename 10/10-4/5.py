d = {}
for _ in range(int(input())):
    s = input().split()
    d[s[0]] = s[1:]
for _ in range(int(input())):
    city = input()
    for country, cities in d.items():
        if city in cities:
            print(country)
