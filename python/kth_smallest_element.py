import random


class Solution(object):

    def pivot(self, nums):
        return random.randint(0,len(nums)-1)

    def partition(self, nums, p=0):
        nums[0], nums[p] = nums[p], nums[0]
        n = len(nums)
        i, j = 1, n - 1
        while True:
            while i < n and nums[i] < nums[0]:
                i += 1
            while j >= 1 and nums[j] >= nums[0]:
                j -= 1
            if j < i:
                break
            else:
                nums[i], nums[j] = nums[j], nums[i]
        nums[0], nums[j] = nums[j], nums[0]
        return j

    def kth_smallest_element(self, nums, k):
        if nums:
            p = self.pivot(nums)
            i = self.partition(nums, p)
            if i == k - 1:
                return nums[i]
            elif k < i + 1:
                return self.kth_smallest_element(nums[:i], k)
            else:
                return self.kth_smallest_element(nums[i+1:], k-i-1)


if __name__ == '__main__':
    nums = [7, 9, 1, 2, 3, 5]
    result = Solution().kth_smallest_element(nums, 4)
    print result