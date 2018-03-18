from collections import defaultdict


class Graph(object):
    """A directed graph. Nodes may be any hashable values."""

    def __init__(self, edges=()):
        """Initialize graph from optional iterable of edges."""
        self._out = defaultdict(set) # Map from node to its out-neighbours
        self._in = defaultdict(set) # Map from node to its in-neighbours
        for u, v in edges:
            self.add_edge(u, v)

    def add_node(self, u):
        """Add a node u to the graph."""
        self._out[u]
        self._in[u]

    def add_edge(self, u, v):
        """Add a directed edge to the graph, from node u to node v."""
        self.add_node(u)
        self.add_node(v)
        self._out[u].add(v)
        self._in[v].add(u)

    def in_neighbours(self, u):
        return self._in[u]

    def out_neighbours(self, u):
        return self._out[u]

    def __iter__(self):
        """Return iterator over the nodes of the graph."""
        return iter(self._out)

    def components(self):
        """Return list of strongly connected components."""
        visited = set()         # Set of visited nodes.
        L = []                  # Nodes in topological order.
        
        def visit(u):
            if u not in visited:
                visited.add(u)
                for v in self.out_neighbours(u):
                    visit(v)
                L.insert(0, u)
        
        for u in self:
            visit(u)
        
        component = defaultdict(set) # Map from root to its component.
        assigned = set()       # Set of nodes assigned to a component.

        def assign(u, root):
            if u not in assigned:
                component[root].add(u)
                assigned.add(u)
                for v in self.in_neighbours(u):
                    assign(v, root)
        
        for u in L:
            assign(u, u)

        res = [len(c) for c in list(component.values())]
        res.extend([0]*5)
        res = sorted(res[:5], reverse=True)
        return res


if __name__ == '__main__':
    n = int(raw_input())
    m = int(raw_input())

    edges = set()
    for i in range(m):
        u, v = raw_input().split()
        u = int(u)
        v = int(v)
        edges.add((u,v))

    g = Graph(edges)
    g_components = g.components()

    out_str = ''
    for i in g_components:
        out_str += str(i) + '\t'

    print out_str
