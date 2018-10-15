class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res
    
    def dfs(self, root, sum, ls, res):
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        if root.left:
            self.dfs(root.left, sum-root.val, ls+[root.val], res)
        if root.right:
            self.dfs(root.right, sum-root.val, ls+[root.val], res)