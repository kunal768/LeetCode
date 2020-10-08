class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l, h = 0, len(arr)-1
        while l <= h :
            mid = (l+h)//2
            if arr[mid] == target:
                return mid 
            elif arr[mid] > target:
                h = mid - 1
            else:
                l = mid + 1 
        
        return -1
    
        
