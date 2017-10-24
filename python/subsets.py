"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

"""
class Solution(object):

    # DFS recursively 
    def subsets(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)


if __name__ == '__main__':
    print Solution().subsets([1,2,3])
