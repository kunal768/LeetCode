# BFS Approach O(n^3)
class Solution:
    def solve(self, words, s):
        q = [0]
        vis = set()
        wordset = set(words)
        while q :
            st = q.pop(0)
            if st in vis : continue
            vis.add(st)
            for en in range(st+1, len(s)+1):
                if s[st:en] in wordset:
                    if en == len(s):
                        return True 
                    q.append(en)
                
            
        return False
