# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0 
        
        def dfs(node):
            if not node :
                return 0 
            
            return node.val + dfs(node.left) + dfs(node.right)
        
        
        return abs(dfs(root.left)-dfs(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)
