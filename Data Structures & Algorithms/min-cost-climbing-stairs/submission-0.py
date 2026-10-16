class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = []
        for i in range(len(cost)):
            if i == 0 or i == 1:
                cache.append(0)
            else:
                cache.append(min(cache[i - 1] + cost[i - 1], cache[i - 2] + cost[i - 2]))
        return min(cache[-1] + cost[-1], cache[-2] + cost[-2])
