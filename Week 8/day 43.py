# 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        """
        --> open and close and n get equal
        --> open > close  => +close
        --> n > open  => +open 
        """
        
        ans=[]
        stack=[]

        def backtracking(nclose,nopen):
            if(nclose==nopen==n):
                ans.append("".join(stack))
                return
            if(n > nopen):
                stack.append("(")
                backtracking(nclose,nopen+1)
                stack.pop()
            if(nclose < nopen):
                stack.append(")")
                backtracking(nclose+1,nopen)
                stack.pop()
        
        backtracking(0,0)
        return ans