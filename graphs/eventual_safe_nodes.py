# 802. Find Eventual Safe States

class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        N = len(graph)
        WHITE, GREY, BLACK = 0, 1, 2
        color = [0]*N
        
        def dfs(u):
            if color[u] != WHITE:
                return color[u] == BLACK
            
            color[u] = GREY
            for nei in graph[u]:
                if color[nei] == BLACK:
                    continue
                if color[nei] == GREY:
                    return False
                elif not dfs(nei):
                    return False
            color[u] = BLACK
            return True
        
        res = []
        for i in range(N):
            if dfs(i):
                res.append(i)
        return res

