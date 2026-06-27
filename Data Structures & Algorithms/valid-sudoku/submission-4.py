class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        rowset = defaultdict(set)
        colset = defaultdict(set)
        boxset = defaultdict(set)

        for r in range(rows):
            for c in range(cols):

                val = board[r][c]
                if val == ".":
                    continue
                
                if (val in rowset[r] or val in colset[c] or val in boxset[(r//3, c//3)]):
                    return False
                rowset[r].add(val) 
                colset[c].add(val)
                boxset[(r//3, c//3)].add(val)
        
        return True