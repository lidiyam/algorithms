class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]     # build the complete array 
        n = len(nums)
        dp = [[0]*(n) for _ in range(n)]
            
        for l in range(2, n):
            for i in range(n-l):
                j = i + l
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j],
                        dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
              
        return dp[0][n-1]
