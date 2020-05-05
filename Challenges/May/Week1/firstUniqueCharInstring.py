class Solution:
    def firstUniqChar(self, s: str) -> int :
        d = dict(collections.Counter(s)) 
        for index,ch in enumerate(s):
            if d[ch] == 1:
                return index
        return -1
    
