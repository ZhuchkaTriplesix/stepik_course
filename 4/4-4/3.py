def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    matrix = []

    index = 1
    for i in range(n):
        row = list(map(int, data[index:index + n]))
        matrix.append(row)
        index += n

    trace = 0
    for i in range(n):
        trace += matrix[i][i]

    print(trace)


main()