from python.utils import TreeNode


class Solution():

    # Time: O(log(n)) and space: O(1)
    def inorderSuccessor(self, root, p):
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ

"""
def inorderSuccessor(root, X):
    # root: TreeNode, p: TreeNode
    # return: TreeNode s
    if not root: return None
    if X.right:
        return X.right
    curr = root
    stack = []
    while curr and curr.val != X.val:
        if X.val < curr.val:
            stack.append((curr, "l"))
            curr = curr.left
        else:
            stack.append((curr, "r"))
            curr = curr.right
    if curr == None: return None
    curr, d = stack.pop(0)
    if d == "r":
        while stack and d != "l":
            curr, d = stack.pop(0)
        return stack.pop(0)[0] if d == "l" else curr
    else:
        return stack.pop(0)[0]
"""
