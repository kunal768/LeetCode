# DP Solution 
class Solution:
    def countBits(self, num: int) -> List[int]:
        cnt = 0 
        if num == 0 :
            return [0]
        if num == 1:
            return [0,1]
        
        setBits = [0 for x in range(num+1)]
        setBits[0] = 0
        setBits[1] = 1
        for i in range(2,num+1):
            if i & 1 == 0 :
                setBits[i] = setBits[i//2]
            else:
                setBits[i] = setBits[i-1] + 1
        
        return setBits
