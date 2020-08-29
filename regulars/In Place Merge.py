# in place merge sorting arrays
# technique -> start filling the array from reverse
# if l1 is greater put that in first and i -= 1 and vice versa
# in case of merge from starting of LL
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place insjtead.
        """
        i,j = m-1,n-1
        while i >= 0 and j >= 0  :
            if nums1[i] > nums2[j] :
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1
        
        if j >= 0 :
            while j >= 0 :
                nums1[j] = nums2[j]
                j -= 1
        
        
        
            
