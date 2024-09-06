lovar = dict([[i for i in input().split(' ')] for i in range(int(input()))])
a = input()
for key, value in lovar.items():
    if key == a:
        print(value)
    if value == a:
        print(key)
