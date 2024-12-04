# question 
# Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        for i in range(0,nums[-1]):
            if(i!=nums[i]):
                return i
        return nums[-1]+1