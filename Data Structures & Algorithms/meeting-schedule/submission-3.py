"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        if len(intervals) == 0:
            return True
        l = intervals[0].start
        r = intervals[0].end
        cur = 0
        while cur < len(intervals) - 1:
            # print(f'r: {r}')
            # print(f'interval: [{intervals[cur + 1].start}, {intervals[cur + 1].end}]')
            if r >= intervals[cur + 1].end or intervals[cur + 1].start < r < intervals[cur + 1].end:
                return False
            else:
                cur += 1
                l = intervals[cur].start
                r = intervals[cur].end
        return True