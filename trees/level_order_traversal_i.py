from python.utils import TreeNode


class Solution(object):

    def level_order_traversal(self, root):
        if root is None:
            return []
        result = []
        queue = [root]

        while queue:
            next_level = []
            vals = []

            for node in queue:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
            result.append(vals)
        return result


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().level_order_traversal(root)
    print result