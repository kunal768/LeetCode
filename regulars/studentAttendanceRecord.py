class Solution:
    # continuous LL 
    # see Logic 
    def checkRecord(self, s: str) -> bool:
        A,L = 0,0
        for i in s :
            if i == 'A' : A += 1
            if i == 'L' : L += 1
            elif i != 'L' : L = 0
            if L > 2 or A > 1:
                return False
        return True
 
