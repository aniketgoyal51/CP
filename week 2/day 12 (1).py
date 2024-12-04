# 58. Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        return len(s.strip().split()[-1])

        # s=s.strip()
        # arr=[]
        # for i in s.split(" "):
        #     arr.append(i)
        # return len(arr[-1])