class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B or len(A) == 0 or len(B) == 0 :
            return []
        
        m,n = len(A),len(B)
        i,j = 0,0
        ans = []
        while i < m and j < n :
            lo = max(A[i][0],B[j][0])
            hi = min(A[i][1],B[j][1])
            if lo <= hi :
                ans.append([lo,hi])
                
            if A[i][1] < B[j][1] :
                i += 1
            else:
                j += 1
        return ans 
