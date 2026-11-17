class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ps = [(p, s) for p, s in zip(position, speed)]
        ps.sort(reverse=True)
        for p, s in ps:
            if len(stack) == 0:
                stack.append(float(target - p) / s)
            else:
                t1 = stack[-1]
                t2 = float(target - p) / s
                if t2 > t1:
                    stack.append(t2)

        return len(stack)