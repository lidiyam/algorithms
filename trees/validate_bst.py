from utils import TreeNode

class Solution(object):
    def isValidBST(self, root):
        if not root: return True
        if root.left and root.val <= root.left.val: return False
        if root.right and root.val >= root.right.val: return False
        return self.isValid(root.left, -float('inf'), root.val) and self.isValid(root.right, root.val, float('inf'))
    
    def isValid(self, root, lo, hi):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True        
        res = lo < root.val < hi
        if root.right:
            res = res and root.val < root.right.val and self.isValid(root.right, root.val, hi)
        if root.left:
            res = res and root.val > root.left.val and self.isValid(root.left, lo, root.val)
        return res

