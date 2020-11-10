class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i] = reversed(list(map(lambda x : 1 - x, A[i])))
        
        return A
