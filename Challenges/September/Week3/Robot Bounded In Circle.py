
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''  directions = 1:up, 2 : down, 3 : left, 4 : right '''
        x,y,direction = 0,0,1
        def turn(command):
            nonlocal direction, x, y
            if direction == 1:
                if command == 'G':
                    y += 1
                elif command == 'L':
                    direction = 3
                elif command == 'R' :
                    direction = 4
                    
            elif direction == 2 :
                if command == 'G':
                    y -= 1
                elif command == 'L':
                    direction = 4
                elif command == 'R' :
                    direction = 3
                    
            elif direction == 3 :
                if command == 'G':
                    x -= 1
                elif command == 'L':
                    direction = 2
                else:
                    direction = 1
                    
            elif direction == 4 :
                if command == 'G':
                    x += 1
                elif command == 'L':
                    direction = 1
                else:
                    direction = 2
            
        
        for i in instructions :
            turn(i)
        
        if direction != 1 or x**2 + y**2  == 0 :
            return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
