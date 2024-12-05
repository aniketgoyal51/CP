# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # count=0
        # for i in range(len(s)):
        #     arr=[]
        #     for j in range(i,len(s)):
        #         if(s[j] not in arr):
        #             arr.append(s[j])
        #         else:
        #             break
        #     if(len(arr)>count):
        #         count=len(arr)
        # return count
        
        window=set()
        l=0
        ans=0
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[l])
                l+=1
            window.add(s[i])
            ans=max(ans,i-l+1)
        return ans