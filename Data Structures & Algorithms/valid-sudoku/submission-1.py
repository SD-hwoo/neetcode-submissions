class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_row = [set() for _ in range(9)]
        seen_col = [set() for _ in range(9)]
        seen_sq = [set() for _ in range(9)]
        for row in range(len(board)):
            for col in range(len(board[row])):
                sq = (row // 3) * 3 + (col // 3)
                if board[row][col] == ".":
                    continue
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

