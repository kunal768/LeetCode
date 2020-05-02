"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""


# minimize thus this is a DP problem


def minPathSum(grid) :
	if grid == None or len(grid) == 0 :
		return 0 
	dp = [[0 for i in range(gird[0])] for i in range(grid)] 
	# create a dp table 	
	for i in range(len(drip)):
		for j in range(len(drip[0])):
			dp[i][j] = grid[i][j]
			if(i > 0 and j > 0):
				dp[i][j] = min(dp[i-1][j],dp[i][j-1])
			elif i > 0 :
				dp[i][j] += dp[i-1][j]
			elif j > 0 :
				dp[i][j] += dp[i][j-1]
	return dp[len(dp)-1][len(dp[0] - 1)]










