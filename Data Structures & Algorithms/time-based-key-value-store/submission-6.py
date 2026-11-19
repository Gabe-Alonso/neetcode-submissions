class TimeMap:

    def __init__(self):
        self.tm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tm:
            self.tm[key].append([timestamp, value])
        else:
            self.tm[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.tm:
            tl = self.tm[key]
            if tl[0][0] > timestamp:
                return ""
            l = 0
            r = len(tl) - 1
            while l <= r:
                mid = (l + r) // 2
                if tl[mid][0] == timestamp:
                    return tl[mid][1]
                elif tl[mid][0] < timestamp:
                    l = mid + 1
                else:
                    r = mid - 1
            mid = (l + r) // 2
            if tl[mid][0] < timestamp:
                return tl[mid][1]
        return ""
        
