def read_matrix(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            element = input().strip()
            row.append(element)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))
n = int(input())
m = int(input())

matrix = read_matrix(n, m)

print_matrix(matrix)