# Code written as per the logic provided in the Hint section 
# HINT : Give candy to everyone each "turn" first [until you can't], then give candy to one person per turn.

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ways = [0]*num_people
        i = 0
        while candies > i+1:
            ways[i%num_people] += i + 1
            candies -= i+1
            i += 1
        
        while candies > 0:
            ways[i%num_people] += 1
            candies -= 1
        return ways
            
        
            
