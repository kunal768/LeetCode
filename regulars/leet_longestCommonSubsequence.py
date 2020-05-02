class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        lcs = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 0 or j == 0 :
                    dp[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    lcs = max(lcs,dp[i][j])
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return lcs