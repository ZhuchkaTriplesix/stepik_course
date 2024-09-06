stroka = input().split('О')
res = max(stroka, key=len)
print(len(res))
