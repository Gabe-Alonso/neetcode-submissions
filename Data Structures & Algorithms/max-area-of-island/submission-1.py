class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    stack = []
                    stack.append((i, j))
                    area = 0
                    while len(stack) > 0:
                        coord = stack.pop()
                        n, m = coord[0], coord[1]
                        print("n: " + str(n) + ", m: " + str(m))
                        if grid[n][m] == 1:
                            area += 1
                            grid[n][m] = 0
                            if n > 0 and grid[n - 1][m] == 1:
                                stack.append((n - 1, m))
                            if n < len(grid) - 1 and grid[n + 1][m] == 1:
                                stack.append((n + 1, m))
                            if m > 0 and grid[n][m - 1] == 1:
                                stack.append((n, m - 1))
                            if m < len(grid[0]) - 1 and grid[n][m + 1] == 1:
                                stack.append((n, m + 1))
                    max_area = max(max_area, area)
        return max_area