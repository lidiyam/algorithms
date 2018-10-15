from python.utils import TreeNode

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        mid = len(nums) / 2
        tree = TreeNode(nums[mid])
        tree.left = self.sortedArrayToBST(nums[:mid])
        tree.right = self.sortedArrayToBST(nums[mid+1:])
        return tree

if __name__ == '__main__':
    tree = Solution().sortedArrayToBST([1,2,3,4])
