import collections

class DSU(object):
    def __init__(self, N):
        self.N = N
        self.parent = [i for i in range(N)]
        # for union rank
        self.rank = [0]*N
        
    def find(self, x):
        # with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        if self.find(x) == self.find(y):
            return False
        self.parent[self.find(x)] = self.find(y)    # parent[find(x)] = find(y)
        return True
    
    def unionRank(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr: return False
        # higher rank -> more followers
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        return True

class Solution(object):
                
    def findRedundantConnection(self, edges):
        dsu = DSU(1001)
        for u,v in edges:
            # if not dsu.union(u,v):
            if not dsu.unionRank(u,v):
                return u,v
        
    def findRedundantConnectionDFS(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        For each edge (u, v), traverse the graph with a depth-first search to see if we can connect u to v. 
        If we can, then it must be the duplicate edge.
        """
        graph = collections.defaultdict(set) # u: nodes connected to u
        
        def dfs(u, v):
            if u not in seen:
                seen.add(u)
                if u == v: return True
                return any(dfs(nei, v) for nei in graph[u])
        
        for u,v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return u,v
            graph[u].add(v)
            graph[v].add(u)