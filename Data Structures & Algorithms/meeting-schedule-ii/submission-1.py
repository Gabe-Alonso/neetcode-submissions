"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()
        s = 0
        e = 0
        active = 0
        max_active = 0
        while s < len(intervals) or e < len(intervals):
            if s < len(intervals) and starts[s] < ends[e]:
                s += 1
                active += 1
                max_active = max(max_active, active)
            else:
                e += 1
                active -= 1
        return max_active