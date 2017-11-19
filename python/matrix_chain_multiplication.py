"""
Given a chain <A1,A2,..,An> of n matrices, where for i = 1,2,...n, 
matrix Ai has dimension p(i-1) x p(i), fully parenthesize the product A1 * A2 * ... An
in a way that minimizes the # of scalar multiplications.
"""
import sys

# Bottom up approach
# Input p: list of matrices dimensions [p0, p1, ..., pn]
def matrix_chain_order(p):
    n = len(p) - 1

    # Build tables m[i,j] - cost of multiplying A[i..j], s[i,j] - optimal split index
    m = [[0] * (n+1) for _ in range(0, n+1)]
    s = [[0] * (n+1) for _ in range(0, n+1)]
    
    for l in range(2, n):   # l is the chain length
        for i in range(1, n-l+1):
            j = i + l - 1
            m[i][j] = sys.maxint
            for k in range(i, j):
                cost_k = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if cost_k < m[i][j]:
                    m[i][j] = cost_k
                    s[i][j] = k

    return (m, s)
    

if __name__ == '__main__':
    p = [30, 35, 15, 5, 10, 20, 25]
    m, s = matrix_chain_order(p)
    print m
