# buit in way
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        mapping = sorted(c.items(),key = lambda x : x[1],reverse = True)
        ans = ""
        for i in mapping :
            ans += i[0]*i[1]
        return ans
        
