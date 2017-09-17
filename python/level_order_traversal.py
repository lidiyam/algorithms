from python.utils import TreeNode


def level_order_traversal(root):
    queue = []
    if root is not None:
        queue.append(root)

    while len(queue) != 0:
        root = queue.pop()
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)
        print root.val


if __name__ == '__main__':
    node = TreeNode(5)
    level_order_traversal(node)