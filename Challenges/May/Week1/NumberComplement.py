# good way XORING with an array of 1's
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0 : return 1
        if N == 1  : return 0
        c = 1
        while c <= N:
            c <<= 1
        return (c-1) ^ N


# noob way (Doing it just coz i can :p)
class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num)[2:]
        s = s.replace("1","-1")
        s = s.replace("0","1")
        s = s.replace("-1","0")
        return int(s,2)
    
