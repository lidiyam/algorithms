# Leetcode #376

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        dp = [0]*n
        sign = [0]*n
        dp[0] = 1
        for i in range(1,n):
            for j in range(i):
                if nums[j] > nums[i] and sign[j] >= 0:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j]+1
                        sign[i] = nums[i]-nums[j]
                elif nums[j] < nums[i] and sign[j] <= 0:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j]+1
                        sign[i] = nums[i]-nums[j]
        return max(dp)
