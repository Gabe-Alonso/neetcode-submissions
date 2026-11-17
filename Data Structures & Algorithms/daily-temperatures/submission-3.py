class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for i, t in enumerate(temperatures):
            if len(stack) > 0 and t > stack[-1][0]:
                while stack and t > stack[-1][0]:
                    res[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
            stack.append([t, i])
        return res