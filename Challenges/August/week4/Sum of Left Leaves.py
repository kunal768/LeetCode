# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(node,level,d,ans,d_p):
            if not node :
                return 
            if not node.left and not node.right and d == d_p-1:
                ans.append(node.val)
            if node.left:
                dfs(node.left,level+1,d-1,ans,d)
            if node.right:
                dfs(node.right,level+1,d+1,ans,d)
        ans = []
        dfs(root,0,0,ans,-1)
        return sum(ans)
        
