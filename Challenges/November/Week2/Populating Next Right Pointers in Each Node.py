"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root :
            return root
        q = [root]
        while q :
            for i in range(len(q)-1):
                q[i].next = q[i+1]
            
            q[-1].next = None
            q = [x for n in q for x in (n.left, n.right) if x]
        
        return root
        
