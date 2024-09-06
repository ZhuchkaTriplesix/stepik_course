s = sorted(s for s in input().lower() if s.isalpha())
dct1 = dict(zip(range(len(s)), s))
s = sorted(s for s in input().lower() if s.isalpha())
dct2 = dict(zip(range(len(s)), s))

print('YES' if dct1 == dct2 else 'NO')
