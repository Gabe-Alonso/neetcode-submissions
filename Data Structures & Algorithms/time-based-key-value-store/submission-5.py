class TimeMap:

    def __init__(self):
        self.tm = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tm:
            self.tm[key].append([timestamp, value])
        else:
            self.tm[key] = [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ""
        times = self.tm[key]
        # print(times)
        l = 0
        r = len(times) - 1
        while l <= r:
            mid = (l + r) // 2
            # print(f'l: {l}, r: {r}, mid: {mid}')
            if times[mid][0] == timestamp:
                return times[mid][1]
            elif times[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        if l > 0:
            return times[l - 1][1]
        return ""
        
