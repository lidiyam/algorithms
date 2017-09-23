"""
Given a binary search tree, print out the elements of the tree in order without using recursion.
"""

from python.utils import TreeNode


class Solution(object):

    def left_to_stack(self, stack, node):
        while node:
            stack.append(node)
            node = node.left
        return stack

    def in_order_traversal_iterative(self, root):
        s = []
        self.left_to_stack(s, root)

        while s:
            popped = s.pop(-1)
            print popped.val,
            s = self.left_to_stack(s, popped.right)

if __name__ == '__main__':
    tree = TreeNode(5)
    tree.left = TreeNode(2)
    tree.right = TreeNode(9)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(11)

    Solution().in_order_traversal_iterative(tree)