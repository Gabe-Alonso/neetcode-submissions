class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [[p, s] for p, s in zip(position, speed)]
        ps.sort(reverse=True)
        stack = []
        for p, s in ps:
            if len(stack) == 0:
                stack.append(float(target - p) / s)
            else:
                time = float(target - p) / s
                if time > stack[-1]:
                    stack.append(time)
        return len(stack)