lst = [input().split() for i in range(int(input()))]

for i in range(len(lst)):
    print(lst[i][0], lst[i][1])

print()

for i in range(len(lst)):
    if lst[i][1] in '45':
        print(lst[i][0], lst[i][1])