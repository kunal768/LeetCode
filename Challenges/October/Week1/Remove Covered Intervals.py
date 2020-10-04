class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], -x[1]))
        i = 0 
        while i+1 < len(intervals):
            if i + 1 < len(intervals) and intervals[i+1][1] <=  intervals[i][1] :
                intervals.pop(i+1)
            else:
                i += 1
        return len(intervals)
