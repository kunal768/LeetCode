class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root :
                return
            root.left,root.right = root.right,root.left
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return root
            
