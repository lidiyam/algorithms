"""
Given a cost matrix cost[][] and a position (m, n) in cost[][], find the minimum cost path to reach (m, n) from (0, 0).
Each cell of the matrix represents a cost to traverse through that cell.
Only traverse down, right and diagonally lower cells from a given cell.
"""


# Recursive solution
def min_cost_path_recursive(cost, pos, curr=(0, 0)):
    i, j = curr
    if curr == pos:
        return cost[i][j]
    width = len(cost[0])
    height = len(cost)
    if i == height - 1:
        # only right
        return cost[i][j] + min_cost_path_recursive(cost, pos, (i, j + 1))
    if j == width - 1:
        # only down
        return cost[i][j] + min_cost_path_recursive(cost, pos, (i + 1, j))
    else:
        return cost[i][j] + min(min_cost_path_recursive(cost, pos, (i+1, j)),
                                min_cost_path_recursive(cost, pos, (i, j+1)),
                                min_cost_path_recursive(cost, pos, (i+1, j+1)))


# DP solution
# O(mn)
def min_cost_path(cost, pos):
    m, n = pos
    min_cost = [[0] * (n+1) for _ in range(m+1)]

    # Iterate back from (m, n) to (0,0)
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i == m and j == n:
                min_cost[i][j] = cost[i][j]
            elif i == m:
                min_cost[i][j] = cost[i][j] + min_cost[i][j + 1]
            elif j == n:
                min_cost[i][j] = cost[i][j] + min_cost[i+1][j]
            else:
                min_cost[i][j] = cost[i][j] + min(min_cost[i+1][j], min_cost[i][j+1], min_cost[i+1][j+1])

    return min_cost[0][0]


if __name__ == '__main__':
    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]

    cost2 = [[1, 2, 3, 4, 0],
            [4, 8, 2, 1, 3],
            [1, 5, 3, 4, 3]]
    print min_cost_path_recursive(cost, (2, 2))
    print min_cost_path(cost, (2, 2))
    print min_cost_path(cost2, (2, 4))