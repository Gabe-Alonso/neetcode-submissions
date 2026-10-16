class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print("ROWS:")
        for i in range(len(board)):
            used = {}
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in used:
                        return False
                    used[board[i][j]] = 1
            print(used)
        print("COLUMNS:")
        for i in range(len(board)):
            used = {}
            for j in range(len(board)):
                #print("y = " + str(j) + ", x = " + str(i))
                #print(board[j][i])
                if board[j][i] != ".":
                    if board[j][i] in used:
                        return False
                    used[board[j][i]] = 1
                #print(used)
            print(used)
        print("SUB BOXES:")
        for i in range(3):
            for j in range(3):
                used = {}
                for k in range(3):
                    for l in range(3):
                        #print("y = " + str(i*3 + k) + ", x = " + str(j*3 + l))
                        if board[i*3 + k][l + j*3] != ".":
                            if board[i*3 + k][l + j*3] in used:
                                return False
                            used[board[i*3 + k][l + j*3]] = 1
                print(used)
        return True
        