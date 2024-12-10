# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=[height[0]]
        right=[height[-1]]
        count=0
        
        for i in range(1,len(height)):
            if(left[-1]<height[i]):
                left.append(height[i])
            else:
                left.append(left[-1])
            
            if(right[-1]>height[(len(height)-1)-i]):
                right.append(right[-1])
            else:
                right.append(height[(len(height)-1)-i])
            
        right=right[::-1]

        for i in range(len(height)):
            if(right[i]>=left[i]):    
                count+=left[i]-height[i]
            elif(right[i]<left[i]):
                count+=right[i]-height[i]
        return count