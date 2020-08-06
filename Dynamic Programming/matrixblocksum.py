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
                
            
# Concept of Prefix Sum in matrix 
def prefixsumMatrix(matrix):
	n,m = len(matrix),len(matrix[0])
	prefixsum = [[0 for _ in range(m)] for _ in range(n)]
	prefixsum[0][0] = matrix[0][0]

	# fill the first row and column 
	for i in range(1,m):
		prefixsum[0][i] = prefixsum[0][i-1] + matrix[0][i]

	for i in range(1,n):
		prefixsum[i][0] = prefixsum[i-1][0] + matrix[i][0]

	# updating values in all cells 
	# prefixsum[i][j] = prefixsum[i-1][j] + prefixsum[i][j-1] - prefixsum[i-1][j-1] + matrix[i][j]

	for i in range(1,n):
		for j in range(1,m):
			prefixsum[i][j] = prefixsum[i-1][j] + prefixsum[i][j-1] - prefixsum[i-1][j-1] + matrix[i][j]

	print(prefixsum)
	return prefixsum
