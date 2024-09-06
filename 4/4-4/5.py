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

    max_element = float('-inf')

    for i in range(n):
        for j in range(i + 1):
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]

    print(max_element)


main()