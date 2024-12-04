# 79. Word Search

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        done=set()
        def bt(i,j,k):
            if(k==len(word)):
                return True
            if(i>=len(board) or i<0 or j>=len(board[0]) or j<0 or word[k]!=board[i][j] or (i,j) in done):
                return False
            done.add((i,j))
            res=(bt(i+1,j,k+1) or bt(i-1,j,k+1) or bt(i,j+1,k+1) or bt(i,j-1,k+1))
            done.remove((i,j))
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if bt(i,j,0):
                    return True
        return False