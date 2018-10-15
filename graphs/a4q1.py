import sys
from collections import defaultdict


class Graph(object):

    def __init__(self, edges=()):
        self.G = defaultdict(set)
        self.G_r = defaultdict(set)
        
        for u, v in edges:
            self.add_edge(u, v)

    def add_edge(self, u, v):
        self.G[u]
        self.G_r[v]

        self.G[u].add(v)
        self.G_r[v].add(u)

    def kosaraju(self):
        visited = set()
        L = []
        
        def dfs(v):
            visited.add(v)
            for u in self.G[v]:
                if u not in visited:
                    dfs(u)
            L.append(v)
        
        for v in self.G.keys():
            if v not in visited:
                dfs(v)
        
        scc = defaultdict(set)
        assigned = set()

        def assign(v, root):
            scc[root].add(v)
            assigned.add(v)
            for u in self.G_r[v]:
                if u not in assigned:
                    assign(u, root)
        
        while L:
            v = L.pop(-1)
            if v not in assigned:
                assign(v, v)

        # Return node counts of top 5 SCC
        res = [len(c) for c in list(scc.values())]
        res.extend([0]*5)
        res = sorted(res, reverse=True)
        return res[:5]


if __name__ == '__main__':

    n = int(raw_input())
    m = int(raw_input())

    sys.setrecursionlimit(n + 10)

    edges = set()
    for i in range(m):
        u, v = raw_input().split()
        u = int(u)
        v = int(v)
        edges.add((u,v))

    g = Graph(edges)
    g_components = g.kosaraju()

    out_str = ''
    for i in g_components:
        out_str += str(i) + '\t'
    
    print out_str
