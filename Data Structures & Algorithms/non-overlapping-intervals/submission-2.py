class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        r = intervals[0][1]
        deletes = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < r:
                r = min(intervals[i][1], r)
                deletes += 1
            else:
                r = intervals[i][1] 
        return deletes