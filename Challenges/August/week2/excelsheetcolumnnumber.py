class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for idx,val in enumerate(reversed(s)):
            ans += (26**idx)*(ord(val)-ord('A')+1)
        return ans
        
        
