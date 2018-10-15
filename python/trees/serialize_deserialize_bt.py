"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from utils import TreeNode

class Solution:
    
    # def maxDepth(self, root):
    #     if root is None: return 0
    #     return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    # def serialize(self, root):
    #     # write your code here
    #     depth = self.maxDepth(root)
    #     arr = [0]*(2**(depth+1)-1)
        
    #     def ser(root, i):
    #         arr[i] = root.val
    #         if not root.left:
    #             arr[2*i+1] = '#'
    #         else:
    #             ser(root.left, 2*i+1)
    #         if not root.right:
    #             arr[2*i+2] = '#'
    #         else:
    #             ser(root.right, 2*i+2)
            
    #     if not root: return []
    #     ser(root,0)
    #     return arr
        
    def serialize(self, root):    
        arr = []
        
        def ser2(root):
            if root is None: 
                arr.append('#')
                return
            arr.append(root.val)
            ser2(root.left)
            ser2(root.right)
            
        ser2(root)
        return arr
        
    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        
        # def des(i):
        #     if i >= len(data): return None
        #     if data[i] != '#':
        #         node = TreeNode(data[i])
        #         node.left = des(2*i+1)
        #         node.right = des(2*i+2)
        #         return node
        #     else:
        #         return None

        def des():
            if not data: return None
            val = data.pop(0)
            if val == '#':
                return None
            node = TreeNode(val)
            node.left = des()
            node.right = des()
            return node

        
        tree = des()
        return tree
           

if __name__ == '__main__':
    tree = TreeNode(3)
    tree.left = TreeNode(5)
    tree.right = TreeNode(6)
    arr = Solution().serialize(tree)
    print arr
    t2 =  Solution().deserialize(arr)
    print t2.val
    print t2.left.val
    print t2.right.val

