# calculated all factorials
dp = [0]*34 
dp[0] = 1
dp[1] = 1
dp[2] = 2 
for i in range(3,34):
    dp[i] = i * dp[i-1]

class Solution:    
    def getRow(self, k: int) -> List[int]:
        if k == 0 :
            return [1]
        ans = []
        for i in range(0,k+1):
            ans.append(dp[k]//(dp[k-i]*dp[i]))
        return ans
