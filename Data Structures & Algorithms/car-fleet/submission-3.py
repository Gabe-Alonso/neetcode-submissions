class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ps = []
        for i in range(len(position)):
            ps.append([position[i], speed[i]])
        ps.sort()
        ps.reverse()
        for p, s in ps:
            if len(stack) == 0:
                stack.append([p, s])
            else:
                t1 = float(target - stack[-1][0]) / stack[-1][1]
                t2 = float(target - p) / s
                if t2 > t1:
                    stack.append([p,s])

        return len(stack)