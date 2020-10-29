# My AC solution Time : O(N) Space : O(N)
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # max(min(gtl, gtr))
        n = len(seats)
        leftone = [float('inf')]*n
        lastseenone = -1
        for i in range(len(seats)):
            if seats[i] == 1 :
                lastseenone = i 
            else:
                if lastseenone != -1 :
                    leftone[i] = i - lastseenone
        
        
        rightone = [float('inf')]*n
        lastseenone = -1
        for i in range(len(seats)-1,-1,-1):
            if seats[i] == 1 :
                lastseenone = i 
            
            else :
                if lastseenone != -1:
                    rightone[i] = lastseenone - i
        
        
        
        ans = float('-inf')
        for i in range(n):
            x, y = leftone[i], rightone[i]
            if x != float('inf') or y != float('inf') :
                ans = max(ans, min(x, y))
        
        return ans
  
  
# Most Efficient Editorial Solution (Groupby Zero) Time : O(N) Space : O(1)
'''
Algorithm

For each group of K empty seats between two people, we can take into account the candidate answer (K+1) / 2.

For groups of empty seats between the edge of the row and one other person, the answer is K, and we should take into account those answers too.
'''

class Solution(object):
    def maxDistToClosest(self, seats):
        ans = seats.index(1)
        seats.reverse()
        ans = max(ans,seats.index(1))
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K+1)/2)

        return ans

            
            
