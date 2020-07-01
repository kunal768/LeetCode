class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0 :
            return 0 
        def recur(n,ans,row):
            if n < 0 :
                return ans
            
            return recur(n-row,ans+1,row+1)
        return recur(n,0,1)-1 
            
