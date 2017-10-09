"""
Given a list of items with values and weights, as well as a max weight,
find the maximum value you can generate from items where the sum of the weights is less than the max.
"""


class Solution(object):

    def knapsack(self, vals, weights, maxWeight):
        T = []
        for x in range(len(vals)+1):
            T.append([0 for y in range(maxWeight+1)])

        for i in range(0, len(vals)+1):
            for j in range(0, maxWeight+1):
                if i == 0 or j == 0:
                    T[i][j] = 0
                    continue
                if j < weights[i-1]:
                    T[i][j] = T[i-1][j]
                else:
                    T[i][j] = max(vals[i-1] + T[i-1][j-weights[i-1]], T[i-1][j])

        return T[len(vals)][maxWeight]


if __name__ == '__main__':
    values = [1, 4, 5, 7]
    weights = [1, 3, 4, 5]
    W = 7
    assert Solution().knapsack(values, weights, W) == 9