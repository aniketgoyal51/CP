# 131. Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.



class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(st):
            l=0
            r=len(st)-1
            while l<r:
                if(st[l]!=st[r]):
                    return False
                l+=1
                r-=1
            return True
            
        def backtracking(index,an):
            if( index==len(s)):
                ans.append(an[:])
                return 
            for i in range(index+1,len(s)+1):
                if(palindrome(s[index:i])):
                    an.append(s[index:i])
                    backtracking(i,an)
                    an.pop()
            
        ans=[]
        backtracking(0,[])
        return ans