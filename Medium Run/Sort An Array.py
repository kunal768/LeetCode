class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(A, B):
            ans = []
            i, j = 0, 0 
            while i < len(A) and j < len(B) :
                if A[i] <= B[j] :
                    ans.append(A[i])
                    i += 1
                else:
                    ans.append(B[j])
                    j += 1
            
            while i < len(A) :
                ans.append(A[i])
                i += 1
            
            while j < len(B):
                ans.append(B[j])
                j += 1
            
            return ans
            
        def mergesort(arr):
            if len(arr) <= 1 :
                return arr
            mid = len(arr)//2
            left, right = mergesort(arr[:mid]), mergesort(arr[mid:])
            return merge(left, right)
    
        return mergesort(nums)
        
