class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        hash = set(J)
        count = 0
        for i in S :
            if i in hash :
                count += 1
        return count
                
        
