# Задача 1
# Напишите функцию для транспонирования матрицы


matrix = [[1, 2, 8, 7],
          [6, 12, 10, 5]]

print("исходная матрица:\n", matrix)

def matrix_transposition_2(matrix):
    trans_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    print(trans_matrix)

matrix_transposition_2(matrix)