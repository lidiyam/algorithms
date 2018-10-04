import collections
import heapq


WHITE, GREY, BLACK = 0, 1, 2

def bfs(G, s):
	seen = set([s])	# color = {v: WHITE for v in G}
	p = {s: None}
	dist = {s: 0}
	q = collections.deque([s])
	while q:
		u = q.popleft()
		for v in G[u]:
			if v not in seen:
				p[v] = u
				dist[v] = dist[u] + 1
				seen.add(v)
				q.append(v)
	return dist, p


def dfs(G, s=None):
	seen = set()
	p = {}
	finish_time = {}
	time = 0

	def visit(u):
		nonlocal time

		seen.add(u)
		for v in G[u]:
			if v not in seen:
				p[v] = u
				visit(v)
		finish_time[u] = time
		time += 1

	if s:
		p[s] = None
		visit(s)
	else:
		# DFS forest
		for v in G:
			if v not in seen:
				p[v] = None
				visit(v)
	return finish_time, p


def dfs_iter(G, s=None):
	color = {v: WHITE for v in G}
	p = {s: None}
	finish_time = {}
	time = 0

	s = collections.deque([s])
	while s:
		u = s.pop()
		if color[u] == WHITE:
			color[u] = GREY
			s.append(u)
			for v in G[u]:
				if color[v] == WHITE:
					p[v] = u
					s.append(v)
		elif color[u] == GREY:
			color[u] = BLACK
			finish_time[u] = time
			time += 1
	return finish_time, p


def bipartition(G):
	if not G: return
	seen = set()
	s = G.keys()[0]
	dist, p = bfs(G, s)
	for v, d in dist.items():
		partition[v] = d % 2

	for u in G:
		for v in G[u]:
			if partition[u] == partition[v]:
				return False
	return True



def undirected_has_cycle(G):
	seen = set()
	cycle = False

	def visit(u, p):
		nonlocal cycle
		if cycle: return
		seen.add(u)
		for v in G[u]:
			if v not in seen:
				visit(v, u)
			elif v != p:
				cycle = True
		
	for s in G:
		if s not in seen:
			visit(s, None)
			if cycle: return True
	return cycle


def dag_has_cycle(G):
	color = {v: WHITE for v in G}
	dag = True

	def visit(u):
		nonlocal dag
		if not dag: return
		color[u] = GREY

		for v in G[u]:
			if color[v] == WHITE:
				visit(v, u)
			elif color[v] == GREY:
				dag = False
		color[u] = BLACK

	for s in G:
		if color[s] == WHITE:
			visit(s)
			if not dag: return dag
	return dag


def topological_sort(G):
	color = {v: WHITE for v in G}
	dag = dag_has_cycle(G)
	if not dag: return False
	ordered = collections.deque([])

	def visit(u):
		color[u] = GREY

		for v in G[u]:
			if color[v] == WHITE:
				visit(v, u)

		color[u] = BLACK
		ordered.appendleft(u)

	for s in G:
		if color[s] == WHITE:
			visit(s)
	return ordered


def reverse_graph(G):
	Gr = collections.defaultdict(set)
	for u in G:
		for v in G[u]:
			Gr[v].add(u)
	return Gr


def kosaraju(G):
	pass


"""Minimum Spanning Tree"""

def kruskal(G, w, s):
	pass

def prim(G, w, s):
	pass


"""Single source shortest path"""

def bfs_sssp(G, s):
	pass

def dijkstra(G, s, w=None):
	pass

def dag_sssp(G, s, w=None):
	pass

"""All pairs shortest path"""

def floyd_warshall(W):
	pass


""" Intractability """

def complement_graph(G):
	pass

def clique_to_vertex_cover(G, k, vertex_cover):
	pass

""" Extra """

def a_star(G, s, w):
	pass


""" Tests """
def test_graph_search(search):
	assert search({0: []}, 0)[1] == ({0: None})
	assert (search({0: [1], 1: [0]}, 0)[1] == ({0: None, 1: 0}))
	assert (search({0: [1], 1: [0]}, 1)[1] == ({0: 1, 1: None}))
	assert (search({0: [1], 1: []}, 0)[1] == ({0: None, 1: 0}))
	assert (search({0: [1], 1: []}, 1)[1] == ({1: None}))
	assert (search({"A": ["B", "C"], "B": ["C"], "C": ["A"]}, "A")[1] ==
	        ({"A": None, "B": "A", "C": "A"}))
	assert (search({"A": ["B", "C"], "B": ["C"], "C": ["A"]}, "B")[1] ==
	        ({"B": None, "C": "B", "A": "C"}))
	assert (search({"A": ["B", "C"], "B": ["C"], "C": ["A"]}, "C")[1] ==
	        ({"C": None, "A": "C", "B": "A"}))

def test_undirected_has_cycle(has_cycle):
    assert not has_cycle({})
    assert not has_cycle({0: []})
    assert not has_cycle({0: [], 1: []})
    assert not has_cycle({0: [1], 1: [0]})
    assert has_cycle({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    assert has_cycle({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 0]})
    assert not has_cycle({0: [1], 1: [0, 2], 2: [1, 3], 3: [2]})

if __name__ == '__main__':
	test_graph_search(bfs)
	test_undirected_has_cycle(undirected_has_cycle)
