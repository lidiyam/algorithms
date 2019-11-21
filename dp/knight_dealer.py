# Leetcode
# 935. Knight Dialer

class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        MOD = 10**9 + 7
        nbrs = {1: [6,8], 2: [7,9], 3:[4,8], 4:[3,9,0], 5:[],
            6:[1,7,0], 7:[2,6], 8:[1,3], 9:[2,4], 0:[4,6]}
        dp = [1]*10
        for _ in range(1,N):
            temp = [0]*10
            for i in range(10):
                for nbr in nbrs[i]:
                    temp[i] += dp[nbr]
            dp = temp
        return sum(dp) % MOD
