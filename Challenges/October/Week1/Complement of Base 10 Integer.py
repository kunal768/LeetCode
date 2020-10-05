# One - Way
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        s = list(map(lambda x : "0" if x == "1" else "1",list(bin(N)[2:]) ))
        return int("".join(s), 2)

# Two - Way
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        c = 1
        while c < N:
            c = (c << 1) + 1
        return N ^ c
        
