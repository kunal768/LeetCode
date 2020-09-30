# O(n) time O(n) space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        i = 1
        while i in nums :
            i += 1
        return i
    
# O(n) time O(1) space 
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        while i <= j :
            if nums[i] > j+1 or nums[i] <= 0 or (nums[i] == nums[nums[i]-1] and i != nums[i]-1):
                nums[i] = nums[j]
                j -= 1
            elif i == nums[i] - 1 :
                i += 1
                continue
            else :
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        return i + 1 
