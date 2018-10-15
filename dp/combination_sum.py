"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.
"""


class Solution(object):

    def combinationSum(self, candidates, target):
        parts = {}
        candidates = set(candidates)
        parts[0] = [[]]
        for t in range(1, target+1):
            # for each 1,2,...,target fill parts[t]
            self.fill_dict(candidates, parts, t)
        return parts[target]

    # parts[4] = [[2,2], [1,3], ...]
    def fill_dict(self, candidates, parts, target):
        parts[target] = []
        for w in candidates:
            if w <= target:
                for i in range(len(parts[target-w])):
                    new_sorted = sorted(parts[target-w][i] + [w])
                    if new_sorted not in parts[target]:
                        parts[target].append(new_sorted)


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    result = [[7], [2, 2, 3]]

    assert sorted(Solution().combinationSum(candidates, target)) == sorted(result)

    candidates = [1, 2, 3, 6, 7]
    res = sorted(Solution().combinationSum(candidates, target))
    print len(res)