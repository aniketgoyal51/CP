# 4. Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n=sorted(nums1+nums2)
        if(len(n)%2==0):
            return (float(n[(len(n)//2)]+n[(len(n)//2)-1])/2)
        else:
            return n[len(n)//2]
        # return 5.00/2
