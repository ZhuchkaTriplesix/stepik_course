numbers = [int(n) for n in input().split()]
counter = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        counter += 1

print(counter)
