# without groupby O(1) space and O(n) Time
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        ans = 0
        i = 0 
        while i < len(s):
            c = 0 
            while i + 1 < len(s) and s[i] == s[i+1]:
                i += 1
                c += 1
            
            ans = max(ans, c)
            c = 0
            i += 1
        
        return ans+1
   
# Using Groupby 
from itertools import groupby
class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0 
        for k, grp in gropuby(s):
            ans = max(ans, len(list(grp)))
        
        return ans
