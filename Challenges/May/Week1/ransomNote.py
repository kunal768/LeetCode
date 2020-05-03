# 1 way : O(nlogn) pattern matching using KMP sorted strings but O(1) space
# 2 way : O(2n) space O(n) time using two CounterDicts

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = dict(Counter(ransomNote))
        dict2 = dict(Counter(magazine))
        
        for i in dict1 :
            if not i in dict2 :
                return False
            else:
                if dict1[i] > dict2[i] :
                    return False
        return True
         
