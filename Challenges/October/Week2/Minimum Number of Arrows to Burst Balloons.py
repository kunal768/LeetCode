class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # its just simple calculating number of overlapping intervals
        if not points:
            return 0 
        points.sort(key = lambda x : (x[1], x[0]))
        
        end = points[0][1]
        ans = 1
        
        for point in points :
            if point[0] <= end :
                continue 
            
            ans += 1
            end = point[1]
        
        return ans
        
