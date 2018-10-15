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
        
        def visit(v):
            if v not in visited:
                visited.add(v)
                for u in self.G[v]:
                    visit(u)
                L.insert(0, v)
        
        for v in self.G.keys():
            visit(v)
        
        scc = defaultdict(set)
        assigned = set()

        def assign(v, root):
            if v not in assigned:
                scc[root].add(v)
                assigned.add(v)
                for u in self.G_r[v]:
                    assign(u, root)
        
        for v in L:
            assign(v, v)

        # Return node counts of top 5 SCC
        # print scc
        res = [len(c) for c in list(scc.values())]
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

