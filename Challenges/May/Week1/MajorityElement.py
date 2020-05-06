# O(n) space  
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = defaultdict(lambda : 0)
        for i in nums :
            hashmap[i] += 1
            if hashmap[i] > n//2 :
                return i
        return -1
        
# O(1) space Approach 6: Boyer-Moore Voting Algorithm O(n) time 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = None
        count = 0 
        for i in nums :
            if count == 0 :
                maj = i 
            if i == maj : 
                count += 1
            else:
                count -= 1
        return maj
            
