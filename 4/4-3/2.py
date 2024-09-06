x = int(input())
array = []
for i in range(1, x + 1):
    if i not in array:
        array.append(i)
    print(array)
