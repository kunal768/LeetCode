from collections import deque
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if root == None:
            return None
        discovered = deque([root])
        while(len(discovered) != 0):
            firstNode = False
            size = len(discovered)
            first_val = None
            while size:
                size -= 1
                temp = discovered.pop()
                if not firstNode :
                    firstNode = True
                    first_val = temp.val
                if temp.left :
                    discovered.appendleft(temp.left)
                if temp.right :
                    discovered.appendleft(temp.right)
        return first_val