# Lambda Function
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted((list(map(lambda x : x**2, A))))

# Two Pointers 
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        l, h = 0, n - 1
        index = h
        ans = [-1]*n
        while l <= h :
            if A[l]*A[l] > A[h]*A[h] :
                ans[index] = A[l]*A[l]
                index -= 1
                l += 1
            else:
                ans[index] = A[h]*A[h]
                index -= 1
                h -= 1
        return ans
                
