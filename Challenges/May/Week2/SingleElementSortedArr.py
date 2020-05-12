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
