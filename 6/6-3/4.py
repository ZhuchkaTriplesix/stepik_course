numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

l = []
for i in numbers:
    l.append(sum(i) / len(i))

print(l)
