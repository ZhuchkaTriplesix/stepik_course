import random

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
for i in range(len(matrix)):
    random.shuffle(matrix[i])
random.shuffle(matrix)
