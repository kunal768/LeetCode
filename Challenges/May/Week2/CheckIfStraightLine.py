# brute force - check slope same that would be O(n2)
# best would be form equation check all satisfy eqn O(n)

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1 = coordinates[0][0],coordinates[0][1]
        x2,y2 = coordinates[1][0],coordinates[1][1]
        if x2 - x1 == 0 :
            m = None
            c = -x1
        else :
            m = (y2-y1)//(x2-x1)
            c =  y1 - m*x1
            
        if len(coordinates) == 2 :
            return True
        
        def equation(x,y,m) :
            if m == None :
                if x == -c :
                    return True
                return False
            
            if (y != m*x + c) :
                return False
            return True
        
        n = len(coordinates)
        
        for i in range(2,n) :
            x = coordinates[i][0]
            y = coordinates[i][1]
            if equation(x,y,m) == False:
                return False
        return True
