class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            print(stack)
            if len(stack) == 0:
                stack.append((i, heights[i]))
            else:
                if heights[i] >= stack[-1][1]:
                    stack.append((i, heights[i]))
                else:
                    start = i
                    while len(stack) > 0 and heights[i] < stack[-1][1]:
                        print("Popping: " + str(stack[-1]))
                        max_area = max(max_area, (stack[-1][1] * (i - stack[-1][0])))
                        print("Max Area: " + str(max_area))
                        start = stack[-1][0]
                        stack.pop()
                    stack.append((start, heights[i]))
        while len(stack) > 0:
            print("Popping: " + str(stack[-1]))
            max_area = max(max_area, (stack[-1][1] * (len(heights) - stack[-1][0])))
            print("Max Area: " + str(max_area))
            stack.pop()

        return max_area