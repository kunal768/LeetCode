class Solution:
    def longestMountain(self, A: List[int]) -> int:
        l, h = 0, 1
        ans = 0
        while l < len(A) and h < len(A) :
            inc, dec = 0, 0 
            # escape valleys 
            while l < len(A) and h < len(A) and A[l] >= A[h] :
                l += 1
                h += 1
                
            
            while l < len(A) and h < len(A) and A[h] > A[l] :
                inc += 1
                l += 1
                h += 1
            
            while l < len(A) and h < len(A) and A[l] > A[h]:
                dec += 1 
                l += 1
                h += 1
            
            
            
            ans = max(ans, inc+dec if inc > 0 and dec > 0 else 0 )
                
                
        return ans + 1 if ans > 0 else 0
