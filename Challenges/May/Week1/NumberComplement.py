# noob way (Doing it just coz i can :p)
class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num)[2:]
        s = s.replace("1","-1")
        s = s.replace("0","1")
        s = s.replace("-1","0")
        return int(s,2)
    
