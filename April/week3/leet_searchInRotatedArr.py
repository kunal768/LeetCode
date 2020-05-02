class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0: 
            return -1 
        n = len(nums)
        # finding pivot 
        left = 0
        right = n-1
        while left < right :
            mid = left + (right-left)//2
            if nums[mid] > nums[right] :
                left = mid + 1
            else :
                right = mid
        # left is the pivot
        start = left 
        left = 0
        right = n-1
        if target >= nums[start] and target <= nums[right] :
            # array is sorted
            left = start
        else :
            right = start
        
        # now binary search 
        while (left <= right) :
            mid = left + (right - left)//2
            if nums[mid] == target :
                return mid 
            elif nums[mid] < target :
                left = mid + 1
            else :
                right = mid - 1
        
        return -1
            