class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append([timestamp, value])
        else:
            self.data[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        print("GET")
        if key not in self.data:
            return ""
        else:
            tl = self.data[key]
            print(tl)
            if tl[0][0] > timestamp:
                return ""
            l = 0
            r = len(tl) - 1
            while l < r:
                mid = (l + r) // 2
                print(mid)
                if timestamp == tl[mid][0]:
                    return tl[mid][1]
                elif timestamp > tl[mid][0] and timestamp < tl[mid + 1][0]:
                    return tl[mid][1]
                elif timestamp > tl[mid][0]:
                    l = mid + 1
                else:
                    r = mid - 1
            mid = (l + r) // 2
            print(mid)
            return tl[mid][1]
                

        
