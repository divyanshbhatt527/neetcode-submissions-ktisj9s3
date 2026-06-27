class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        rowset = defaultdict(set)
        colset = defaultdict(set)
        squares = defaultdict(set)

        for r in range(rows):
            for c in range(cols):
                val = board[r][c]
                if val == ".":
                    continue
                if (val in rowset[r] or val in colset[c]
                    or val in squares[(r//3,c//3)]):
                    return False
                else:
                    rowset[r].add(val)
                    colset[c].add(val)
                    squares[(r//3,c//3)].add(val)

        else:
            return True
