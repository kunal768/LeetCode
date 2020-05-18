# Much dissapointed this was same as yesterday's question you could just paste the whole code with ine line alteration 
class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        if len(s) <= len(p) :
            return sorted(s) == sorted(p) 
        pattern = [0]*26
        for l in p :
            pattern[ord(l) - ord("a")] += 1
        
        apointer = 0 
        bpointer = 0
        while bpointer < len(s):
            # first expand to size k 
            while bpointer < len(p) :
                pattern[ord(s[bpointer]) - ord("a")] -= 1
                bpointer += 1
                
            if not any(pattern):
                return True 
            
            # slide right 
            pattern[ord(s[apointer])-ord("a")] += 1
            pattern[ord(s[bpointer])-ord("a")] -= 1
            apointer += 1
            bpointer += 1
        
        if not any(pattern):
            return True
        
        return False
