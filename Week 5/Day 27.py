# Question 
# Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all 
# four edges of the grid are all surrounded by water.


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def island(grid,i,j):
            if(i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=="0"):
                return 
            grid[i][j]="0"
            island(grid,i+1,j)
            island(grid,i-1,j)
            island(grid,i,j+1)
            island(grid,i,j-1)

        count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]=="1"):
                    count+=1
                    island(grid,i,j)
        return count