class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = [i for i in s.split(" ") if i]
        if l :
            return len(l[-1])
        return 0
