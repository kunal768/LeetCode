
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
		root = TreeNode(preorder[0])    	
    	s  = [root]
    	i = 1
    	while len(s)!=0 :
    		temp = None
  
            # Keep on popping while the next value  
            # is greater than stack's top value.  
            while (len(s) > 0 and preorder[i] > s[-1].data):  
                temp = s.pop() 
              
            # Make this greater value as the right child 
            # and append it to the stack 
            if (temp != None):  
                temp.right = Node(preorder[i]) 
                s.append(temp.right) 
              
            # If the next value is less than the stack's top 
            # value, make this value as the left child of the  
            # stack's top node. append the new node to stack 
            else : 
                temp = s[-1] 
                temp.left = Node(preorder[i]) 
                s.append(temp.left) 
            i = i + 1
          
        return root 
