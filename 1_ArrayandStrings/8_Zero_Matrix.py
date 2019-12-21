#1.8 Zero Matrix: Write an alogrithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0

import numpy as np

def nullifyRow(matrix, row_index):
    for j in range(0, len(matrix[0])):
        matrix[row_index][j] = 0

def nullifyColumn(matrix, col_index):
    for j in range(0, len(matrix)):
        matrix[j][col_index] = 0

def setZeros(matrix):
    row_length = len(matrix)
    col_length = len(matrix[0])
    row = [False]*(row_length)
    col = [False]*(col_length)
    
    for i in range(0, row_length):
        for j in range(0, col_length):
            if ( matrix[i][j] == 0 ):
                row[i] = True
                col[j] = True

    #Nullify rows
    for i in range(0, row_length):
        if (row[i]):
            nullifyRow(matrix, i)

    #Nullify columns
    for i in range(0, col_length):
        if (row[i]):
            nullifyColumn(matrix, i)
    return matrix

example_matrix = [[3]*4, [1]*4, [2]*4, [3]*4]
example_matrix[2][2] =0
print ( np.matrix(setZeros(example_matrix)) )

