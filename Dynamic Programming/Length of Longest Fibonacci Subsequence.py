class Solution(object):
    def lenLongestFibSubseq(self, nums):
        # Write your code here
        maxx = 0 
        s = set(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                x,y = nums[j], nums[i]+nums[j]
                cnt = 2
                while y in s :
                    x, y = y, x + y
                    cnt += 1
                maxx = max(maxx,cnt)
        return maxx if maxx >= 3 else 0 
