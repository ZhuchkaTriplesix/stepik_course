nums = input().split()


def cmp(num):
    n = [int(i) for i in num]
    return sum(n)


nums.sort(key=cmp)
print(*nums)
