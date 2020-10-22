# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root :
            return 0 
        
        if not root.left and not root.right:
            return 1
        
        q = [(root, 0)]
        dis = []
        while q :
            node, d = q.pop(0)
            if not node.left and not node.right :
                dis.append(d)
            
            if node.left :
                q.append((node.left, d+1))
            if node.right:
                q.append((node.right, d+1))
        
        
        return min(dis)+1
            

        
