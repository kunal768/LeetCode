'''
84. Largest Rectangle in Histogram
Hard

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Example:

Input: [2,1,5,6,2,3]
Output: 10

'''

def histogram(heights):     
    # max area rectangle 
    def nsl(arr):
        stack,vector = [],[]
        index = -1
        for i in range(len(arr)):
            if not stack :
                vector.append(-1)
            elif stack and stack[-1][0] < arr[i]:
                vector.append(stack[-1][1])
            elif stack and stack[-1][0] >= arr[i]:
                while stack and stack[-1][0] >= arr[i] :
                    stack.pop()
                if not stack :
                    vector.append(index)
                else:
                    vector.append(stack[-1][1])
            stack.append([arr[i],i])
        return vector
                    
    def nsr(arr):
        stack,vector = [],[]
        index = len(arr)
        for i in range(len(arr)-1,-1,-1):
            if not stack :
                vector.append(index)
            elif stack and stack[-1][0] < arr[i]:
                vector.append(stack[-1][1])
            elif stack and stack[-1][0] >= arr[i]:
                while stack and stack[-1][0] >= arr[i] :
                    stack.pop()
                if not stack :
                    vector.append(index)
                else:
                    vector.append(stack[-1][1])
            stack.append([arr[i],i])
        return vector[::-1]
    l,r = nsl(heights),nsr(heights)
    # print(heights,l,r)
    maxx = 0
    for i in range(len(heights)):
        maxx = max(maxx,heights[i]*(r[i]-l[i]-1))
    return maxx

  
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0 
        return histogram(heights)
        
        
