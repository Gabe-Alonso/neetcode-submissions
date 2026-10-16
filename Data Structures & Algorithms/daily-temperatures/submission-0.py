class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        diffs = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            if len(stack) > 0:
                
                while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                    print(stack)
                    diffs[stack[-1]] = i - stack[-1]
                    stack.pop()
            stack.append(i)
        while len(stack) > 0:
            diffs[stack.pop()] = 0
        return diffs