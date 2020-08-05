
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = [(startTime[i],endTime[i],profit[i]) for i in range(n)]
        jobs.sort(key = lambda x : x[1])
        dp = [0]*n
        dp[0] = jobs[0][2]
        def lastNonConflict(i):
            for j in range(i-1,-1,-1):
                if jobs[j][1] <= jobs[i][0] :
                    return j 
            return -1
        for i in range(1,n):
            incl = jobs[i][2]
            l = lastNonConflict(i)
            if l != -1 :
                incl += dp[l] 
            dp[i] = max(dp[i-1],incl)
       
        return dp[-1]
    
        
