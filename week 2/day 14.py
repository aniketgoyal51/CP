# 5. Longest Palindromic Substring

# Given a string s, return the longest palindromic substring in s.


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss=s[0]

        for i in range(len(s)):
            l,r=i,i
            while r<len(s) and l>=0 and s[l]==s[r]:
                if(r-l+1>len(ss)):
                    ss=s[l:r+1]
                r+=1
                l-=1

            l,r=i,i+1
            while r<len(s) and l>=0 and s[l]==s[r]:
                if(r-l+1>len(ss)):
                    ss=s[l:r+1]
                r+=1
                l-=1
        if(not ss and len(s)==1):
            return s
        return ss
                    