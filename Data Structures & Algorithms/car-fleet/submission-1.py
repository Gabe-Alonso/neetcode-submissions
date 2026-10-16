class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        comb = []
        for i in range(len(position)):
            comb.append((position[i], speed[i]))
        comb.sort()
        print(comb)
        for i in range(len(comb) - 1, -1, -1):
            print(comb[i])
            if len(stack) == 0:
                stack.append(comb[i])
            else:
                t1 = (target - stack[-1][0]) / stack[-1][1]
                t2 = (target - comb[i][0]) / comb[i][1]
                print("Time to beat:")
                print(t1)
                print("Challenger:")
                print(t2)
                if t2 > t1:
                    stack.append(comb[i])
                    
        return len(stack)