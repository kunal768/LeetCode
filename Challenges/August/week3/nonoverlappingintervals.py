class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0 
        count = 0
        intervals.sort(key = lambda x : (x[0],x[1]))
        start = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0] < start[1] :
                count += 1
                # remove interval with higher end point
                start[1] = min(intervals[i][1],start[1])
            else:
                start = intervals[i]
        return count
