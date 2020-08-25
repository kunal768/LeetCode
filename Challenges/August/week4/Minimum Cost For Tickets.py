from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)
        @lru_cache(None)
        def dfs(i):
            if i > 365 :
                return 0
            elif i in dayset:
                return min(dfs(i+1)+costs[0],dfs(i+7)+costs[1],dfs(i+30)+costs[2])
            else:
                return dfs(i+1)
            
        return dfs(1)
            
        
