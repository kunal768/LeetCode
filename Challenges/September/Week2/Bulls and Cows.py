class Solution:
    def getHint(self, secret: str, guess: str) -> str:        
        sh,gh = collections.defaultdict(int),collections.defaultdict(int)
        cows,bulls = 0,0
        for s,g in zip(secret,guess):
            if s == g :
                bulls += 1
            else:
                sh[s] += 1
                gh[g] += 1
        
        cows = sum(min(sh[k],gh[k]) for k in sh if k in gh)
        return "{}A{}B".format(bulls,cows)
