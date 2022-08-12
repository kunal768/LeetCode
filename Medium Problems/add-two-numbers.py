# Optimized in one run 
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ansNode = ListNode(0)
        temp = ansNode
        carry = 0 
        while l1 or l2 or carry :
            l1val, l2val = l1.val if l1 else 0, l2.val if l2 else 0
            columnSum = l1val + l2val + carry
            carry = columnSum//10
            temp.next = ListNode(columnSum%10)
            temp = temp.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        return ansNode.next



# Khatarak Brute Force
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node):
            rev, c = None, 0
            while node :
                rev, rev.next, node, c = node, rev, node.next, c + 1
            return (rev, c)
        
        def printList(node):
            temp = node
            while temp : 
                print(temp.val, end = ' ')
                temp = temp.next
        
        (newl1, c1), (newl2, c2) = rev(l1), rev(l2)
        
        num1, num2 = 0, 0
        while newl1 :
            num1 += (newl1.val*(10**(c1 - 1)))
            c1 -= 1
            newl1 = newl1.next
        
        while newl2 :
            num2 += (newl2.val*(10**(c2 - 1)))
            c2 -= 1
            newl2 = newl2.next
        
        ans = num1 + num2
        
        # edge case ans == 0 
        if not ans :
            return ListNode(ans)
        
        ansNode = ListNode(-100)
        temp = ansNode
        while ans :
            temp.next = ListNode(ans%10)
            ans = ans//10
            temp = temp.next
        
        return ansNode.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
        
        
