lst = []
for i in range(int(input())):
    lst.append(len(set(input().lower())))
print(*lst, sep='\n')
