class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nz = 0 
        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[i], nums[nz] = nums[nz], nums[i]
                nz += 1
        
        
                
            
            
