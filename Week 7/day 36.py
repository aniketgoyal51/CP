# 455. Assign Cookies

# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.



class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count=0
        cg=0
        cs=0
        g.sort()
        s.sort()

        while cg<len(g):
            while cs<len(s) and s[cs]<g[cg]:
                cs+=1
            if cs==len(s):
                break
            if(g[cg]<=s[cs] ):
                count+=1
                cg+=1
                cs+=1
            else:
                cg+=1
        print(g)
        print(s)
        return count