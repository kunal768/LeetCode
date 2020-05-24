# O(n2)
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = None
        def dfs(root,element):
            if not root :
                root = TreeNode(element)
                return root
            if element < root.val :
                root.left = dfs(root.left,element)
            else:
                root.right = dfs(root.right,element)
            return root
        
        for i in preorder :
            root = dfs(root,i)
            
        return root


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0 :
            return None
        root = TreeNode(preorder[0])    	
        s  = [root]
        i = 1
        while i < len(preorder) :
            temp = None
            while (len(s) > 0 and preorder[i] > s[-1].val):  
                temp = s.pop() 
            if (temp != None):  
                temp.right = TreeNode(preorder[i]) 
                s.append(temp.right) 
            else : 
                temp = s[-1] 
                temp.left = TreeNode(preorder[i]) 
                s.append(temp.left)
            i = i + 1
        return root 
