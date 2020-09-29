class Solution(object):
    def findJudge(self, n, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        inn = [0]*n
        out = [0]*n
        for pair in trust:
            inn[pair[1]-1] += 1
            out[pair[0]-1] += 1
        
        
        for i in range(n):
            if inn[i] == n-1 and out[i] == 0 :
                return i+1 
        return -1
            
           