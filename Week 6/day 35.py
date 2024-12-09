# 233. Number of Digit One
# 
# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        factor=1

        while factor<=n:
            low=n%factor
            current=(n//factor)%10
            high=n//(factor*10)

            if(current==0):
                count+=high*factor
            elif(current==1):
                count+=(high*factor)+low+1
            else:
                count+=(high+1)*factor

            factor*=10
        return count
    