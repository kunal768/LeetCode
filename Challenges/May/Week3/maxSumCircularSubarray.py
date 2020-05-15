'''
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)


'''
# Accepted solution

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        currMax,currMin,maxsum,minsum,total = 0,0,-float("inf"),float("inf"),0
        for a in A:
            currMax = max(a,currMax+ a)
            currMin = min(a,currMin+ a)
            maxsum = max(maxsum,currMax)
            minsum = min(minsum,currMin)
            total += a
        
        return max(maxsum,total-minsum) if maxsum > 0 else maxsum



# Rotate the arr and calculate gives TLE on large inputs  
class Solution:
    def kadanes(self,arr):
        curr,maxx,n = arr[0],arr[0],len(arr)
        for i in range(1,n):
            curr = max(arr[i],curr+arr[i])
            maxx = max(maxx,curr)
        return maxx
    
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        maxOP = float("-inf")
        n = len(A)
        for i in range(n):
            A = A[-1:] + A [:-1]
            maxOP = max(maxOP,self.kadanes(A))
        return maxOP
            
