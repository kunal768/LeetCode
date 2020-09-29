class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            l, h = i, min(i+k-1, len(a)-1)
            while l < h :
                temp = a[l]
                a[l] = a[h]
                a[h] = temp
                l += 1
                h -= 1
        
        return "".join(a)
                
            