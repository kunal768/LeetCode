class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid == None or len(grid) == 0 :
            return 0 
        dp = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]  
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                dp[i][j] += grid[i][j]
                if(i > 0 and j > 0):
                    dp[i][j] += min(dp[i-1][j],dp[i][j-1])
                elif i > 0 :
                    dp[i][j] += dp[i-1][j]
                elif j > 0 :
                    dp[i][j] += dp[i][j-1]
        return dp[len(dp)-1][len(dp[0]) - 1]
        