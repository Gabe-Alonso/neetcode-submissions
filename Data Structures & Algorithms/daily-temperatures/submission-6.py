class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append([temperatures[i], i])
            else:
                while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                    cur = stack.pop()
                    res[cur[1]] = i - cur[1]
                stack.append([temperatures[i], i])
        return res