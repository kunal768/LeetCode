class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = []
        def inorder(root,arr):
            if root.left :
                inorder(root.left,arr)
            if root :
                arr.append(root.val)
            if root.right :
                inorder(root.right,arr)
    
        inorder(root,arr)
    
        return arr[k-1]
