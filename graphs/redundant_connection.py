class DisjointSet(object):
    def __init__(self):
        self.nodes = []

    def join(self, d_set):
        self.nodes.extend(d_set.nodes)

    def find(self, node):
        return node in self.nodes

class Solution(object):
    def findRedundantConnection(self, edges):
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        sets = {}
        for edge in edges:
            u, v  = edge[0], edge[1]
            sets[u] = u
            sets[v] = v
        
        for edge in edges:
            u, v  = edge[0], edge[1]
            if sets[u] == sets[v]:
                return edge
            else:

                sets[v] = sets[u]


if __name__ == '__main__':
    input_list = [[1,2],[2,3],[3,4],[1,4],[4,5]]
    edges = [[1,4],[3,4],[1,3],[1,2],[4,5]]
    edges = [[1,5],[3,4],[3,5],[4,5],[2,4]]
    print(Solution().findRedundantConnection(edges))