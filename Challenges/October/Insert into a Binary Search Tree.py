# Recursive
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(root, val):
            if not root :
                return TreeNode(val)
            
            if root.val > val :
                root.left = insert(root.left, val)
            
            else :
                root.right = insert(root.right, val)
            
            return root
        
        return insert(root, val)

# Iterative
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root :
            return TreeNode(val)
        
        temp = root
        parent = None
        while temp :
            parent = temp
            if val < temp.val :
                temp = temp.left
            else:
                temp = temp.right
        
        if val < parent.val :
            parent.left = TreeNode(val)
            
        else :
            parent.right = TreeNode(val)
        
        return root
            
               
            
        
