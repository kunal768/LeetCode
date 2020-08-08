class Solution:
    def minSteps(self, s: str, t: str) -> int:
        letters = "abcdefghijklmnopqrstuvwxyz"
        fs = {i:0 for i in letters}
        ft = {i:0 for i in letters}
        for i in s : fs[i] += 1
        for j in t : ft[j] += 1
        count = 0
        for x in letters :
            if ft[x] < fs[x] :
                count += fs[x]-ft[x]
        return count
