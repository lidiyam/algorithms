import sys

class Graph(object):

    def __init__(self, edges=()):
        self.G = {}
        self.V = set()
        self.E = set()

        for u,v in edges:
            if u not in self.V:
                self.V.add(u)
            if v not in self.V:
                self.V.add(u)
            self.add_edge(u,v)

    def add_edge(self, u, v):
        self.E.add((u,v))

        if u not in self.G:
            self.G[u] = [v]
        else:
            self.G[u].append(v)

        if v not in self.G:
            self.G[v] = []
        
    def reverse(self):
        r_edges = set()
        for u, v in self.E:
            r_edges.add((v,u))

        rG = Graph(r_edges)
        return rG

    def kosaraju(self):
        visited = set()
        L = []

        def dfs(v):
            visited.add(v)
            for u in self.G[v]:
                if u not in visited:
                    dfs(u)
            L.append(v)

        for v in self.V:
            if v not in visited:
                dfs(v)

        G_r = self.reverse()
        Gr = G_r.G

        rev_order = []
        while L:
            item = L.pop(-1)
            rev_order.append(item)

        scc = {v: v for v in self.V}
        visited = set()
        indx = 0

        def dfs_rev(v):
            visited.add(v)
            scc[v] = indx
            for u in Gr[v]:
                if u not in visited:
                    dfs_rev(u)

        for v in rev_order:
            if v not in visited:
                dfs_rev(v)
            indx += 1

        components = {}
        for v, c in scc.items():
            if c not in components:
                components[c] = [v]
            else:
                components[c].append(v)

        # Return node counts of top 5 SCC
        res = [len(c) for c in list(components.values())]
        res.extend([0]*5)
        return sorted(res[:5], reverse=True)


if __name__ == '__main__':

    sys.setrecursionlimit(5000)

    n = int(raw_input())
    m = int(raw_input())

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
