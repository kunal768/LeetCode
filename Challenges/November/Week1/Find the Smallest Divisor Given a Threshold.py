from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        l = ceil(sum(nums)/threshold)
        h = sum(nums)
        
        
        def satisfies(x):
            ans = 0 
            for i in nums :
                ans += ceil(i / x)
            
            return ans <= threshold
            
        ans = -1
        while l <= h :
            mid = (l+h)//2
            if satisfies(mid) :
                ans = mid 
                h = mid - 1
            else:
                l = mid + 1
        
        return ans
