# Binary Search O(logn) runtime and O(1) space
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            m = (lo + hi) // 2
            if m % 2 == 1 and nums[m - 1] == nums[m]:
                lo = m + 1
            elif  m % 2 == 0 and nums[m + 1] == nums[m]:
                lo = m + 2
            else:
                hi = m
        return nums[lo]
    

# O(n) runtime and O(1) space
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        prev = None 
        curr = 0 
        n = len(nums)
        for idx,val in enumerate(nums):
            if val != prev :
                curr += 1
            else :
                curr -= 1
            # val lies somewhere in middle
            if curr == 2 :
                return nums[idx-1] 
            # last val is the val 
            elif curr == 1 and idx == n - 1 :
                return val
            
            prev = val

        return -1
