# 7. Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative=False
        if(x>0):
            negative=False
        else:
            negative=True


        x=abs(x)
        ss=str(x)[::-1]
        x=int(ss)


        if(len(bin(x))-2<32):
            if(negative):
                return x-2*x
            else:
                return x        
        else:
            return 0