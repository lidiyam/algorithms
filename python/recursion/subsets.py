"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

"""
class Solution(object):

    # Subsets i
    def subsets(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)

    # Subsets ii
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfsDup(nums, 0, [], res)
        return res

    def dfsDup(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfsDup(nums, i+1, path+[nums[i]], res)


if __name__ == '__main__':
    print Solution().subsets([1,2,3])
    print Solution().subsetsWithDup([1,2,2])