from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)
        @lru_cache
        def dp(i):
            if i > 365 :
                return 0
            
            elif i in dayset :
                return min(dp(i+1)+costs[0],dp(i+7)+costs[1],dp(i+30)+costs[2])
            else:
                return dp(i+1)
        return dp(1)
       
        
