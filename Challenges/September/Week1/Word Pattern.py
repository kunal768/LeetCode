class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        pat = [x for x in pattern]
        string = string.split(" ")
        n = len(pat)
        if n != len(string) :
            return False
        hm = {}
        hmr = {}
        for i in range(n):
            if string[i] in hm and pat[i] in hmr :
                if hm[string[i]] != pat[i] or hmr[pat[i]] != string[i]:
                    return False
                else:
                    continue
            elif string[i] in hm or pat[i] in hmr :
                return False
            else:
                hmr[pat[i]] = string[i]
                hm[string[i]] = pat[i]
        return True
    
