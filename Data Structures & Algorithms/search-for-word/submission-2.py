class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Each level, check char by char, in all 4 directions
        # If a char is found, recurse
        # If a char is not found, return and remove from path?
        seen = set()

        found = False

        # Find starting points
        starting_points = []
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == word[0]:
                    starting_points.append((y, x))

        def backtracking(start, place):
            nonlocal found
            if found:
                return
            if start in seen:
                return
            seen.add((start[0], start[1]))
            if board[start[0]][start[1]] == word[place]:
                if place == (len(word) - 1):
                    found = True
                    return

                # Down
                if start[0] + 1 < len(board):
                    backtracking((start[0] + 1, start[1]), place + 1)

                # Up
                if start[0] - 1 >= 0:
                    backtracking((start[0] - 1, start[1]), place + 1)

                # Left
                if start[1] - 1 >= 0:
                    backtracking((start[0], start[1] - 1), place + 1)

                # Right
                if start[1] + 1 < len(board[0]):
                    backtracking((start[0], start[1] + 1), place + 1)
                
            seen.remove((start[0], start[1]))

        for point in starting_points:
            backtracking(point, 0)
            if found:
                return True

        return False