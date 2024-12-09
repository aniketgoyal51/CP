# 976. Largest Perimeter Triangle
# 
# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.


class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        for i in range(len(nums)-1,1,-1):
            if(nums[i-2]+nums[i-1]>nums[i]):
                return nums[i]+nums[i-1]+nums[i-2]
        return 0