class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # return maximum from prefix and suffix 
        prefix,suffix,maxx = 0,0,float('-inf')
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            maxx = max(prefix,suffix,maxx)
        return maxx
