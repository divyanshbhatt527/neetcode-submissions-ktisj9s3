class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        rowset = defaultdict(set)
        colset = defaultdict(set)
        squares = defaultdict(set)

        for r in range(rows):
            for c in range(cols):

                if board[r][c] == ".":
                    continue
                if (board[r][c] in rowset[r] or board[r][c] in colset[c]
                    or board[r][c] in squares[(r//3,c//3)]):
                    return False
                else:
                    rowset[r].add(board[r][c])
                    colset[c].add(board[r][c])
                    squares[(r//3,c//3)].add(board[r][c])

        else:
            return True
