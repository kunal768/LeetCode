# Reference : https://www.geeksforgeeks.org/maximum-xor-of-two-numbers-in-an-array/
class Solution:
    def findMaximumXOR(self, arr: List[int]) -> int:
        maxx,mask = 0,0
        se = set()
        for i in range(30,-1,-1):
            mask |= 1 << i
            newMaxx = maxx | (1 << i)
        
            for i in range(len(arr)):
                se.add(arr[i] & mask)

            for prefix in se :
                if newMaxx ^ prefix in se :
                    maxx = newMaxx
                    break
 
            se.clear()
        return maxx
