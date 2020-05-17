class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) <= len(p) :
            return [0] if s == p else []
        ans = []
        pattern = [0]*26
        for l in p :
            pattern[ord(l) - ord("a")] += 1
        print(pattern)
        apointer = 0 
        bpointer = 0
        while bpointer < len(s):
            # first expand to size k 
            while bpointer < len(p) :
                pattern[ord(s[bpointer]) - ord("a")] -= 1
                bpointer += 1
                
            if not any(pattern):
                ans.append(apointer)
            
            # slide right 
            pattern[ord(s[apointer])-ord("a")] += 1
            pattern[ord(s[bpointer])-ord("a")] -= 1
            apointer += 1
            bpointer += 1
        
        if not any(pattern):
            ans.append(apointer)
        
        return ans
