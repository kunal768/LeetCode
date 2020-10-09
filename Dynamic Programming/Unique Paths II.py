class Solution:
    def uniquePathsWithObstacles(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            if matrix[i][0] == 1 :
                break
            else:
                dp[i][0] = 1
        
        for j in range(m):
            if matrix[0][j] == 1 :
                break
            else:
                dp[0][j] = 1
        
        
        for r in range(1, n):
            for c in range(1, m):
                if matrix[r][c] == 0 :
                    dp[r][c] = (dp[r][c-1] if c - 1 >= 0 else 0) + (dp[r-1][c] if r-1 >= 0 else 0 ) 
        
        return dp[n-1][m-1]
