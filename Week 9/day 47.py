# 2418. Sort the People

# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.



class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        for i in range(len(heights)):
            for j in range(i,len(heights)):
                if(heights[i]<heights[j]):
                    height=heights[j]
                    heights[j]=heights[i]
                    heights[i]=height

                    name=names[j]
                    names[j]=names[i]
                    names[i]=name
        return names