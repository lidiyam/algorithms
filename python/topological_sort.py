
def topologicalSort(G):
	# run DFS, order by decreasing finish time
	res = []
	n = len(G)
	visited = set()

	def dfs(u):
		for v in G[u]:
			if v not in visited:
				dfs(v)
		visited.add(u)
		del G[u]
		res.insert(0, u)

	while len(visited) != n:
		root = G.keys()[0]
		if root not in visited:
			dfs(root)

	return res


if __name__ == '__main__':
	G = {'b': ['d', 'a'], 'd': ['a'], 'a': ['c'], 'c': []}
	print topologicalSort(G)
