# 17. Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if(digits==""):
            return []
        keyboard={
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        
        result=[]
        def backtracking(index,path):
            if(index==len(digits)):
                result.append(path)
                return
            curpath=keyboard[int(digits[index])]
            for i in curpath:
                backtracking(index+1,path+i)

        backtracking(0,"")
        return result