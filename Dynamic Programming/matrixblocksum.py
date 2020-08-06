class Solution:
    def matrixBlockSum(self, matrix: List[List[int]], K: int) -> List[List[int]]:
        n,m = len(matrix),len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        prefix = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                prefix[i+1][j+1] = matrix[i][j] + prefix[i+1][j] + prefix[i][j+1] - prefix[i][j]
    
        for i in range(n):
            for j in range(m):
                r1 = max(0,i-K)
                c1 = max(0,j-K)
                r2 = min(i+K,n-1)
                c2 = min(j+K,m-1)
                dp[i][j] = prefix[r2+1][c2+1] - prefix[r2+1][c1] - prefix[r1][c2+1] + prefix[r1][c1]
        return dp
                
            
