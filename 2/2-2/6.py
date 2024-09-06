l = [int(input()) for n in range(int(input()))]
n = int(input())
fl = False

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] * l[j] == n:
            fl = True
            break

print('ДА' if fl == True else 'НЕТ')
