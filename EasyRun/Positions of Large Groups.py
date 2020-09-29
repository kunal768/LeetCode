# Two Pointers Baby ;)
class Solution(object):
    def largeGroupPositions(self, s):
        i, j = 0, 0
        n = len(s)
        ans = []
        while i < n and j < n :
            while j < n and s[i] == s[j] :
                j += 1
                
            if j-i >= 3 :
                ans.append([i, j-1])
            
            i = j
                
        
        return sorted(ans, key = lambda x : x[0])