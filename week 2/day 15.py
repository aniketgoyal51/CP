# 32. Longest Valid Parentheses

# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        stack.append(-1)
        max=0
        for i in range(len(s)):
            if(s[i]=="("):
                stack.append(i)
            else:
                stack.pop()
                if(not stack):
                    stack.append(i)
                else:
                    l=i-stack[-1]
                    if(l>max):
                        max=l
        return max