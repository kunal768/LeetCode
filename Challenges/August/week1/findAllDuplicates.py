# very very important concept
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for num in nums :
            index=abs(num)-1
            if nums[index]<0: 
                ans.append(abs(num))
            nums[index]=-nums[index]
        return ans      
            
