# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS approach 

class Solution:
    # level and parent node [] 
    def dfs(self,root,parent,target,level,lis):
        if root == None :
            return []
        if root.val == target :
            lis.append(parent)
            lis.append(level) 
        else :
            if root.left :
                self.dfs(root.left,root.val,target,level+1,lis)
            if root.right :
                self.dfs(root.right,root.val,target,level+1,lis)
        
    
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # dfs of x and y
        if root == None :
            return False
        
        xlis = [] 
        self.dfs(root,None,x,0,xlis)
        ylis = []
        self.dfs(root,None,y,0,ylis)
                
        if xlis[0] != ylis[0] and xlis[1] == ylis[1] :
            return True
        return False
        
