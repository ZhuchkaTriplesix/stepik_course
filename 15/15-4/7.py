def sum_nums(numstr):
    nums = list(map(int, list(numstr)))
    return sum(nums), int(numstr)


s = input().split()
print(*sorted(s, key=sum_nums))
