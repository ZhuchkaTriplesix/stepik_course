def chunked(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
input_string = input()
n = int(input())
lst = input_string.split()
result = chunked(lst, n)
print(result)