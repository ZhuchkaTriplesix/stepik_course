s = sorted(input())
dct1 = dict(zip(range(len(s)), s))

s = sorted(input())
dct2 = dict(zip(range(len(s)), s))

print('YES' if dct1 == dct2 else 'NO')
