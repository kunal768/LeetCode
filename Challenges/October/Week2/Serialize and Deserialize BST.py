# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        ans = []
        def preorder(node):
            nonlocal ans
            if node :
                ans.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ','.join(ans)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        # edge case 
        if not data :
            return []
        
        vals = collections.deque(int(val) for val in data.split(','))
        
        def build(minval, maxval):
            if vals and minval < vals[0] < maxval:
                val = vals.popleft()
                root = TreeNode(val)
                root.left = build(minval, val)
                root.right = build(val, maxval)
                return root
        
        return build(float('-inf'), float('inf'))
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
