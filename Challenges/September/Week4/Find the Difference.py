# Good Efficient Way
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # haa xor ka concept use krlo har cheez double except one 
        x = 0 
        for i in s+t:
            x ^= ord(i)
        return chr(x)
 
 # Bad Way 
 class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = collections.Counter(s)
        t = collections.Counter(t)
        for i in t :
            if i not in c :
                return i
            else:
                if c[i] < t[i] :
                    return i 
        
        
