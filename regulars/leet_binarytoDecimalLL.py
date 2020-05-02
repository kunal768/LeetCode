class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while(head) :
            res = res << 1 
            res = res | head.val
            head = head.next
        
        return res
        
        