class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, h = 0, len(nums)-1
        while l <= h :
            if nums[l] == val :
                nums[l] = nums[h]
                h -= 1
            else:
                l += 1
        return h+1