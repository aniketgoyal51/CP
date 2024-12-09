# 70. Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        last=1
        lasts=1
        index=n
        while index!=1:
            lastt=lasts+last
            last=lasts
            lasts=lastt
            index-=1
            print(last,lasts)
        return lasts