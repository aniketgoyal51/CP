# 3074. Apple Redistribution into Boxes

# You are given an array apple of size n and an array capacity of size m.

# There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box has a capacity of capacity[i] apples.

# Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.

# Note that, apples from the same pack can be distributed into different boxes.


class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        apples=sum(apple)
        count=0
        capacity=sorted(capacity)
        for i in range(len(capacity)-1,-1,-1):
            apples-=capacity[i]
            count+=1
            if(apples<=0):
                return count