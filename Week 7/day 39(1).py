# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

# Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.


class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """

        count=0

        for i in range(len(n)):
            if(int(n[i])>count):
                count=int(n[i])
        return count