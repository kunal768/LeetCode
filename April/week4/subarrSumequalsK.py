from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        hashmap = defaultdict(lambda : 0)
        n = len(nums)
        summ = 0
        for i in range(n) :
            summ += nums[i]
            if summ == k:
                count += 1
            if summ - k in hashmap :
                count += hashmap[summ-k]
            hashmap[summ] += 1
                
        return count
            
 
