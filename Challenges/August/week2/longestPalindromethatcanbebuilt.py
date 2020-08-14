class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s :
            return 0 
        hs = set()
        c = 0
        for i in s :
            if i in hs :
                hs.remove(i)
                c += 1
            else:
                hs.add(i)
        if hs :
            return 2*c + 1
        return 2*c
