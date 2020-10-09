# Look at the solution and think, it will make sense 
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Bottom Up Solution
        # dp of arriving at a particular cell = min(dp of arriving from left cell or dp of arriving from top cell)
        
        r, c = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                if i == r-1 and j == c - 1 :
                    dp[i][j] = min(0, dungeon[i][j])
                
                elif i == r-1 :
                    dp[i][j] = min(0, dungeon[i][j] + dp[i][j+1])
                
                elif j == c-1:
                    dp[i][j] = min(0, dungeon[i][j] + dp[i+1][j])
                
                else :
                    dp[i][j] = min(0, dungeon[i][j] + max(dp[i][j+1], dp[i+1][j]))
            
        return abs(dp[0][0]) + 1
