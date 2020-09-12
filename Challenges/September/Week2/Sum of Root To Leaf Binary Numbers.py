# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = []
        def dfs(node,path):
            nonlocal res
            if not node:
                return 
            if not node.left and not node.right:
                path.append(node.val)
                res.append(int("".join(map(str,path)),2))
                return 
            dfs(node.left,path+[node.val])
            dfs(node.right,path+[node.val])
        
        dfs(root,[])
        return sum(res) if len(res) > 0 else 0
