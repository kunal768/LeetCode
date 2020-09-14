# Simple Recursive Approach
from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i < 0 or i >= len(nums):
                return 0
            
            return max((nums[i]+dfs(i+2) if i < len(nums) else 0) ,(nums[i+1]+dfs(i+3) if i + 1 < len(nums) else 0 ))
        
        return dfs(0)
    
# Table Approach 
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums :
            return 0
        n = len(nums)
        if n == 1 : 
            return nums[0]
        dp = [0]*n
        dp[0],dp[1] = nums[0],max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        # print(dp)
        return dp[n-1]
        
