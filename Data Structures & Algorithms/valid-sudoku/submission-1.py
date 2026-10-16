class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = []
        for x in range(3):
            cur = []
            for y in range(3):
                cur.append(set([]))
            squares.append(cur)
        # print(squares)
        columns = [set([]) for _ in range(9)]
        rows = [set([]) for _ in range(9)]
        for x in range(9):
            for y in range(9):
                # print(f'x,y: {x},{y}, square:[{int(x/3)}][{int(y/3)}], val: {board[x][y]}')
                if board[x][y] != '.':
                    if board[x][y] not in columns[y] and board[x][y] not in rows[x] and board[x][y] not in squares[int(x/3)][int(y/3)]:
                        columns[y].add(board[x][y])
                        rows[x].add(board[x][y])
                        squares[int(x/3)][int(y/3)].add(board[x][y])
                    else:
                        # print(f'val: {board[x][y]}')
                        # if board[x][y] in columns[y]:
                        #     print(f"board[{x}][{y}] in columns[{y}]: {columns[y]}")
                        # if board[x][y] in rows[x]:
                        #     print(f"board[{x}][{y}] in rows[{x}]: {rows[x]}")
                        # if board[x][y] in squares[int(x/3)][int(y/3)]:
                        #     print(f"board[{x}][{y}] in squares[{int(x/3)}][{int(y/3)}]: {squares[int(x/3)][int(y/3)]} ")
                        return False
        return True