import sys
import os
import math

from python.utils import TreeNode


def traverse(queuqe):
    if queuqe.__len__() == 1:
        return
    root = queuqe.pop(0)
    if root.left is not None:
        queuqe.append(root.left)
    if root.right is not None:
        queuqe.append(root.right)
    print root.val
    return traverse(queuqe)


def level_order_traversal(root):
    queue = []
    if root is not None:
        queue.append(root)
        traverse(queue)
    else:
        return


if __name__ == '__main__':
    node = TreeNode(5)
    level_order_traversal(node)