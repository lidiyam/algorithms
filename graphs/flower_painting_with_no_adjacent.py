# 1042. Flower Planting With No Adjacent 

class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        if not paths: return [1]*N
        graph = collections.defaultdict(set)
        for u, v in paths:
            graph[u].add(v)
            graph[v].add(u)

        colors = [0]*(N+1)

        for i in range(1,N+1):
            possibilities = set({1, 2, 3, 4})
            for nei in graph[i]:
                if colors[nei] in possibilities:
                    possibilities.remove(colors[nei])
            colors[i] = possibilities.pop()

        return colors[1:]
