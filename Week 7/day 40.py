# 135. Candy

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # count=0
        # for i in range(0,len(ratings)):
        #     if(i==0 and ratings[i+1]>ratings[i]):
        #         count+=1
        #     elif(i>0 and i<len(ratings)-1):
        #         if( ratings[i]>ratings[i-1] or ratings[i]<ratings[i+1] ):
        #             count+=1            
        #         elif(ratings[i]<ratings[i-1] or ratings[i]>ratings[i+1]):
        #             count+=1
        #         if(ratings[i]==ratings[i-1]):
        #             count+1
        #     elif(i==len(ratings)-1 and ratings[i-1]>ratings[i]):
        #         count+=1
        #     else:
        #         count+=2
            
        # return count

        
        candies=[1]*len(ratings)

        for i in range(1,len(ratings)):
            if(ratings[i]>ratings[i-1]):
                candies[i]=candies[i-1]+1
        
        for i in range(len(ratings)-2,-1,-1):
            if(ratings[i]>ratings[i+1]):
                candies[i]=max(candies[i],candies[i+1]+1)
        
        return sum(candies)