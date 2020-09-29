# Rotate String - Part 1 (BF way but works)
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        n = len(A)
        for _ in range(n):
            A = A[-1] + A[:-1]
            if A == B :
                return True
        return False
            
'''
All rotations of A are contained in A+A. Thus, we can simply check whether B is a substring of A+A. We also need to check A.length == B.length, otherwise we will fail cases like A = "a", B = "aa".
'''


class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(A) == len(B) and B in A+A
    
        


