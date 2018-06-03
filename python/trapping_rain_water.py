"""
Given n non-negative integers representing an elevation map,
compute how much water it is able to trap.
"""

class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		start, end = 0, len(height)-1
		total = 0
		level = 0
		while start <= end:
			level = max(level, min(height[start], height[end]))
			# move where curr will be filled up with more water
			start_delta = level - height[start]
			end_delta = level - height[end]
			if start_delta > end_delta:
				total += start_delta if start_delta > 0 else 0
				start += 1
			else:
				total += end_delta if end_delta > 0 else 0
				end -= 1
		return total


if __name__ == '__main__':
	inputs = [0,1,0,2,1,0,1,3,2,1,2,1]
	ans = 6
	print Solution().trap(inputs)
