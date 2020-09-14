from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i < 0 or i >= len(nums):
                return 0
            
            return max((nums[i]+dfs(i+2) if i < len(nums) else 0) ,(nums[i+1]+dfs(i+3) if i + 1 < len(nums) else 0 ))
        
        return dfs(0)
