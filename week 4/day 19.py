# question
# Kth Missing Positive Number
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Return the kth positive integer that is missing from this array.

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        missing=0
        number=1
        while count!=k:
            if(number not in arr):
                missing=number
                count+=1
                number+=1
            else:
                number+=1
        return missing