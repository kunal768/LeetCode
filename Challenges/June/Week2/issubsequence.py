class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def dfs(s,t,m,n):
            if m == 0 :
                return True 
            if n == 0 :
                return False
            # last character matching 
            if s[m-1] == t[n-1]:
                return dfs(s,t,m-1,n-1)
            return dfs(s,t,m,n-1)
        return dfs(s,t,len(s),len(t))
        
