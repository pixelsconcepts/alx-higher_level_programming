#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []
    for row in matrix:
        squared_row = []
        for el in row:
            squared_el = el ** 2
            squared_row.append(squared_el)

        new_matrix.append(squared_row)

    return new_matrix
