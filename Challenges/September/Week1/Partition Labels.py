class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c : i for  i ,c in enumerate(S)}
        j,anchor = 0,0
        ans = []
        for i,c in enumerate(S):
            j = max(j,last[c])
            if i == j :
                ans.append(i-anchor+1)
                anchor = i+1
        return ans
        
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ans = []
        if len(S) == 0 :
            return ans
        seen = set()
        hm = collections.Counter(S)
        count = 0 
        for c in S :
            count += 1
            seen.add(c)
            hm[c] -= 1
            if hm[c] == 0:
                seen.remove(c)
                if not seen :
                    ans.append(count)
                    count = 0 
        return ans
