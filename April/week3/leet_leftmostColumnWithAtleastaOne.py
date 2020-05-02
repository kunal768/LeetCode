
# OPTIMAL SOLUTION (implemented idea as shown in HINT2)

# start from top right corner 
# if the value is 1 : move left, if value is 0 : move right 
# 2. (Optimal Approach) Imagine there is a pointer p(x, y) starting from top right corner.
# p can only move left or down. If the value at p is 0, move down. If the value at p is 1, move left. 
# Try to figure out the correctness and time complexity of this algorithm.


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        [r,c] = binaryMatrix.dimensions()
        i,j = 0,c-1
        minIndex = c 
        while (i < r and j >= 0) :
            val = binaryMatrix.get(i,j)
            print(val,end = ' ')
            if val == 1 :
                minIndex = min(minIndex,j)
                j -= 1
            else :
                 i += 1
        print(minIndex)
        if minIndex == c : return -1
        return minIndex
        