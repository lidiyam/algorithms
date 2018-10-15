import collections

class Solution(object):
    def findShortestSubArray(self, nums):
    	nums_map, deg, min_len = collections.defaultdict(list), 0, len(nums)
        
        for index, num in enumerate(nums):
            nums_map[num].append(index)
            deg = max(deg, len(nums_map[num]))
        
        for num, indices in nums_map.items():
            if len(indices) == deg:
                min_len = min(min_len, indices[-1] - indices[0] + 1)
        return min_len


if __name__ == '__main__':
	arr1 = [1, 2, 2, 2, 3, 4, 1, 5, 1, 6]
	arr2 = [1, 2]
	print Solution().findShortestSubArray(arr1)