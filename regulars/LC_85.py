'''
85. Maximal Rectangle
Hard

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

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
    def maximalRectangle(self, arr: List[List[str]]) -> int:
        if not arr :
            return 0
        if arr == [["1"]]:
            return 1
        # start_row = None
        n,m = len(arr),len(arr[0])
        if n == 0 or m == 0 :
            return 0 
    
        maxx = 0 
        height = []
        for i in range(m):
            height.append(int(arr[0][i]))
        maxx = max(maxx,histogram(height))
        
        for i in range(1,n):
            for j in range(m):
                if arr[i][j] == "0":
                    height[j] = 0
                else:
                    height[j] += int(arr[i][j])
            maxx = max(maxx,histogram(height))        
            
        return maxx
        

        
        
        
        
        
        
        
        
        
        
        
        
       
