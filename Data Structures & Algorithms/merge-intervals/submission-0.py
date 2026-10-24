class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        cur = 0
        l = intervals[0][0]
        r = intervals[0][1]
        while cur < len(intervals) - 1:
            if r >= intervals[cur + 1][1]:
                cur += 1
            elif intervals[cur + 1][0] <= r < intervals[cur + 1][1]:
                r = intervals[cur + 1][1]
                cur += 1
            else:
                res.append([l, r])
                cur += 1
                l = intervals[cur][0]
                r = intervals[cur][1]
        res.append([l, r])
        return res