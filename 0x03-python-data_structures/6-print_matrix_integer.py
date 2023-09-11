#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    for i in range(num_rows):
        for j in range(num_cols):
            print("{:d}".format(matrix[i][j]), end=" ")
        print()
