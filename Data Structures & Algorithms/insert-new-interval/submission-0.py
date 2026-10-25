class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = newInterval[0]
        r = newInterval[1]
        i = 0
        newIntervals = []
        while i < len(intervals):
            # Before
            if r < intervals[i][0]:
                newIntervals.append([l, r])
                while i < len(intervals):
                    newIntervals.append(intervals[i])
                    i += 1
                return newIntervals

            # In
            elif intervals[i][0] <= l <= intervals[i][1] or intervals[i][0] <= r <= intervals[i][1]:
                l = min(l, intervals[i][0])
                r = max(r, intervals[i][1])
            
            # After
            elif intervals[i][1] < l:
                newIntervals.append(intervals[i])
            
            i += 1

        newIntervals.append([l, r])
        return newIntervals