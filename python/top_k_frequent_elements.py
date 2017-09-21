"""
Given a non-empty array of integers, return the k most frequent elements.
"""
import collections
import heapq


class Solution(object):

    def topKFrequentSlow(self, nums, k):
        nums = sorted(nums)
        prev = nums[0]
        lst = [prev]
        k = k - 1
        for i in range(1, len(nums)):
            if k > 0 and nums[i] != prev:
                prev = nums[i]
                lst.append(prev)
                k -= 1
        return lst

    def topKFrequent(self, nums, k):
        freq_list = []
        counts = collections.defaultdict(int)
        for i in nums:
            counts[i] += 1

        for key in counts.keys():
            freq_list.append((-counts[key], key))
        heapq.heapify(freq_list)
        topk = []
        for i in range(0, k):
            topk.append(heapq.heappop(freq_list)[1])
        return topk


if __name__ == '__main__':
    nums = [7, 3, 2, 2, 3, 3]
    result = Solution().topKFrequent(nums, 2)
    print result