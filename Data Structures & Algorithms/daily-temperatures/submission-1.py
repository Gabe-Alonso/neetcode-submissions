class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i, t in enumerate(temperatures):
            print(i)
            print(t)
            if not stack:
                stack.append([i, t])
            else:
                if t <= stack[-1][1]:
                    stack.append([i, t])
                else:
                    while stack and t > stack[-1][1]:
                        print(stack)
                        res[stack[-1][0]] = i - stack[-1][0]
                        stack.pop()
                    stack.append([i, t])
                    print(res)
        return res