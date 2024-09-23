# question
# Two Sum II - Input Array Is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to 
# a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(nums)-1

        while l<r:
            if(nums[l]+nums[r]>target):
                r-=1
            if(nums[l]+nums[r]<target):
                l+=1
            if nums[l]+nums[r]==target:
                return [l+1,r+1]