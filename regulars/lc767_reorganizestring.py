-- First Method
class Solution(object):
    def reorganizeString(self, S):
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)):
            if c > (N+1)/2: return ""
            A.extend(c * x)
        ans = [None] * N
        ans[::2], ans[1::2] = A[N/2:], A[:N/2]
        return "".join(ans)
        
        
-- Better and more logical heap based method (always pop max2 based on count) 
from heapq import heappush,heappop
class Solution(object):
    def reorganizeString(self, S):
        N = len(S)
        pq = []
        for i in set(S):
            x = S.count(i)
            if x > (N+1)/2 : 
                return ""
            heappush(pq,(-x,i))
        ans = ""
        while len(pq) >= 2 :
            (n1,ch1),(n2,ch2) = heappop(pq),heappop(pq)
            ans += ch1+ch2
            if n1 + 1 < 0 :
                heappush(pq,(n1+1,ch1))
            if n2 + 1 < 0 :
                heappush(pq,(n2+1,ch2))

        return ans + (pq[0][1] if pq else "")
    
        
            
            
            
        
        
