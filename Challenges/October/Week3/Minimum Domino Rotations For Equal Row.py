class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        x = reduce(set.__and__, (set(d) for d in zip(A, B)))
        if not x :
            return -1
        char = x.pop()
        return min(len(A) - A.count(char), len(B) - B.count(char))
    
