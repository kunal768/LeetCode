# square -> rnum = cnum 
# 

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        if r > 0 :
            c = len(matrix[0])
        else:
            c = 0
        dp = [[0 for i in range(c+1)] for i in range(r+1)]
        maxLen = 0 
        for i in range(1,r+1):
            for j in range(1,c+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
                    maxLen = max(maxLen,dp[i][j])
        
        return maxLen*maxLen
        
        