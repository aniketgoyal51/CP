# Question
# Transpose Matrix
# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        arr=[]
        for i in range(0, len(matrix[0])):
            ar=[]
            for j in range(0,len(matrix)):
                ar.append(matrix[j][i])
            arr.append(ar) 
        return arr