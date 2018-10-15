from utils import TreeNode

class Solution(object):

    def kthSmallest(self, root, k):
        stack = []
        current = root
        count = 0

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                prev = stack.pop(-1)
                count += 1
                if count == k:
                    return prev.val
                current = prev.right



if __name__ == '__main__':
    tree = TreeNode(5)
    left = TreeNode(3)
    right = TreeNode(10)
    left.left = TreeNode(1)
    left.right = TreeNode(4)
    right.left = TreeNode(8)
    tree.left = left
    tree.right = right
    Solution().in_order(tree, 3)