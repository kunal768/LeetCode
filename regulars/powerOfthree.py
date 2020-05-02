# keep dividing by 3 until remainder is 0 
# should be divisible if n == 1 while remainder is 0 

# recursive 
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0 or n == 2:
            return False
        if n == 1 or n == 3:
            return True
        return self.isPowerOfThree(n / 3)


# iterative
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while(n%3 == 0 ):
            n //= 3
            
        return (n == 1)