s = input().split()

print(('NO', 'YES')[set(s[0]) == set(s[1]) == set(s[2])])
