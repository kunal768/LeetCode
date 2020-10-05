# Bad Way and O(N) space O(N) time
class Solution:
    def longestPrefix(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            if s[:i] == s[-i:]:
                ans = s[:i]
        return ans

# KMP Way O(1) space O(N) time 
