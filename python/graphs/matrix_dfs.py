# import collections
# import heapq


def getCenter(grid, M, N):
	X, Y = [M//2], [N//2]
	if M % 2 == 0:
		X.append(M // 2 - 1)
	if N % 2 == 0:
		Y.append(N // 2 - 1)
	x, y, max_carrots = 0,0,-1
	for i in X:
		for j in Y:
			if grid[i][j] > max_carrots:
				x, y, max_carrots = i, j, grid[i][j]
	return x, y, max_carrots


def getTotalCarrots(grid):
	M = len(grid)
	if M == 0: return 0
	N = len(grid[0])
	if N == 0: return 0

	r, c, total = getCenter(grid, M, N)

	def getNeighbours(r, c):
		dirs = [(-1,0),(0,1),(1,0),(0,-1)]
		return [(r+i, c+j) for i,j in dirs if 0 <= r+i < M and 0 <= c+j < N]

	visited = set()
	while True:
		visited.add((r,c))
		nbrs = getNeighbours(r,c)
		next_r, next_c, max_carrots = 0,0,-1
		for i, j in nbrs:
			if (i,j) not in visited and grid[i][j] > max_carrots:
				next_r, next_c, max_carrots = i, j, grid[i][j]
		if max_carrots <= 0: return total
		total += max_carrots
		r, c = next_r, next_c

	return total


if __name__ == '__main__':
    grid = [[5, 7, 8, 6, 3],
            [0, 0, 7, 0, 4],
            [4, 6, 3, 4, 9],
            [3, 1, 0, 5, 8]]
    
    print(getTotalCarrots(grid)) # == 27
    print(getTotalCarrots([[0, 1, 2, 0]]))
    print(getTotalCarrots([[]]))
