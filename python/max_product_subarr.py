class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curmax = nums[0]
        curmin = nums[0]
        gmax = nums[0]
        
        for i in range(1, len(nums)):
            t_curr_max = curmax
            curmax = max(curmax*nums[i], curmin*nums[i], nums[i])
            curmin = min(t_curr_max*nums[i], curmin*nums[i], nums[i])
            gmax = max(gmax, curmax)
        
        return gmax