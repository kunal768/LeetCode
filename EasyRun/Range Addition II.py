'''
Approach #2 Single Pass [Accepted]
Algorithm

As per the given problem statement, all the operations are performed on a rectangular sub-matrix of the initial all 0's MMM matrix. The upper left corner of each such rectangle is given by the index (0,0)(0, 0)(0,0) and the lower right corner for an operation [i,j][i, j][i,j] is given by the index (i,j)(i, j)(i,j).

The maximum element will be the one on which all the operations have been performed. The figure below shows an example of two operations being performed on the initial MMM array.
'''

# Ultra Smart Approach 
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        for op in ops :
            m, n = min(m, op[0]), min(n, op[1])
        
        return m*n
