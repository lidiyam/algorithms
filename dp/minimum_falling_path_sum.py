# 931. Minimum Falling Path Sum

class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # dp[i][j] = min falling path to get to (i,j)
        # dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + A[i][j]
        n = len(A)
        dp = [[float('inf')]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == 0:
                    dp[i][j] = A[i][j]
                    continue
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + A[i][j])
                if j < n-1:
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1] + A[i][j])
                dp[i][j] = min(dp[i][j], dp[i-1][j] + A[i][j])
        ans = float('inf')
        for i in range(n):
            ans = min(ans, dp[n-1][i])
        return ans


