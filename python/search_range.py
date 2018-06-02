class Solution(object):

	def binaryLowSearch(self, nums, target, low, high):
		if low < 0 or high >= len(nums) or low > high:
			return -1
		mid = low + ((high - low) / 2)
		if nums[mid] == target and (mid == low or (mid-1 >= low and nums[mid-1] < target)):
			return mid
		elif nums[mid] == target:
			return self.binaryLowSearch(nums, target, low, mid-1)
		elif nums[mid] < target:
			return self.binaryLowSearch(nums, target, mid+1, high)
		else:
			return self.binaryLowSearch(nums, target, low, mid-1)

	def binaryHighSearch(self, nums, target, low, high):
		if low < 0 or high >= len(nums) or low > high:
			return -1
		mid = low + ((high - low) / 2)
		if nums[mid] == target and (mid == high or (mid+1 <= high and nums[mid+1] > target)):
			return mid
		elif nums[mid] == target:
			return self.binaryHighSearch(nums, target, mid+1, high)
		elif nums[mid] < target:
			return self.binaryHighSearch(nums, target, mid+1, high)
		else:
			return self.binaryHighSearch(nums, target, low, mid-1)

	def searchRange(self, nums, target):
		if not nums:
			return [-1, -1]

		lo = self.binaryLowSearch(nums, target, 0, len(nums)-1)
		if lo == -1:
			return [-1, -1]
		hi = self.binaryHighSearch(nums, target, lo+1, len(nums)-1)
		hi = hi if hi != -1 else lo
		return [lo, hi]

if __name__ == '__main__':
	"""
	Input: nums = [5,7,7,8,8,10], target = 8
	Output: [3,4]
	"""
	print Solution().searchRange([5,7,7,8,8,10], 8)
	print Solution().searchRange([1], 1)
	print Solution().searchRange([2,2], 1)
	print Solution().searchRange([0,0,0,0,0,1,1,2,2,3,4,4,5,5,5,5,6,7], 0)



