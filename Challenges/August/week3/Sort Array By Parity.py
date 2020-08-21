# Used the Dutch National Flag Algorithm so got O(n) solution with O(1) space complexity
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        l,h,mid = 0,n-1,0 
        while mid <= h :
            if A[mid] & 1 == 0:
                A[l],A[mid] = A[mid],A[l]
                l += 1
                mid += 1
            else :
                A[mid],A[h] = A[h],A[mid]
                h -= 1
        return A
                
