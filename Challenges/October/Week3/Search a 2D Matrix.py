class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        c = len(matrix[0])-1
        for row in matrix:
            while c >= 0 and row[c] > target:
                c -= 1
            if c >= 0 and row[c] == target:
                return True
        
        return False
