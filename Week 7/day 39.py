# 1833. Maximum Ice Cream Bars

# It is a sweltering summer day, and a boy wants to buy some ice cream bars.

# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

# Note: The boy can buy the ice cream bars in any order.

# Return the maximum number of ice cream bars the boy can buy with coins coins.

# You must solve the problem by counting sort.


class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort(reverse=False)
        count=0
        for i in range(len(costs)):
            if(costs[i]<=coins):
                coins-=costs[i]
                count+=1
        return count