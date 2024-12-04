# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        count=0
        right=len(height)-1
        left=0
        while right>left:
            if(count < min(height[right],height[left])*(right-left)):
                count=min(height[right],height[left])*(right-left)
            if(height[right]==min(height[right],height[left])):
                right-=1
            elif(height[left]==min(height[right],height[left])):
                left+=1

        return count