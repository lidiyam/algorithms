class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parent = {root: None}
        while stack:
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q
