from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Process starting from each treasure?
        # Expand in all directions? 
        # Then Use the following distances to calculate the next distances?
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([])
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 0:
                    queue.append((y,x))
        while queue:
            cy, cx = queue.popleft()
            
            for ny, nx in ((cy + 1, cx), (cy - 1, cx), (cy, cx + 1), (cy, cx - 1)):
                if 0 <= ny < rows and 0 <= nx < cols:
                    if grid[ny][nx] == 2147483647:
                        grid[ny][nx] = grid[cy][cx] + 1
                        queue.append((ny, nx))

