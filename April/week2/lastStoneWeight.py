class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:    
        stones.sort()
        while len(stones) >= 1:
            if(len(stones)) == 1:
                break			
            y,x = stones[-1],stones[-2]
            stones.remove(x)
            stones.remove(y)
            if x == y :
                pass
            else :
                stones.append(y-x)
            stones.sort()	
        return stones[0] if len(stones) == 1 else 0

