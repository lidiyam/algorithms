class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # last element in or not in
        dp = [[0]*(len(nums)+1) for _ in range(len(nums)+1)]
        
        for i in range(len(nums)-1, 0, -1):
            j = i # len(nums)-1
            while j < len(nums):
                if nums[j] >= nums[i]:
                    dp[i][j] = max(1+dp[i][j-1], dp[i+1][j])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                j += 1
        #print dp
        return dp[1][len(nums)-1]

    def lengthOfLIS_2(self, nums):
        if len(nums) == 0:
            return 0

        dp = [0]*len(nums)
        dp[0] = 1
        maxans = 1

        for i in range(1, len(dp)):
            maxval = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])

            dp[i] = maxval + 1
            maxans = max(maxans, dp[i])
        return maxans


if __name__ == '__main__':
    print Solution().lengthOfLIS([9,1,5,3,4])
    #print Solution().lengthOfLIS([10,9,2,5,3,7,101,18])