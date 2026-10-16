class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        cur_sol = max(piles) + 1
        while l <= r:
            print("L: " + str(l) + ", R: " + str(r))
            k = (l + r) // 2
            print(k)
            hours = 0
            for p in piles:
                print(p)
                hours += math.ceil(float(p) / k)
                print("Hours: " + str(hours))
            if hours <= h:
                cur_sol = min(cur_sol, k)
                r = k - 1
            else:
                l = k + 1
        return cur_sol