import sys


def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    matrix = []
    index = 2
    for i in range(n):
        row = data[index:index + m]
        matrix.append(row)
        index += m
    for row in matrix:
        print(" ".join(row))
    print()
    for j in range(m):
        transposed_row = [matrix[i][j] for i in range(n)]
        print(" ".join(transposed_row))


main()
