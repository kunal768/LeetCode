class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        num1,num2 = list(map(int,version1.split('.'))),list(map(int,version2.split('.')))
        d = abs(len(num1)-len(num2))
        num1 += [0]*d
        num2 += [0]*d
        i,j = 0,0
        while i < len(num1) and j < len(num2):
            if num1[i] < num2[j]:
                return -1 
            elif num1[i] > num2[j]:
                return 1
            else:
                i += 1
                j += 1
        return 0 
        
        
                                                            
        
        
