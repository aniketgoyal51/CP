# 48. Rotate Image

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                m=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=m

        for i in range(len(matrix)):
            matrix[i].reverse()
        
        return matrix