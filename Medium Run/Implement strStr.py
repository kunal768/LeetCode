class Solution:
    def strStr(self, text: str, pat: str) -> int:
        # edge cases 
        if text == pat or not pat:
            return 0
        # kmp 
        def kmp(s, m):
            n = len(s)
            pi = [0]*n
            for i in range(1, n):
                j = pi[i-1]
                while j > 0 and s[i] != s[j]:
                    j = pi[j-1]
                if s[i] == s[j] :
                    j += 1
                pi[i] = j 
            
            b = []
            for i in range(m+1, n):
                if pi[i] == m:
                    b.append((i - 2*m, i - m))
            
            return b
        
        new = kmp(pat + "$" + text, len(pat))
        if new :
            return new[0][0] 
        return -1
        
