class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, h = 0, len(nums) - 1
        while l < h :
            if nums[l] + nums[h] == target :
                return [l+1, h+1]
            elif nums[l] + nums[h] > target :
                h -= 1
            else:
                l += 1
        
        
        
