# 719. Find K-th Smallest Pair Distance

# The distance of a pair of integers a and b is defined as the absolute difference between a and b.

# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.



class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        low, high = 0, nums[-1] - nums[0]

        def count_pairs_with_max_distance(mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        while low < high:
            mid = (low + high) // 2
            if count_pairs_with_max_distance(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low
