# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root :
            return []
        if not root.left and not root.right :
            return [[root.val]]
        
        res = defaultdict(lambda : [])
        def dfs(root,d,lev,res):
            res[d].append((root.val,lev))
            if root.left: 
                dfs(root.left,d-1,lev-1,res)
            if root.right :
                dfs(root.right,d+1,lev-1,res)
        dfs(root,0,0,res)
        # print(res)
        ans = []
        for key in sorted(res.keys()):
            ans.append([x[0] for x in sorted(res[key],key = lambda x : (-x[1],x[0]) )])
        return ans
            
            
        
