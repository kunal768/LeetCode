class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i.isalnum()]
        # print(s)
        return s == s[::-1]
