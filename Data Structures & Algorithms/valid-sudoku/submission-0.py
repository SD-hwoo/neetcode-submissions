class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = dict()
        seen_col = dict()
        seen_sq = dict()
        for row in range(len(board)):
            if row not in seen_row:
                seen_row[row] = set()
            for col in range(len(board[row])):
                if col not in seen_col:
                    seen_col[col] = set()
                sq = (row // 3) * 3 + (col // 3)
                if sq not in seen_sq:
                    seen_sq[sq] = set()
                if board[row][col] != ".":
                    if board[row][col] in seen_row[row]:
                        return False
                    else:
                        seen_row[row].add(board[row][col])
                    if board[row][col] in seen_col[col]:
                        return False
                    else:
                        seen_col[col].add(board[row][col])
                    if board[row][col] in seen_sq[sq]:
                        return False
                    else:
                        seen_sq[sq].add(board[row][col])
        return True

