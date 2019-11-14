# Leetcode
# 965. Univalued Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        univalued = True
        if root and root.left:
            if root.val == root.left.val:
                univalued = univalued and self.isUnivalTree(root.left)
            else:
                return False
        if root and root.right:
            if root.val == root.right.val:
                univalued = univalued and self.isUnivalTree(root.right)
            else:
                return False
        return univalued

