from heapq import heappush,heappop
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack = [ ]
        pq = []
        while stack or root1:
            while root1:
                stack.append(root1)
                root1 = root1.left
            
            root1 = stack.pop()
            heappush(pq,root1.val)
            root1 = root1.right
        
        stack.clear()
        while stack or root2:
            while root2 :
                stack.append(root2)
                root2 = root2.left
            root2 = stack.pop()
            heappush(pq,root2.val)
            root2 = root2.right
            
        ans = []
        while pq :
            ans.append(heappop(pq))
        return ans    
        
        
        
        
        
