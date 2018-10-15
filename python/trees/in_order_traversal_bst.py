"""
Given a binary search tree, print out the elements of the tree in order without using recursion.
"""

from python.utils import TreeNode


# class Solution(object):

#     def left_to_stack(self, stack, node):
#         while node:
#             stack.append(node)
#             node = node.left
#         return stack

#     def in_order_traversal_iterative(self, root):
#         s = []
#         self.left_to_stack(s, root)

#         while s:
#             popped = s.pop(-1)
#             print popped.val,
#             s = self.left_to_stack(s, popped.right)
class Solution(object):
    
    def stack_push(self, stack, node):
        while node:
            stack.append(node)
            node = node.left
        return stack

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        
        stack = self.stack_push(stack, root)
        
        while stack:
            node = stack.pop(-1)
            res.append(node.val)
            stack = self.stack_push(stack, node.right)
        return res

if __name__ == '__main__':
    tree = TreeNode(5)
    tree.left = TreeNode(2)
    tree.right = TreeNode(9)
    tree.right.left = TreeNode(7)
    tree.right.right = TreeNode(11)

    Solution().inorderTraversal(tree)