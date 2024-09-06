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

    results = []

    for row in matrix:
        average = sum(row) / n
        count = sum(1 for x in row if x > average)
        results.append(count)

    for result in results:
        print(result)


main()
