# Leetcode
# 746. Min Cost Climbing Stairs

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # dp[i] = min cost ending at cost[i]
        n = len(cost)
        dp = [1000]*n
        for i in range(n):
            if i == 0 or i == 1:
                dp[i] = cost[i]
                continue
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[n-1], dp[n-2])

