#LIS using Binary Search Concept, append if large, replace if small 
# https://www.youtube.com/watch?v=1RpMc3fv0y4 for concept
class Solution:
    def solve(self, nums):
        if not nums :
            return 0
        n = len(nums)
        dp = []
        def bsearch(arr, x):
            l, r, ans = 0, len(arr) - 1, -1
            while l <= r :
                mid = (l+r)//2
                if arr[mid] > x :
                    ans = mid 
                    r = mid - 1
                elif arr[mid] < x:
                    l = mid + 1
                else:
                    return mid
            
            return ans

        for x in nums:
            if not dp :
                dp.append(x)
            else:
                res = bsearch(dp, x)
                if res == -1 :
                    dp.append(x)
                else:
                    dp[res] = x

        return len(dp)
