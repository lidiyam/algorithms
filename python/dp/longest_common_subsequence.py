"""
Given sequences X and Y find the length of the longest common subsequence between them.

Common subsequence is a sequence of chars that appear in both X and Y in the same
order, but not necessarily consecutively.
"""


def length_LCS(x, y):
    m, n = len(x), len(y)
    # c[i][j] - length of LCS of X[i] and Y[j]
    c = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[m][n]


if __name__ == '__main__':
    X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    Y = ['B', 'D', 'C', 'A', 'B', 'A']

    print length_LCS(X, Y)