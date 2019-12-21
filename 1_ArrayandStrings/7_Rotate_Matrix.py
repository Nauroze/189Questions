# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

import numpy as np

example_matrix = [[0]*4, [1]*4, [2]*4, [3]*4]

print ( "Original matrix :" )
print ( np.matrix(example_matrix) )

def Rotate(matrix, N):
    temp_matrix= np.zeros((N,N))

    for row in range(0,N):
        for column in range(0,N):
            temp_matrix[row][column]= matrix[N-column-1][row]

    return temp_matrix

print ("Rotated Matrix:")
print ( Rotate(example_matrix, 4) )