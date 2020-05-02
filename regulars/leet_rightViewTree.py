from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return None
        answer = []
        discovered = deque([root])
        while(len(discovered) != 0):
            size = len(discovered)
            lastNode = False
            while(size):
                size -= 1
                temp = discovered.pop()
                if size == 0: 
                    answer.append(temp.val)
                if temp.left :
                    discovered.appendleft(temp.left)
                if temp.right :
                    discovered.appendleft(temp.right)
        
        return answer