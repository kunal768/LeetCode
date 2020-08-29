# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root,p,q):
            if not root :
                return None
            if p == root or q == root :
                return root
            
            l,r = lca(root.left,p,q) , lca(root.right,p,q)
            
            if l and r :
                return root
            
            return l if l else r
        
        return lca(root,p,q)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
