# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l,r = 0,0
        curr = 0
        minn = float("inf") 
        n = len(nums)
        while r < n :
            # expand 
            while r < n and curr < s :
                curr += nums[r]
                r += 1
            # contract 
            while l<=r and curr >= s :
                curr -= nums[l]
                l += 1
                minn = min(r-l+1,minn)
                
        if minn == float("inf") :
            return 0 
        return minn
            
            
        
