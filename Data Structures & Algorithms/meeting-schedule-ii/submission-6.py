"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [0 for _ in range(len(intervals))]
        end = [0 for _ in range(len(intervals))]
        for i in range(len(intervals)):
            start[i] = intervals[i].start
            end[i] = intervals[i].end
        start.sort()
        end.sort()
        s = 0
        e = 0
        count = 0
        res = 0
        while s < len(start):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res
