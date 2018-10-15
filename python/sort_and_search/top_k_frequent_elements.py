"""
Given a non-empty array of integers, return the k most frequent elements.
"""
import collections
import heapq


class Solution(object):

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