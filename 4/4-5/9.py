n = int(input())                                                 # размерность матрицы
matrix = [[int(i) for i in input().split()] for i in range(n)]   # задаем матрицу
matrix_90 = [[[] for i in range(n)] for i in range(n)]           # матр., повернутая на 90гр
count = 0                  #  счетчик для подсч. равенства строк начальной и повернутой матрицы
diag_main = []             #  список элементов главной диагонали
diag = []                  #  список элементов побочной диагонали
lst = []                   #  список элементов матрицы для исключения повторений и проверки от 1 до 1**n
for i in range(n):
    diag_main.append(matrix[i][i])              #  заполняем список элем-ми гл. диаг.
    diag.append(matrix[i][n - i - 1])           #  заполняем список элем-ми побочн. диаг.
    for j in range(n):
        matrix_90[i][j] = matrix[n - j - 1][i]  #  заполняем повернутую на 90 матрицу
        if matrix[i][j] not in lst:
            lst.append(matrix[i][j])            # заполняем список учета всех элементов
for i in range(n):
    if sum(matrix[i]) == sum(matrix_90[i]) == sum(diag_main) == sum(diag):
        count += 1
print('YES' if count == n and len(lst) == n ** 2 and 0 not in lst else 'NO')