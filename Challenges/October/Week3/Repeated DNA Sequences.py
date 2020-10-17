# Kind of sliding window but Bad Space complexity way (Still AC)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10 :
            return []
        
        seen = collections.defaultdict(lambda : 0)
        i, j = 0, 10
        while i < len(s) and j <= len(s):
            seen[s[i:j]] += 1
            i += 1
            j += 1
        
        return [string for string in seen if seen[string] > 1]
        
