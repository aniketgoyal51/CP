# 797. All Paths From Source to Target

# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).



class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # result=[]
        # def backtracking(index,ans):
        #     if(graph[index]==[]):
        #         result.append(ans)
        #         return
        #     for i in range(len(graph[index])):
        #         backtracking(index+1,ans)
        #         backtracking(index+1,ans+[graph[index][i]]])

        # backtracking(0,[])
        # return result



        result=[]
        def backtracking(index,ans):
            if(index==len(graph)-1):
                result.append(ans+[index])
                return
            for i in range(len(graph[index])):
                backtracking(graph[index][i],ans+[index])

        backtracking(0,[])
        return result