class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i, t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append([t, i])
            else:
                while len(stack) > 0 and stack[-1][0] < t:
                    res[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                stack.append([t, i])
        return res