class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                print("i: " + str(i) + ", j: " + str(j))
                if grid[i][j] == "1":
                    islands += 1
                    stack = []
                    stack.append((i, j))
                    while len(stack) > 0:
                        coord = stack.pop()
                        n, m = coord[0], coord[1]
                        print("n: " + str(n) + ", m: " + str(m))
                        grid[n][m] = "0"
                        if n > 0 and grid[n - 1][m] == "1" :
                            stack.append((n - 1, m))
                        if n < len(grid) - 1 and  grid[n + 1][m] == "1":
                            stack.append((n + 1, m))
                        if m > 0 and grid[n][m - 1] == "1":
                            stack.append((n , m - 1))
                        if m < len(grid[0]) - 1 and grid[n][m + 1] == "1":
                            stack.append((n, m + 1))
        return islands