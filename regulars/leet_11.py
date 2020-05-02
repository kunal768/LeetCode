# wrong solution tho please correct this 


# from collections import deque
# def maxArea(height) -> int:
#     n = len(height)
#     maxLeft,maxRight = height[0],height[-1]
#     leftmax = [maxLeft]
#     rightmax = deque([maxRight]) 
#     for i in range(1,n):
#         maxLeft = max(maxLeft,height[i])
#         leftmax.append(maxLeft)
#     for i in range(n-2,-1,-1):
#         maxRight = max(height[i],maxRight)
#         rightmax.appendleft(maxRight)
#     summ = 0
#     print(leftmax,rightmax)
#     for i in range(n):
#         summ += (leftmax[i]-rightmax[i]) * height[i]
#     return summ
    
# height = [1,8,6]
# print(maxArea(height))