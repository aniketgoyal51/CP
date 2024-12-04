# question 
# Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ar=[-1,-1]
        c=0
        for i in range(len(nums)):
            if(nums[i]==target):
                if(c==0):
                    ar[0]=i
                    ar[1]=i
                else:
                    ar[1]=i
                c+=1
        return ar