# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        newHead = ListNode(0)
        temp = newHead
        for node in lists :
            while(node):
                heapq.heappush(heap,node.val)
                node = node.next
            heap.sort()
        
        heap = list(heap)
        while(len(heap)):
            temp.next = ListNode(heap.pop(0))
            temp = temp.next
        
        return newHead.next