from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        queue = deque([])
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])

        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 2:
                    queue.append((y,x))
                if grid[y][x] == 1:
                    fresh += 1
        
        while fresh and queue:
            for _ in range(len(queue)):
                y, x = queue.popleft()
                for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if 0 <= ny < rows and 0 <= nx < cols:
                        if grid[ny][nx] == 1:
                            queue.append((ny, nx))
                            grid[ny][nx] = 2
                            fresh -= 1
            minutes += 1
        return minutes if fresh == 0 else -1
        
