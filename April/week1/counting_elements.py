# hence we got accepted 
from collections import defaultdict
class Solution:
    def countElements(self, arr: List[int]) -> int:
        hashmap = defaultdict(lambda:0)
        for i in arr:
            hashmap[i]+=1
        
        c = 0
        for i in hashmap :
            if i+1 in hashmap:
                c += hashmap[i]
        return c 