def merge(A, B):
    if not A or not B :
        return A or B 
    if A.val <= B.val :
        A.next = merge(A.next, B)
        return A
    else:
        B.next = merge(A, B.next)
        return B

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next :
            return head
        s, f, p = head, head, None
        while s and f and f.next:
            p = s
            s = s.next
            f = f.next.next
            
        p.next = None
        l, r = self.sortList(head), self.sortList(s)
        return merge(l,r)
        
