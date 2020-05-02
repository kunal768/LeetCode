# OrderedDict -> you can get top pop push
# how will you get minimum in O(1)
# minElement -> always maintain

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.


"""

"""
Approach : @author : Kunal Keshav Singh Sahni 
		   @descr : we need some dynamic O(1) DS and only hashmap comes to mind

""" 
from collections import defaultdict
import heapq
import sys
class MinStack:

    def __init__(self):
    	self.items = defaultdict(lambda:0)
    	self.min_items = [] 
    	self.top_item = None

    def push(self, x: int) -> None:
    	self.top_item = x
    	self.items[x] 

       
    def pop(self) -> None:
    	# remove top item
    	# also remove ind
    	del self.items[self.top_item]
        

    def top(self) -> int:
    	return self.top_item
        

    def getMin(self) -> int:
    	return self.min_item

# 
MinStack = [-2,0,-3,]
push(-2) 
push(0)
push(-3)
getMin = -3 

