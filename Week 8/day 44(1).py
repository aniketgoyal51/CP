# 53. Maximum Subarray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.



class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cn=mn=nums[0]
        for i in range(1,len(nums)):
            cn=max(nums[i],cn+nums[i])
            mn=max(cn,mn)
        return mn  