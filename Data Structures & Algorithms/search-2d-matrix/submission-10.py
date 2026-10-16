class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        if len(matrix) == 1 and len(matrix[0]) == 1:
            if matrix[0][0] == target:
                return True
            return False
        
        
        l = 0
        r = len(matrix) * len(matrix[0]) - 1
        while l <= r:
            i = l + (r - l) // 2
            print("L: " + str(l) + ", R:" + str(r))
            cur = matrix[i // len(matrix[0])][i % len(matrix[0])]
            print(i)
            print(cur)
            if cur != target:
                if target < cur:
                    r = i - 1
                else:
                    l = i + 1
            else:
                return True
        return False