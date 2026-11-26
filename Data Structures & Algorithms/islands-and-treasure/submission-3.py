from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Process starting from each treasure?
        # Expand in all directions? 
        # Then Use the following distances to calculate the next distances?
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        queue = deque([])
        count = 1
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 0:
                    queue.append((y,x))
        
        def traverse(y, x, count):
            nonlocal seen
            if (y,x) in seen:
                return
            seen.add((y,x))
            if grid[y][x] in [0, -1]:
                return
            if count < grid[y][x]:
                grid[y][x] = count
            
            for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if 0 <= ny < rows and 0 <= nx < cols:
                    traverse(ny, nx, count + 1)
            
        while queue:
            seen = set()
            cy, cx = queue.popleft()
            
            for ny, nx in ((cy + 1, cx), (cy - 1, cx), (cy, cx + 1), (cy, cx - 1)):
                if 0 <= ny < rows and 0 <= nx < cols:
                    if grid[ny][nx] == 2147483647:
                        grid[ny][nx] = grid[cy][cx] + 1
                        queue.append((ny, nx))

