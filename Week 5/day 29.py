# 54. Spiral Matrix

# Given an m x n matrix, return all elements of the matrix in spiral order.


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left=0
        right=len(matrix[0])
        up=0
        down=len(matrix)
        ans=[]
        while left <right and up<down:
            for i in range(left,right):
                ans.append(matrix[up][i])
            up+=1

            for i in range(up,down):
                ans.append(matrix[i][right-1])
            right-=1

            if not (left < right and up < down):
                break

            for i in range(right-1,left-1,-1):
                ans.append(matrix[down-1][i])
            down-=1

            for i in range(down-1,up-1,-1):
                ans.append(matrix[i][left])
            left+=1

        return ans