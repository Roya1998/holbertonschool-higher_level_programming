#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squareMatrix = []
    for num in matrix:
        newRow = []
        for x in num:
            square = x * x
            newRow.append(square)
        squareMatrix.append(newRow)
    return squareMatrix
