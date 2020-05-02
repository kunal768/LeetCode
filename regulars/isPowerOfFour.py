class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1 or n == 4 :
            return True
        if n == 2 or n == 3 :
            return False
        return self.isPowerOfFour(n/4)