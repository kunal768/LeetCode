# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(node):            
    p, c, t = None, node, None
    while c :
        t = c.next
        c.next = p 
        p = c
        c = t
    return p

def printList(node):
    while node :
        print(node.val, end = ' ')
        node = node.next
    
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        fnode, knode, c = head, head, k
        while knode and c > 1:
            c -= 1
            knode = knode.next

        temp = None
        if not knode :
            return fnode
        else:
            temp = knode.next
            knode.next = None 
            
        newHead = reverse(fnode)
        curr = newHead
        while curr.next :
            curr = curr.next
        curr.next = self.reverseKGroup(temp, k)
        return newHead
            
        
            
        
