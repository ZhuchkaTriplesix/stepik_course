input_data = input().split()
n = len(input_data)
result = [[]]
for size in range(1, n + 1):
    cur_seq = []
    for i in range(n - size + 1):
        cur_seq.append(input_data[i:i + size])

    result.extend(cur_seq)

print(result)