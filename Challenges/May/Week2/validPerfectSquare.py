# O(n) way but there's got to be some bitwise solution to this also 
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1 
        while i * i <= num :
            if i == math.ceil(num/i) :
                return True
            i += 1 
        return False
       
