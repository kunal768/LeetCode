class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        ans = 0
        for idx,val in enumerate(citations):
            if val >= len(citations)-idx :
                ans = max(ans,len(citations)-idx)
        return ans
                
